import os
import io
import json
from typing import Dict, Tuple
from flask import Flask, request, jsonify, send_from_directory, send_file
from flask_cors import CORS
from dotenv import load_dotenv

print("[STARTUP] Loading environment variables...", flush=True)
load_dotenv()

print("[STARTUP] Initializing Flask app...", flush=True)
app = Flask(__name__, static_folder='public', static_url_path='')

CORS(app, resources={
    r"/*": {
        "origins": "*",
        "methods": ["GET", "POST"],
        "allow_headers": ["Content-Type"]
    }
})

@app.after_request
def set_security_headers(response):
    response.headers['X-Frame-Options'] = 'SAMEORIGIN'
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['Content-Security-Policy'] = (
        "default-src 'self'; "
        "script-src 'self' 'unsafe-inline' https://cdn.jsdelivr.net; "
        "style-src 'self' 'unsafe-inline' https://fonts.googleapis.com; "
        "font-src 'self' https://fonts.gstatic.com; "
        "img-src 'self' data: https:; "
        "connect-src 'self'"
    )
    response.headers['Referrer-Policy'] = 'strict-origin-when-cross-origin'
    response.headers['Permissions-Policy'] = 'geolocation=(), microphone=(), camera=()'
    return response

print("[STARTUP] Flask app initialized successfully", flush=True)

GEMINI_MODEL = 'gemini-2.5-flash'
DEFAULT_PORT = 8000
REQUEST_TIMEOUT = 180
GUNICORN_WORKERS = 1
GUNICORN_THREADS = 2

API_VERSION = '1.0.1'
SERVICE_NAME = 'AI SEO Audit Team API'


@app.route('/health', methods=['GET'])
def health_check() -> Tuple[Dict, int]:
    print("[HEALTH] Health check endpoint called")
    return jsonify({
        'status': 'healthy',
        'service': SERVICE_NAME,
        'version': API_VERSION
    }), 200


@app.route('/readiness', methods=['GET'])
def readiness_check() -> Tuple[Dict, int]:
    try:
        api_key = os.getenv('GOOGLE_API_KEY')
        if not api_key:
            return jsonify({
                'status': 'not_ready',
                'reason': 'GOOGLE_API_KEY not configured'
            }), 503

        print("[READINESS] Readiness check passed")
        return jsonify({
            'status': 'ready',
            'service': SERVICE_NAME,
            'version': API_VERSION
        }), 200
    except Exception as e:
        print(f"[READINESS ERROR] {str(e)}")
        return jsonify({
            'status': 'not_ready',
            'reason': str(e)
        }), 503


@app.route('/diagnostic', methods=['GET'])
def diagnostic() -> Tuple[Dict, int]:
    diagnostics = {
        'service': SERVICE_NAME,
        'version': API_VERSION,
        'timestamp': None,
        'checks': {}
    }

    all_ok = True

    try:
        api_key = os.getenv('GOOGLE_API_KEY')
        diagnostics['checks']['env_vars'] = {
            'status': 'OK' if api_key else 'FAILED',
            'google_api_key': 'configured' if api_key else 'MISSING',
            'render': 'yes' if os.getenv('RENDER') else 'no'
        }
        if not api_key:
            all_ok = False
    except Exception as e:
        diagnostics['checks']['env_vars'] = {'status': 'ERROR', 'error': str(e)}
        all_ok = False

    try:
        from google import genai
        diagnostics['checks']['google_genai'] = {
            'status': 'OK',
            'import': 'success'
        }
    except Exception as e:
        diagnostics['checks']['google_genai'] = {
            'status': 'FAILED',
            'import': 'failed',
            'error': str(e)
        }
        all_ok = False

    try:
        from web_scraper import scrape_url
        diagnostics['checks']['web_scraper'] = {
            'status': 'OK',
            'import': 'success'
        }
    except Exception as e:
        diagnostics['checks']['web_scraper'] = {
            'status': 'FAILED',
            'import': 'failed',
            'error': str(e)
        }
        all_ok = False

    try:
        from scoring_system import calculate_scores
        diagnostics['checks']['scoring_system'] = {
            'status': 'OK',
            'import': 'success'
        }
    except Exception as e:
        diagnostics['checks']['scoring_system'] = {
            'status': 'FAILED',
            'import': 'failed',
            'error': str(e)
        }
        all_ok = False

    if diagnostics['checks']['env_vars'].get('google_api_key') == 'configured':
        try:
            from google import genai
            client = genai.Client(api_key=os.getenv('GOOGLE_API_KEY'))
            diagnostics['checks']['genai_client'] = {
                'status': 'OK',
                'client': 'initialized'
            }
        except Exception as e:
            diagnostics['checks']['genai_client'] = {
                'status': 'FAILED',
                'error': str(e)
            }
            all_ok = False
    else:
        diagnostics['checks']['genai_client'] = {
            'status': 'SKIPPED',
            'reason': 'API key not configured'
        }
        all_ok = False

    diagnostics['overall_status'] = 'HEALTHY' if all_ok else 'UNHEALTHY'

    status_code = 200 if all_ok else 503
    return jsonify(diagnostics), status_code


@app.route('/')
def index():
    return send_from_directory('public', 'index.html')


@app.route('/invoke', methods=['POST'])
def invoke_agent() -> Tuple[Dict, int]:
    print("[INVOKE] Endpoint /invoke chamado", flush=True)

    try:
        data = request.get_json()
        if not data:
            print("[INVOKE ERROR] Nenhum JSON recebido", flush=True)
            return jsonify({'error': 'Nenhum dado JSON recebido'}), 400

        url = data.get('message', '')
        print(f"[INVOKE] URL recebida: {url}", flush=True)

        if not url:
            print("[INVOKE ERROR] URL vazia", flush=True)
            return jsonify({'error': 'URL não fornecida'}), 400

        if not url.startswith('http://') and not url.startswith('https://'):
            url = 'https://' + url
            print(f"[INVOKE] URL ajustada para: {url}", flush=True)

        print(f"[INVOKE] Iniciando análise para URL: {url}", flush=True)

        api_key = os.getenv('GOOGLE_API_KEY')
        if not api_key:
            print("[INVOKE ERROR] GOOGLE_API_KEY não configurada", flush=True)
            return jsonify({'error': 'GOOGLE_API_KEY não configurada no servidor'}), 500

        print("[INVOKE] API key encontrada, importando dependências...", flush=True)

        try:
            from google import genai
            print("[INVOKE] google.genai importado com sucesso", flush=True)
        except ImportError as e:
            print(f"[INVOKE ERROR] Erro ao importar google.genai: {e}", flush=True)
            return jsonify({'error': f'Erro ao importar google.genai: {str(e)}'}), 500

        try:
            from web_scraper import scrape_url
            from scoring_system import calculate_scores
            print("[INVOKE] web_scraper e scoring_system importados com sucesso", flush=True)
        except ImportError as e:
            print(f"[INVOKE ERROR] Erro ao importar módulos locais: {e}", flush=True)
            return jsonify({'error': f'Erro ao importar módulos: {str(e)}'}), 500

        try:
            client = genai.Client(api_key=api_key)
            print("[INVOKE] Cliente GenAI criado com sucesso", flush=True)
        except Exception as e:
            print(f"[INVOKE ERROR] Erro ao criar cliente GenAI: {e}", flush=True)
            return jsonify({'error': f'Erro ao conectar com Google GenAI: {str(e)}'}), 500

        print(f"[INVOKE] Executando pipeline de 4 agentes com DADOS REAIS...", flush=True)

        real_data = scrape_url(url)
        if not real_data.get('success'):
            return jsonify({
                'error': f"Não foi possível acessar o site: {real_data.get('error', 'Erro desconhecido')}"
            }), 400

        print(f"[SCRAPING] ✓ Dados coletados!")
        print(f"[SCRAPING]   URL: {real_data['final_url']}")
        print(f"[SCRAPING]   Status: {real_data['status_code']}")
        print(f"[SCRAPING]   Tempo: {real_data['load_time']}s")

        scores_data = calculate_scores(real_data)
        print(f"[SCORING] ✓ Scores calculados:")
        print(f"[SCORING]   SEO: {scores_data['seo']['score']}/100 ({scores_data['seo']['classification']})")
        print(f"[SCORING]   CRO: {scores_data['cro']['score']}/100 ({scores_data['cro']['classification']})")
        print(f"[SCORING]   GEO: {scores_data['geo']['score']}/100 ({scores_data['geo']['classification']})")
        print(f"[SCORING]   Overall: {scores_data['overall']['score']}/100")

        page_audit = _execute_page_auditor(client, real_data)
        serp_analysis = _execute_serp_analyst(client, page_audit)
        cro_analysis = _execute_cro_analyst(client, real_data)
        final_report = _execute_strategic_advisor(client, url, real_data, scores_data,
                                                   page_audit, serp_analysis, cro_analysis)

        print(f"[SUCCESS] Análise completa finalizada!")
        return jsonify({'output': final_report})

    except json.JSONDecodeError as e:
        error_msg = f'Erro ao processar JSON dos agentes: {str(e)}'
        print(f"[ERROR] {error_msg}")
        return jsonify({'error': error_msg}), 500

    except ImportError as e:
        error_msg = f'Erro ao importar google.genai: {str(e)}'
        print(f"[ERROR] {error_msg}")
        return jsonify({'error': 'Módulo google-genai não disponível'}), 500

    except Exception as e:
        import traceback
        error_trace = traceback.format_exc()
        print(f"[ERROR] Exception: {error_trace}")
        return jsonify({
            'error': f'Erro interno: {str(e)}',
            'details': error_trace if app.debug else None
        }), 500


def _execute_page_auditor(client, real_data: Dict) -> Dict:
    """
    Agent 1: Page Auditor - Analyzes SEO on-page with real data.

    Args:
        client: Google GenAI client
        real_data: Real data extracted from website

    Returns:
        Dictionary with audit results and target keywords
    """
    print(f"[AGENT 1] Page Auditor - Analisando dados REAIS...")

    real_data_summary = f"""
DADOS REAIS EXTRAÍDOS DO SITE:
- URL: {real_data['url']}
- Título Real: {real_data['title']}
- Meta Description Real: {real_data['meta_description']}
- Contagem REAL de palavras: {real_data['word_count']}
- Links REAIS: {real_data['links']['total']} total ({real_data['links']['internal']} internos, {real_data['links']['external']} externos)
- Headings encontrados: {json.dumps(real_data['headings'], ensure_ascii=False)}
- Imagens: {real_data['images']['total']} ({real_data['images']['without_alt']} sem alt text)
- Tem SSL (HTTPS): {real_data['has_ssl']}
- Mobile-friendly: {real_data['mobile_friendly']}
- Structured Data (Schema.org): {', '.join(real_data['schema_types']) if real_data['schema_types'] else 'Nenhum'}
- Tempo de carregamento: {real_data['load_time']}s
"""

    page_audit_prompt = f"""You are Agent 1 in a sequential SEO workflow. You have REAL DATA extracted from the website.

REAL DATA FROM THE SITE:
{real_data_summary}

TASK: Analyze this REAL data and create a structured audit. Identify:
1. Primary and secondary keywords based on REAL title, headings, and meta description
2. SEO issues found in the REAL data
3. Opportunities for improvement

Return ONLY a JSON object:
{{
  "target_keywords": {{
    "primary_keyword": "keyword extracted from real title/H1",
    "secondary_keywords": ["keyword from H2s", "keyword from content"],
    "search_intent": "informational/transactional/navigational"
  }},
  "audit_results": {{
    "title_tag": "{real_data['title']}" (this is REAL),
    "meta_description": "{real_data['meta_description']}" (this is REAL),
    "word_count": {real_data['word_count']} (this is REAL),
    "link_counts": {json.dumps(real_data['links'])} (this is REAL),
    "findings": ["list REAL SEO issues found", "e.g., missing H1", "images without alt", "slow load time", etc.]
  }}
}}

IMPORTANT: Use ONLY the real data provided. DO NOT simulate or invent data."""

    response = client.models.generate_content(
        model=GEMINI_MODEL,
        contents=page_audit_prompt
    )

    result_text = _extract_json_from_response(response.text.strip())
    page_audit = json.loads(result_text)

    print(f"[AGENT 1] ✓ Concluído - Palavra-chave: {page_audit['target_keywords']['primary_keyword']}")
    return page_audit


def _execute_serp_analyst(client, page_audit: Dict) -> Dict:
    """
    Agent 2: SERP Analyst - Simulates competitive SERP analysis.

    Args:
        client: Google GenAI client
        page_audit: Results from Page Auditor

    Returns:
        Dictionary with SERP analysis and content opportunities
    """
    print(f"[AGENT 2] SERP Analyst - Iniciando...")

    primary_keyword = page_audit['target_keywords']['primary_keyword']
    serp_prompt = f"""You are Agent 2. Your function is to analyze the competitive SERP for the keyword: "{primary_keyword}"

*Simulate* the competitive SERP for that keyword, inferring:
- Top competitor titles
- Common content formats
- Key themes/angles used by competitors

Return ONLY a JSON object:
{{
  "primary_keyword": "{primary_keyword}",
  "serp_results": [
    {{"position": 1, "title": "título do resultado", "domain": "dominio.com", "content_format": "artigo/vídeo/produto"}},
    {{"position": 2, "title": "título do resultado", "domain": "dominio.com", "content_format": "artigo/vídeo/produto"}}
  ],
  "content_opportunities": ["oportunidade 1", "oportunidade 2"]
}}"""

    response = client.models.generate_content(
        model=GEMINI_MODEL,
        contents=serp_prompt
    )

    result_text = _extract_json_from_response(response.text.strip())
    serp_analysis = json.loads(result_text)

    print(f"[AGENT 2] ✓ Concluído - {len(serp_analysis.get('serp_results', []))} resultados simulados")
    return serp_analysis


def _execute_cro_analyst(client, real_data: Dict) -> Dict:
    """
    Agent 3: CRO Analyst - Analyzes usability and conversion optimization.

    Args:
        client: Google GenAI client
        real_data: Real data extracted from website

    Returns:
        Dictionary with usability findings and conversion opportunities
    """
    print(f"[AGENT 3] CRO Analyst - Analisando usabilidade com dados REAIS...")

    cro_real_data = f"""
DADOS TÉCNICOS REAIS PARA ANÁLISE CRO:
- Tempo de carregamento REAL: {real_data['load_time']}s
- Mobile-friendly: {"✓ Sim" if real_data['mobile_friendly'] else "✗ NÃO (PROBLEMA CRÍTICO)"}
- HTTPS/SSL: {"✓ Seguro" if real_data['has_ssl'] else "✗ Inseguro (PROBLEMA CRÍTICO)"}
- Imagens sem ALT text: {real_data['images']['without_alt']} de {real_data['images']['total']}
- Total de palavras: {real_data['word_count']}
- Structured Data: {', '.join(real_data['schema_types']) if real_data['schema_types'] else 'Nenhum (oportunidade perdida)'}
- Status HTTP: {real_data['status_code']}
"""

    cro_prompt = f"""You are Agent 3, specialized in CRO and UX. Analyze REAL technical data from the website.

URL: {real_data['url']}

REAL TECHNICAL DATA:
{cro_real_data}

REAL PAGE STRUCTURE:
- H1 tags found: {len(real_data['headings'].get('h1', []))} (should have exactly 1)
- H2 tags: {len(real_data['headings'].get('h2', []))}
- H3 tags: {len(real_data['headings'].get('h3', []))}

TASK: Based on this REAL data, identify:
1. REAL usability issues (e.g., slow loading, no mobile optimization, missing SSL)
2. REAL conversion opportunities (e.g., add structured data, optimize images, improve load time)

Return ONLY a JSON object:
{{
  "usability_findings": [
    {{"issue": "REAL issue found in data", "severity": "high/medium/low", "evidence": "reference to real data"}}
  ],
  "conversion_opportunities": [
    {{"opportunity": "specific improvement based on real data", "impact": "high/medium/low", "rationale": "why this matters based on evidence"}}
  ]
}}

IMPORTANT: Base your analysis ONLY on the real data provided. If mobile-friendly is false, that's a HIGH severity issue. If load time > 3s, that's a problem. Be specific and reference real numbers."""

    response = client.models.generate_content(
        model=GEMINI_MODEL,
        contents=cro_prompt
    )

    result_text = _extract_json_from_response(response.text.strip())
    cro_analysis = json.loads(result_text)

    print(f"[AGENT 3] ✓ Concluído - {len(cro_analysis.get('conversion_opportunities', []))} oportunidades")
    return cro_analysis


def _execute_strategic_advisor(client, url: str, real_data: Dict, scores_data: Dict,
                                page_audit: Dict, serp_analysis: Dict, cro_analysis: Dict) -> str:
    """
    Agent 4: Strategic Advisor - Generates final professional report in Portuguese.

    Args:
        client: Google GenAI client
        url: Analyzed URL
        real_data: Real data extracted from website
        scores_data: Calculated scores
        page_audit: Results from Agent 1
        serp_analysis: Results from Agent 2
        cro_analysis: Results from Agent 3

    Returns:
        Markdown formatted professional report
    """
    print(f"[AGENT 4] Strategic Advisor - Gerando relatório final...")

    final_prompt = f"""You are a Senior Digital Strategist. Generate a PROFESSIONAL, CONCISE report in Portuguese (pt-BR) for {url}.

CRITICAL RULE: Use ONLY real data provided. NEVER invent numbers, percentages, or data.

═══════════════════════════════════════════════
DADOS REAIS EXTRAÍDOS:
═══════════════════════════════════════════════

URL: {url}
Data da Análise: {scores_data['timestamp']}

SCORES CALCULADOS (baseados em dados reais):
• Score Geral: {scores_data['overall']['score']}/100 - {scores_data['overall']['classification']}
• SEO Score: {scores_data['seo']['score']}/100 - {scores_data['seo']['classification']}
• CRO Score: {scores_data['cro']['score']}/100 - {scores_data['cro']['classification']}
• GEO Score: {scores_data['geo']['score']}/100 - {scores_data['geo']['classification']}

SEO Breakdown:
- On-Page SEO: {scores_data['seo']['breakdown']['on_page_seo']}/25
- Technical SEO: {scores_data['seo']['breakdown']['technical_seo']}/25
- Content Quality: {scores_data['seo']['breakdown']['content_quality']}/25
- Performance: {scores_data['seo']['breakdown']['core_web_vitals']}/25

Page Audit: {json.dumps(page_audit, indent=2, ensure_ascii=False)}
SERP Analysis: {json.dumps(serp_analysis, indent=2, ensure_ascii=False)}
CRO Analysis: {json.dumps(cro_analysis, indent=2, ensure_ascii=False)}

═══════════════════════════════════════════════

Generate a PROFESSIONAL report with this structure:

# Relatório de Auditoria Digital Estratégica

> Análise realizada em: {scores_data['timestamp']}

---

**URL Analisada:** {url}

---

## Índice de Performance Digital

```
╔══════════════════════════════════════════════════════╗
║  SCORE GERAL: {scores_data['overall']['score']}/100 - {scores_data['overall']['classification']}                    ║
╠══════════════════════════════════════════════════════╣
║  SEO Health:        {scores_data['seo']['score']}/100  {scores_data['seo']['progress_bar']}      ║
║  CRO Readiness:     {scores_data['cro']['score']}/100  {scores_data['cro']['progress_bar']}      ║
║  GEO Optimization:  {scores_data['geo']['score']}/100  {scores_data['geo']['progress_bar']}      ║
╚══════════════════════════════════════════════════════╝
```

**Classificação dos Scores:**
- 80-100: Excelente | 60-79: Bom | 40-59: Requer Otimização | 0-39: Crítico

---

## Sumário Executivo

[Write a concise 3-4 sentence professional summary in Portuguese highlighting the main findings and strategic recommendations. Focus on business impact and actionable insights. Based ONLY on REAL data.]

**Principais Achados:**
- **Forças Identificadas:** [List 2-3 strengths based on REAL data with specific metrics]
- **Oportunidades de Melhoria:** [List 2-3 critical issues based on REAL data with specific metrics]
- **Prioridade Estratégica:** [State the #1 priority action based on lowest score component]

---

## 1. Auditoria SEO - Search Engine Optimization

### Score SEO: {scores_data['seo']['score']}/100 - {scores_data['seo']['classification']}

**Detalhamento:**
- On-Page (tags e meta dados): {scores_data['seo']['breakdown']['on_page_seo']}/25
- Aspectos Técnicos: {scores_data['seo']['breakdown']['technical_seo']}/25
- Qualidade do Conteúdo: {scores_data['seo']['breakdown']['content_quality']}/25
- Velocidade do Site: {scores_data['seo']['breakdown']['core_web_vitals']}/25

### Análise dos Dados Reais:

#### On-Page Elements

**Title Tag:**
- Conteúdo: "{real_data['title']}"
- Comprimento: {len(real_data['title'])} caracteres
- Avaliação: [Evaluate: Ótimo (50-60 chars), Adequado (40-70 chars), Requer Otimização (fora dessa faixa)]
- [Provide professional analysis of title tag effectiveness for SEO and CTR]

**Meta Description:**
- Conteúdo: "{real_data['meta_description']}"
- Comprimento: {len(real_data['meta_description'])} caracteres
- Avaliação: [Evaluate: Ótimo (150-160 chars), Adequado (140-170 chars), Requer Otimização (fora dessa faixa)]

**Estrutura de Headings:**
- H1: {len(real_data['headings'].get('h1', []))} | Padrão ideal: 1 único H1 por página
- H2: {len(real_data['headings'].get('h2', []))}
- Status da Hierarquia: [Evaluate if heading structure is optimal]

#### Content Analysis

**Volume de Conteúdo:**
- Total de palavras: {real_data['word_count']}
- Classificação: [Classify: Thin Content (<300), Adequado (300-1000), Conteúdo Robusto (>1000)]
- [Provide professional recommendation based on word count]

**Otimização de Imagens:**
- Total de imagens: {real_data['images']['total']}
- Com atributo ALT: {real_data['images']['with_alt']}
- Sem atributo ALT: {real_data['images']['without_alt']}
- Taxa de cobertura: [Calculate percentage]
- [If images without ALT > 0, explain the SEO and accessibility impact]

#### Technical SEO

**Segurança e Protocolo:**
- HTTPS: {"Implementado" if real_data['has_ssl'] else "NÃO IMPLEMENTADO - CRÍTICO"}
- Status SSL: [Provide security assessment]

**Mobile Optimization:**
- Meta Viewport: {"Configurado" if real_data['mobile_friendly'] else "NÃO CONFIGURADO - CRÍTICO"}
- Mobile-Friendly: [Assess mobile readiness]

**Performance:**
- Tempo de carregamento: {real_data['load_time']}s
- Classificação: [Classify: Excelente (<2s), Bom (<4s), Requer Otimização (>4s)]

**Structured Data:**
- Schemas implementados: {len(real_data['schema_types'])}
- Tipos: {', '.join(real_data['schema_types']) if real_data['schema_types'] else 'Nenhum'}
- [Assess schema implementation and recommendations]

---

## 2. Análise Competitiva - SERP Intelligence

[Analyze the competitive landscape based on serp_analysis data. Present key competitors, their strategies, and opportunities for differentiation. Keep it concise and data-driven.]

### Principais Insights Competitivos:
[List 3-5 key competitive findings from SERP analysis]

### Oportunidades de Diferenciação:
[Identify content gaps and strategic opportunities based on competitive analysis]

---

## 3. Auditoria CRO - Conversion Rate Optimization

### Score CRO: {scores_data['cro']['score']}/100 - {scores_data['cro']['classification']}

**Detalhamento:**
- Efetividade de CTAs: {scores_data['cro']['breakdown']['cta_effectiveness']}/20
- Otimização de Formulários: {scores_data['cro']['breakdown']['form_optimization']}/20
- Confiança e Credibilidade: {scores_data['cro']['breakdown']['trust_credibility']}/20
- Experiência da Página: {scores_data['cro']['breakdown']['page_experience']}/20
- Mobile: {scores_data['cro']['breakdown']['mobile_readiness']}/20

[Analyze CRO findings from cro_analysis data. Focus on conversion barriers, user experience issues, and optimization opportunities. Keep analysis professional and data-driven.]

### Principais Achados CRO:
[List key conversion optimization findings based on cro_analysis]

---

## 4. Otimização GEO - Generative Engine Optimization

### Score GEO: {scores_data['geo']['score']}/100 - {scores_data['geo']['classification']}

**Análise de Structured Data:**
- Schemas implementados: {len(real_data['schema_types'])}
- Tipos: {', '.join(real_data['schema_types']) if real_data['schema_types'] else 'Nenhum detectado'}
- Status: [Assess quality and completeness of schema implementation]
- Impacto para IA: [Explain how current schema setup affects AI visibility and recommendations]

**Preparação para AI Search Engines:**
[Assess how well the site is optimized for AI-powered search engines like ChatGPT, Bard, and Perplexity]

---

## Recomendações Estratégicas Priorizadas

### Prioridade Alta - Implementação Imediata

[Generate 3-5 HIGH-PRIORITY recommendations based on REAL deficiencies found in data. Use professional, concise language.]

#### Recomendação 1: [Title based on most critical issue]
- **Situação Atual:** [Describe current state using REAL data]
- **Impacto no Negócio:** [Explain business/technical impact]
- **Ação Recomendada:** [Specific implementation steps]
- **Resultado Esperado:** [Realistic improvement expectation]
- **Esforço Estimado:** [Time/complexity assessment]

[Repeat format for 2-4 more high-priority recommendations]

### Prioridade Média - Otimizações Incrementais

[Generate 2-3 MEDIUM-PRIORITY recommendations in same format]

### Backlog - Melhorias Futuras

[Generate 1-2 NICE-TO-HAVE improvements in same format]

---

## Roadmap de Implementação (30 Dias)

**Semana 1:**
- [ ] [Action 1 based on high priority]
- [ ] [Action 2 based on high priority]

**Semana 2-3:**
- [ ] [Medium priority actions from recommendations]

**Semana 4:**
- [ ] [Review implementation and measure results]

---

## Metodologia e Disclaimer

**Data da Análise:** {scores_data['timestamp']}

**Fonte dos Dados:**
- Extração técnica via web scraping (BeautifulSoup + Requests)
- Análise de HTML, CSS e elementos estruturais
- Medição de performance e tempo de resposta
- Detecção de structured data (Schema.org)

**Nota Importante:**
Este relatório baseia-se exclusivamente em dados reais extraídos do website no momento da análise. Todos os números, métricas e scores são calculados a partir de evidências técnicas verificáveis. Nenhuma informação foi inferida ou simulada além dos dados coletados.

Websites são dinâmicos e mudam constantemente. Recomendamos realizar novas análises a cada 30 dias para monitorar progresso e identificar novas oportunidades.

---

**SiteScore - Auditoria Digital Estratégica**
*Relatório Técnico Profissional*

---

IMPORTANT INSTRUCTIONS:
- Return ONLY the markdown content above
- NO preamble, NO JSON wrapping, NO code blocks around the markdown
- Keep the report CONCISE, PROFESSIONAL, and DATA-DRIVEN
- Use ONLY real data provided - never invent metrics
- Maintain formal business tone throughout"""

    response = client.models.generate_content(
        model=GEMINI_MODEL,
        contents=final_prompt
    )

    final_report = response.text.strip()

    if '```markdown' in final_report:
        final_report = final_report.split('```markdown')[1].split('```')[0].strip()
    elif final_report.startswith('```') and final_report.endswith('```'):
        final_report = final_report[3:-3].strip()

    print(f"[AGENT 4] ✓ Concluído - Relatório gerado ({len(final_report)} caracteres)")
    return final_report


def _extract_json_from_response(text: str) -> str:
    """
    Extract JSON content from AI response, removing markdown code blocks.

    Args:
        text: Raw response text from AI model

    Returns:
        Clean JSON string
    """
    if '```json' in text:
        return text.split('```json')[1].split('```')[0].strip()
    elif '```' in text:
        return text.split('```')[1].split('```')[0].strip()
    return text


@app.route('/generate-pdf', methods=['POST'])
def generate_pdf() -> Tuple[Dict, int]:
    """
    Generate PDF from markdown report.
    Currently disabled due to WeasyPrint system dependencies.

    Returns:
        PDF file or error message
    """
    try:
        data = request.get_json()
        markdown_text = data.get('markdown', '')
        url_analisada = data.get('url', 'URL não especificada')

        if not markdown_text:
            return jsonify({'error': 'Markdown não fornecido'}), 400

        print(f"[INFO] Gerando PDF para URL: {url_analisada}")

        from pdf_generator import markdown_to_pdf

        pdf_bytes = markdown_to_pdf(markdown_text, url_analisada)
        pdf_io = io.BytesIO(pdf_bytes)
        pdf_io.seek(0)

        safe_url = url_analisada.replace('https://', '').replace('http://', '').replace('/', '_')[:50]
        filename = f'relatorio_seo_{safe_url}.pdf'

        print(f"[SUCCESS] PDF gerado com sucesso: {filename}")

        return send_file(
            pdf_io,
            mimetype='application/pdf',
            as_attachment=True,
            download_name=filename
        )

    except ImportError as e:
        print(f"[WARNING] Geração de PDF desabilitada (WeasyPrint não instalado): {e}")
        return jsonify({
            'error': 'Geração de PDF temporariamente desabilitada',
            'message': 'Use o botão "Copiar Markdown" para salvar o relatório. A geração de PDF será habilitada em breve.',
            'details': 'WeasyPrint requer dependências de sistema adicionais'
        }), 503

    except Exception as e:
        import traceback
        error_trace = traceback.format_exc()
        print(f"[ERROR] Erro ao gerar PDF: {error_trace}")
        return jsonify({
            'error': f'Erro ao gerar PDF: {str(e)}',
            'details': error_trace if app.debug else None
        }), 500


def preload_dependencies():
    try:
        print("[PRELOAD] Loading google.genai...", flush=True)
        from google import genai  # noqa: F401
        print("[PRELOAD] google.genai loaded successfully", flush=True)

        print("[PRELOAD] Loading web scraper dependencies...", flush=True)
        from web_scraper import scrape_url  # noqa: F401
        from scoring_system import calculate_scores  # noqa: F401
        print("[PRELOAD] All dependencies loaded successfully", flush=True)
    except Exception as e:
        print(f"[PRELOAD WARNING] Could not preload dependencies: {e}", flush=True)


if os.getenv('RENDER') or os.getenv('FLASK_ENV') == 'production':
    print("[STARTUP] Production environment detected - preloading dependencies...", flush=True)
    preload_dependencies()


if __name__ == '__main__':
    if not os.getenv('GOOGLE_API_KEY'):
        print("[WARNING] GOOGLE_API_KEY não encontrada no ambiente!")
        print("[WARNING] Configure no arquivo .env ou como variável de ambiente")
    else:
        print("[INFO] GOOGLE_API_KEY detectada")

    port = int(os.getenv('PORT', DEFAULT_PORT))
    is_production = os.getenv('FLASK_ENV') == 'production' or os.getenv('RENDER') is not None
    debug_mode = not is_production

    print(f"[INFO] Ambiente: {'PRODUÇÃO' if is_production else 'DESENVOLVIMENTO'}")
    print(f"[INFO] Iniciando servidor Flask em http://0.0.0.0:{port}")
    print(f"[INFO] Frontend disponível em: http://localhost:{port}")
    print(f"[INFO] Health check em: http://localhost:{port}/health")
    print(f"[INFO] Modo debug: {'Ativado' if debug_mode else 'Desativado'}")

    app.run(host='0.0.0.0', port=port, debug=debug_mode)
