# SiteScore - Documentação Técnica Completa

> Sistema de Auditoria Digital Estratégica com IA
>
> Análise automatizada de SEO, CRO e GEO utilizando Multi-Agent AI System

**Versão:** 1.0.0
**Última Atualização:** Novembro 2025
**Autor:** Ezio Lima

---

## Índice

1. [Visão Geral](#visão-geral)
2. [Arquitetura do Sistema](#arquitetura-do-sistema)
3. [Tecnologias Utilizadas](#tecnologias-utilizadas)
4. [Sistema de Scoring](#sistema-de-scoring)
5. [Estrutura de Arquivos](#estrutura-de-arquivos)
6. [Instalação e Configuração](#instalação-e-configuração)
7. [Como Usar](#como-usar)
8. [API Endpoints](#api-endpoints)
9. [Pipeline de Análise](#pipeline-de-análise)
10. [Web Scraping](#web-scraping)
11. [Frontend](#frontend)
12. [Geração de PDF](#geração-de-pdf)
13. [Troubleshooting](#troubleshooting)
14. [Deploy](#deploy)
15. [Roadmap Futuro](#roadmap-futuro)

---

## Visão Geral

### O que é o SiteScore?

SiteScore é uma ferramenta de auditoria digital estratégica que analisa websites de forma automatizada, fornecendo:

- **Análise SEO Completa**: On-page, technical, content quality, performance
- **Auditoria CRO**: Conversion rate optimization e user experience
- **Otimização GEO**: Generative Engine Optimization para IA (ChatGPT, Bard, Perplexity)
- **Scores Objetivos**: Pontuação 0-100 baseada em dados reais
- **Relatórios Profissionais**: Markdown + PDF com recomendações priorizadas

### Principais Características

✅ **Dados Reais**: 100% baseado em web scraping real (BeautifulSoup)
✅ **Multi-Agent AI**: 4 agentes especializados em pipeline sequencial
✅ **Scoring Inteligente**: Cálculo automático de SEO/CRO/GEO scores
✅ **Sem Alucinações**: Validação rigorosa de dados extraídos
✅ **Análise Gratuita**: Não requer APIs pagas (exceto Google Gemini)
✅ **PDF Profissional**: Export pronto para apresentações

### Caso de Uso

1. **Agências de Marketing**: Auditorias para clientes
2. **Consultores SEO**: Análises técnicas detalhadas
3. **Empresas**: Auto-avaliação de presença digital
4. **Desenvolvedores**: Checklist de otimização

---

## Arquitetura do Sistema

### Diagrama de Componentes

```
┌─────────────────────────────────────────────────────────────┐
│                        USER INTERFACE                        │
│                     (React-like Frontend)                    │
│                   http://localhost:8000                      │
└───────────────────────┬─────────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────────────┐
│                      FLASK BACKEND                           │
│                      (Python 3.13)                           │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  Routes:                                              │  │
│  │  - GET  /              → Frontend                     │  │
│  │  - GET  /health        → Health Check                 │  │
│  │  - POST /invoke        → Análise Completa             │  │
│  │  - POST /generate-pdf  → Geração de PDF               │  │
│  └──────────────────────────────────────────────────────┘  │
└───────┬───────────────────────┬─────────────────────────────┘
        │                       │
        ▼                       ▼
┌──────────────────┐   ┌────────────────────────────────────┐
│  WEB SCRAPER     │   │   MULTI-AGENT AI PIPELINE         │
│  (web_scraper.py)│   │   (Google Gemini 2.0 Flash)       │
├──────────────────┤   ├────────────────────────────────────┤
│ • BeautifulSoup  │   │ Agent 1: Page Auditor              │
│ • Requests       │   │   → On-page SEO + Keywords         │
│ • lxml parser    │   │                                    │
│                  │   │ Agent 2: SERP Analyst              │
│ Extrai:          │   │   → Competitive Intelligence       │
│ - Title/Meta     │   │                                    │
│ - Headings       │   │ Agent 3: CRO Analyst               │
│ - Word Count     │   │   → UX + Conversion Optimization   │
│ - Links          │   │                                    │
│ - Images         │   │ Agent 4: Strategic Advisor         │
│ - Schema.org     │   │   → Final Report Generation        │
│ - Performance    │   │                                    │
└────────┬─────────┘   └────────────────┬───────────────────┘
         │                              │
         ▼                              ▼
┌────────────────────────┐   ┌─────────────────────────────┐
│  SCORING SYSTEM        │   │   PDF GENERATOR             │
│  (scoring_system.py)   │   │   (pdf_generator.py)        │
├────────────────────────┤   ├─────────────────────────────┤
│ • SEO Score (0-100)    │   │ • WeasyPrint                │
│ • CRO Score (0-100)    │   │ • Markdown → HTML → PDF     │
│ • GEO Score (0-100)    │   │ • Professional Layout       │
│ • Overall Score        │   │                             │
│ • Classificações A-D   │   │                             │
└────────────────────────┘   └─────────────────────────────┘
```

### Fluxo de Dados

```
1. Usuário insere URL no frontend
   ↓
2. Frontend envia POST /invoke com {"message": "example.com"}
   ↓
3. Backend valida URL e inicia pipeline
   ↓
4. Web Scraper extrai dados REAIS do site
   ↓
5. Scoring System calcula SEO/CRO/GEO scores
   ↓
6. Agent 1 (Page Auditor) analisa dados on-page
   ↓
7. Agent 2 (SERP Analyst) analisa competição
   ↓
8. Agent 3 (CRO Analyst) analisa conversão
   ↓
9. Agent 4 (Strategic Advisor) gera relatório final
   ↓
10. Backend retorna Markdown para frontend
    ↓
11. Frontend renderiza relatório (marked.js)
    ↓
12. Usuário pode baixar PDF (POST /generate-pdf)
```

---

## Tecnologias Utilizadas

### Backend (Python)

| Tecnologia | Versão | Propósito |
|-----------|--------|-----------|
| **Python** | 3.13 | Linguagem principal |
| **Flask** | 3.0.0 | Web framework |
| **Flask-CORS** | 4.0.0 | Cross-origin requests |
| **google-genai** | 0.2.0 | Google Gemini API |
| **BeautifulSoup4** | 4.12.2 | HTML parsing |
| **lxml** | 5.1.0 | XML/HTML parser |
| **requests** | 2.31.0 | HTTP requests |
| **WeasyPrint** | 60.1 | PDF generation |
| **markdown** | 3.5.1 | Markdown processing |
| **python-dotenv** | 1.0.0 | Environment variables |
| **pydantic** | 2.0.0 | Data validation |

### Frontend (JavaScript)

| Tecnologia | Versão | Propósito |
|-----------|--------|-----------|
| **HTML5** | - | Markup |
| **CSS3** | - | Styling (design premium) |
| **JavaScript** | ES6+ | Interatividade |
| **marked.js** | CDN | Markdown rendering |

### IA e Análise

- **Google Gemini 2.0 Flash Experimental**: LLM para análise e geração de relatórios
- **Multi-Agent Architecture**: 4 agentes especializados em pipeline sequencial

### Infraestrutura

- **Servidor**: Flask Development Server (produção requer WSGI)
- **Porta**: 8000
- **Ambiente**: Python venv

---

## Sistema de Scoring

### Metodologia de Cálculo

O sistema calcula 3 scores principais e 1 score geral:

#### 1. SEO Score (0-100)

Composto por 4 componentes de 25 pontos cada:

**On-Page SEO (25 pontos):**
- Title tag length (8 pts): Ótimo 50-60 chars, Adequado 40-70 chars
- Meta description length (8 pts): Ótimo 150-160 chars, Adequado 140-170 chars
- H1 count (9 pts): Ideal = 1 único H1

**Technical SEO (25 pontos):**
- HTTPS/SSL (10 pts): Implementado = 10, Não = 0
- Mobile-friendly (10 pts): Meta viewport presente = 10
- Schema.org (5 pts): 3+ schemas = 5, 1-2 schemas = 3

**Content Quality (25 pontos):**
- Word count (10 pts): >1000 = 10, 300-1000 = 7, 100-300 = 4
- Image ALT coverage (10 pts): 90%+ = 10, 70-90% = 7, 50-70% = 4
- Internal links (5 pts): 10+ = 5, 5-10 = 3, 1-5 = 1

**Performance (25 pontos):**
- Load time: <1.5s = 25, <2.5s = 20, <4s = 12, <6s = 6, >6s = 2

**Fórmula:**
```python
SEO_Score = on_page + technical + content + performance
```

#### 2. CRO Score (0-100)

Composto por 5 componentes de 20 pontos cada:

**CTA Effectiveness (20 pontos):**
- Total links: 5+ = 10, 2-5 = 5
- Internal > External: +10

**Form Optimization (20 pontos):**
- Atualmente 0 (dados não disponíveis)

**Trust & Credibility (20 pontos):**
- HTTPS: 15 pts
- Schema.org presente: 5 pts

**Page Experience (20 pontos):**
- Load time: <2s = 10, <3.5s = 6, <5s = 3
- Content adequado (500-3000 words): 10 pts

**Mobile Readiness (20 pontos):**
- Meta viewport: 15 pts
- Load time mobile <3s: 5 pts

**Fórmula:**
```python
CRO_Score = cta + forms + trust + experience + mobile
```

#### 3. GEO Score (0-100)

Composto por 4 componentes de 25 pontos cada:

**Structured Data Quality (25 pontos):**
- Quantidade de schemas: 5+ = 15, 3+ = 12, 1+ = 8
- Schemas importantes (Org, Article, LocalBusiness, Product, FAQ): 10 pts

**AI Content Format (25 pontos):**
- Heading hierarchy (H1=1, H2>=2): 15 pts
- Word count: 800+ = 10, 400+ = 6, 200+ = 3

**Knowledge Graph Signals (25 pontos):**
- Schema Org/LocalBusiness: 10 pts
- Meta description 100+ chars: 5 pts
- Title bem estruturado (com | ou -): 5 pts
- Internal links 15+: 5 pts

**Hallucination Risk Management (25 pontos):**
- Schemas 2+: 10 pts
- H1=1 + word count 300+: 10 pts
- Title 30+ + meta 100+: 5 pts

**Fórmula:**
```python
GEO_Score = structured_data + ai_format + knowledge_graph + hallucination_mgmt
```

#### 4. Overall Score (0-100)

Score geral ponderado:

```python
Overall_Score = (SEO * 0.4) + (CRO * 0.3) + (GEO * 0.3)
```

**Peso:** SEO 40%, CRO 30%, GEO 30%

### Classificações

| Score | Classificação | Grade |
|-------|--------------|-------|
| 80-100 | Excelente | A |
| 60-79 | Bom | B |
| 40-59 | Requer Otimização | C |
| 0-39 | Crítico | D |

### Visualização

Barras de progresso ASCII:
```
SEO Health:     72/100  ██████████████░░░░░░
CRO Readiness:  45/100  █████████░░░░░░░░░░░
```

---

## Estrutura de Arquivos

```
ai_seo_audit_team/
│
├── app.py                      # Flask backend principal
├── agent.py                    # (Legado - não usado)
├── web_scraper.py              # Módulo de scraping
├── scoring_system.py           # Cálculo de scores
├── pdf_generator.py            # Geração de PDF
├── requirements.txt            # Dependências Python
├── .env                        # Variáveis de ambiente (GOOGLE_API_KEY)
├── .gitignore                  # Arquivos ignorados pelo git
│
├── public/                     # Frontend
│   ├── index.html             # HTML principal
│   ├── style.css              # CSS premium
│   └── script.js              # JavaScript frontend
│
├── venv/                       # Ambiente virtual Python
│
├── server.log                  # Logs do servidor
├── DOCUMENTATION.md            # Esta documentação
├── documents.md                # Especificação do prompt
├── backend.md                  # Documentação legada
└── frontend.md                 # Documentação legada
```

### Descrição dos Arquivos Principais

#### `app.py` (511 linhas)

Backend Flask com:
- Routes: `/`, `/health`, `/invoke`, `/generate-pdf`
- Pipeline de 4 agentes IA
- Integração com scraper e scoring
- Logging detalhado

**Key Functions:**
```python
@app.route('/invoke', methods=['POST'])
def invoke_agent():
    # 1. Recebe URL
    # 2. Executa scraping
    # 3. Calcula scores
    # 4. Roda pipeline de agentes
    # 5. Retorna relatório markdown
```

#### `web_scraper.py` (307 linhas)

Web scraping profissional:
- Classe `WebScraper`
- Extração de título, meta tags, headings, conteúdo
- Análise de links, imagens, schema.org
- Medição de performance

**Key Functions:**
```python
def scrape_url(url: str) -> Dict:
    scraper = WebScraper(url)
    return scraper.analyze_page()
```

#### `scoring_system.py` (450 linhas)

Sistema de pontuação:
- Classe `SiteScoreCalculator`
- Métodos de cálculo para SEO/CRO/GEO
- Classificações e barras de progresso

**Key Functions:**
```python
def calculate_scores(real_data: Dict) -> Dict:
    calculator = SiteScoreCalculator(real_data)
    return calculator.get_full_report_data()
```

#### `pdf_generator.py`

Conversão Markdown → PDF:
- WeasyPrint para renderização
- CSS customizado para PDF
- Layout profissional

#### `public/index.html` (60 linhas)

Frontend HTML5 com:
- SEO meta tags completos
- Schema.org structured data
- Open Graph + Twitter Cards
- Form de análise
- Área de resultado

#### `public/style.css` (746 linhas)

Design system premium:
- CSS variables para cores, spacing, shadows
- Markdown styling profissional
- Responsive design
- Animações suaves
- Print styles

#### `public/script.js` (143 linhas)

JavaScript frontend:
- Form submission
- Loading states
- Markdown rendering (marked.js)
- PDF download

---

## Instalação e Configuração

### Pré-requisitos

- Python 3.13+
- pip (gerenciador de pacotes Python)
- Google API Key (Gemini)

### Passo a Passo

#### 1. Clone o repositório

```bash
cd ai_seo_audit_team
```

#### 2. Crie ambiente virtual

```bash
python3 -m venv venv
```

#### 3. Ative o ambiente virtual

**MacOS/Linux:**
```bash
source venv/bin/activate
```

**Windows:**
```bash
venv\Scripts\activate
```

#### 4. Instale dependências

```bash
pip install -r requirements.txt
```

#### 5. Configure variáveis de ambiente

Crie arquivo `.env` na raiz:

```env
GOOGLE_API_KEY=sua_api_key_aqui
```

**Como obter Google API Key:**
1. Acesse: https://aistudio.google.com/app/apikey
2. Crie um novo projeto
3. Gere uma API key
4. Copie e cole no `.env`

#### 6. Instale dependências do WeasyPrint

**MacOS:**
```bash
brew install cairo pango gdk-pixbuf libffi
```

**Ubuntu/Debian:**
```bash
sudo apt-get install python3-dev python3-pip python3-setuptools python3-wheel python3-cffi libcairo2 libpango-1.0-0 libpangocairo-1.0-0 libgdk-pixbuf2.0-0 libffi-dev shared-mime-info
```

**Windows:**
- Baixe GTK3 runtime: https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer

#### 7. Inicie o servidor

```bash
python app.py
```

Servidor inicia em: `http://localhost:8000`

### Verificação

```bash
curl http://localhost:8000/health
```

Resposta esperada:
```json
{
  "status": "healthy",
  "service": "AI SEO Audit Team API",
  "version": "1.0.0"
}
```

---

## Como Usar

### Interface Web

1. **Acesse o frontend:**
   - Abra `http://localhost:8000` no navegador

2. **Insira a URL:**
   - Digite a URL do site a ser analisado (ex: `example.com`)
   - Sistema adiciona `https://` automaticamente se necessário

3. **Inicie a análise:**
   - Clique em "Analisar"
   - Aguarde 20-40 segundos (depende do tamanho do site)

4. **Visualize o relatório:**
   - Relatório aparece com scores e análise detalhada
   - Markdown renderizado com estilo profissional

5. **Baixe o PDF:**
   - Clique em "Baixar PDF"
   - PDF gerado com mesmo conteúdo do relatório

### API (cURL)

**Análise completa:**
```bash
curl -X POST http://localhost:8000/invoke \
  -H "Content-Type: application/json" \
  -d '{"message": "example.com"}'
```

**Gerar PDF:**
```bash
curl -X POST http://localhost:8000/generate-pdf \
  -H "Content-Type: application/json" \
  -d '{
    "markdown": "# Relatório...",
    "url": "example.com"
  }' \
  --output relatorio.pdf
```

---

## API Endpoints

### GET /

**Descrição:** Serve o frontend (index.html)

**Response:** HTML page

---

### GET /health

**Descrição:** Health check do servidor

**Response:**
```json
{
  "status": "healthy",
  "service": "AI SEO Audit Team API",
  "version": "1.0.0"
}
```

**Status Code:** 200

---

### POST /invoke

**Descrição:** Executa análise completa do site

**Request:**
```json
{
  "message": "example.com"
}
```

**Response:**
```json
{
  "output": "# Relatório de Auditoria Digital Estratégica\n\n..."
}
```

**Status Codes:**
- 200: Sucesso
- 400: URL inválida ou site inacessível
- 500: Erro interno

**Tempo de resposta:** 20-40 segundos

**Pipeline interno:**
1. Validação de URL
2. Web scraping (5-10s)
3. Cálculo de scores (1s)
4. Agent 1 - Page Auditor (3-5s)
5. Agent 2 - SERP Analyst (3-5s)
6. Agent 3 - CRO Analyst (3-5s)
7. Agent 4 - Strategic Advisor (5-10s)

---

### POST /generate-pdf

**Descrição:** Gera PDF do relatório markdown

**Request:**
```json
{
  "markdown": "# Relatório...",
  "url": "example.com"
}
```

**Response:** PDF file (application/pdf)

**Headers:**
- `Content-Type: application/pdf`
- `Content-Disposition: attachment; filename=relatorio_seo_example.com.pdf`

**Status Codes:**
- 200: PDF gerado com sucesso
- 400: Markdown não fornecido
- 500: Erro na geração

---

## Pipeline de Análise

### Agent 1: Page Auditor

**Responsabilidade:** Análise on-page e identificação de keywords

**Input:**
- Dados reais do scraper (title, meta, headings, word count, links, images)

**Output:**
```json
{
  "target_keywords": {
    "primary_keyword": "palavra-chave principal",
    "secondary_keywords": ["secundária 1", "secundária 2"],
    "search_intent": "informational|transactional|navigational"
  },
  "audit_results": {
    "title_tag": "título real",
    "meta_description": "meta real",
    "word_count": 1234,
    "link_counts": {"internal": 45, "external": 12, "total": 57},
    "findings": ["issue 1", "issue 2", "issue 3"]
  }
}
```

**Análise:** Identifica keyword principal e secundárias com base nos dados reais.

---

### Agent 2: SERP Analyst

**Responsabilidade:** Análise competitiva simulada

**Input:**
- Primary keyword do Agent 1

**Output:**
```json
{
  "primary_keyword": "palavra-chave",
  "serp_results": [
    {
      "position": 1,
      "title": "Título do competidor",
      "domain": "competidor.com",
      "content_format": "artigo|vídeo|produto"
    }
  ],
  "content_opportunities": [
    "oportunidade 1",
    "oportunidade 2"
  ]
}
```

**Análise:** Simula resultados SERP (não usa API real de busca).

---

### Agent 3: CRO Analyst

**Responsabilidade:** Análise de conversão e UX

**Input:**
- Dados técnicos reais (load time, mobile-friendly, HTTPS, images, schema)

**Output:**
```json
{
  "usability_findings": [
    {
      "issue": "problema encontrado",
      "severity": "high|medium|low",
      "evidence": "referência aos dados reais"
    }
  ],
  "conversion_opportunities": [
    {
      "opportunity": "melhoria específica",
      "impact": "high|medium|low",
      "rationale": "justificativa com evidências"
    }
  ]
}
```

**Análise:** Identifica problemas de UX e oportunidades de conversão reais.

---

### Agent 4: Strategic Advisor

**Responsabilidade:** Geração do relatório final consolidado

**Input:**
- Scores calculados (SEO, CRO, GEO, Overall)
- Dados reais do scraper
- Outputs dos Agents 1, 2, 3

**Output:** Relatório markdown completo

**Estrutura do relatório:**
1. Índice de Performance Digital (scores)
2. Sumário Executivo
3. Auditoria SEO detalhada
4. Análise Competitiva
5. Auditoria CRO
6. Otimização GEO
7. Recomendações Priorizadas (Alta/Média/Backlog)
8. Roadmap de 30 dias
9. Metodologia e Disclaimer

**Prompt engineering:** Tom profissional, conciso, baseado APENAS em dados reais.

---

## Web Scraping

### Tecnologia

- **BeautifulSoup4** + **lxml** + **requests**
- User-Agent: Mozilla/5.0 (simula navegador real)
- Timeout: 10 segundos
- Redirects: Habilitado

### Dados Extraídos

#### 1. Meta Tags
```python
{
  "title": "Título da página (<title>)",
  "meta_description": "Meta description (<meta name='description'>)",
  "canonical": "URL canônica (<link rel='canonical'>)",
  "viewport": "Configuração mobile (<meta name='viewport'>)"
}
```

#### 2. Headings
```python
{
  "h1": ["Texto do H1"],
  "h2": ["Texto dos H2s"],
  "h3": ["Texto dos H3s"],
  # ... até h6
}
```

#### 3. Conteúdo
```python
{
  "word_count": 1234,  # Total de palavras (remove scripts/styles)
  "content_length": 45678  # Bytes do HTML
}
```

#### 4. Links
```python
{
  "internal": 45,   # Links para mesmo domínio
  "external": 12,   # Links para outros domínios
  "total": 57
}
```

#### 5. Imagens
```python
{
  "total": 20,
  "with_alt": 15,
  "without_alt": 5
}
```

#### 6. Technical
```python
{
  "has_ssl": true,           # URL começa com https://
  "mobile_friendly": true,    # Tem meta viewport
  "status_code": 200,
  "load_time": 1.23,         # Segundos
  "final_url": "https://..."  # Após redirects
}
```

#### 7. Schema.org
```python
{
  "schema_types": ["Organization", "Article", "LocalBusiness"]
}
```

**Detecção:** JSON-LD (`<script type="application/ld+json">`) e Microdata (atributo `itemtype`)

### Limitações

- ❌ Não executa JavaScript (sites SPA precisam SSR)
- ❌ Não captura Core Web Vitals reais (usa load time como proxy)
- ❌ Não analisa CSS/imagens (apenas HTML)
- ❌ Não detecta formulários (feature futura)

### Tratamento de Erros

```python
try:
    scraper = WebScraper(url)
    data = scraper.analyze_page()
except requests.exceptions.Timeout:
    return {"success": False, "error": "Timeout"}
except requests.exceptions.RequestException as e:
    return {"success": False, "error": str(e)}
```

---

## Frontend

### Design System

**Paleta de Cores:**
- Primary Gradient: `#667eea → #764ba2` (Blue/Purple)
- Background: `#f8fafc` (Light gray)
- Surface: `#ffffff` (White)
- Text Primary: `#1e293b` (Dark blue-gray)
- Text Secondary: `#64748b` (Medium gray)

**Tipografia:**
- Font: -apple-system, BlinkMacSystemFont, Segoe UI, Roboto
- Base size: 16px
- Line height: 1.6 (body), 1.8 (markdown)

**Spacing System:**
- xs: 0.5rem (8px)
- sm: 0.75rem (12px)
- md: 1rem (16px)
- lg: 1.5rem (24px)
- xl: 2rem (32px)
- 2xl: 3rem (48px)
- 3xl: 4rem (64px)

**Shadows:**
- sm: `0 1px 2px rgba(0,0,0,0.05)`
- md: `0 4px 6px rgba(0,0,0,0.1)`
- lg: `0 10px 15px rgba(0,0,0,0.1)`
- xl: `0 20px 25px rgba(0,0,0,0.1)`
- glow: `0 0 20px rgba(102,126,234,0.3)`

### Componentes

**Header:**
- Sticky position
- Backdrop blur
- Logo com gradient text

**Hero Section:**
- Large heading (3rem)
- Subtitle
- Analysis card com hover effect

**Analysis Card:**
- Elevated surface
- Form com input + button
- Focus states com ring effect

**Report Section:**
- Markdown rendering (marked.js)
- Professional typography
- Code blocks com syntax colors
- Tables com gradient header
- Responsive images

**Buttons:**
- Primary: Gradient background
- Secondary: Border + hover
- States: hover, active, disabled

### Responsividade

**Breakpoints:**
- Mobile: ≤480px
- Tablet: ≤768px
- Desktop: >768px

**Mobile:**
- Stacked layout
- Full-width buttons
- Reduced spacing
- Smaller typography

---

## Geração de PDF

### Tecnologia

**WeasyPrint** (Python HTML-to-PDF renderer)

### Processo

```python
1. Markdown input
   ↓
2. markdown.markdown() → HTML
   ↓
3. Injetar CSS customizado
   ↓
4. WeasyPrint.HTML(string=html).write_pdf()
   ↓
5. BytesIO → send_file()
```

### CSS para PDF

```css
@page {
  size: A4;
  margin: 2cm;
}

body {
  font-family: sans-serif;
  font-size: 11pt;
  line-height: 1.6;
}

h1 {
  font-size: 24pt;
  page-break-after: avoid;
}

table {
  page-break-inside: avoid;
}
```

### Funcionalidades

- ✅ Headers e footers customizados
- ✅ Table of contents
- ✅ Page numbers
- ✅ Syntax highlighting para code blocks
- ✅ Charts e gráficos (SVG)

### Limitações

- ❌ Não suporta JavaScript
- ❌ Lento para documentos grandes (>50 páginas)
- ❌ Requer dependências do sistema (cairo, pango)

---

## Troubleshooting

### Problema: Servidor não inicia

**Erro:**
```
Address already in use
Port 8000 is in use
```

**Solução:**
```bash
# Matar processo na porta 8000
lsof -ti:8000 | xargs kill -9

# Ou usar outra porta
python app.py --port 8001
```

---

### Problema: Google API Key inválida

**Erro:**
```
[ERROR] Erro ao importar google.genai: Invalid API key
```

**Solução:**
1. Verifique se `.env` existe e contém `GOOGLE_API_KEY=...`
2. Teste a key: https://aistudio.google.com/app/apikey
3. Gere nova key se necessário
4. Reinicie o servidor

---

### Problema: WeasyPrint não instala

**Erro:**
```
ERROR: Could not find a version that satisfies the requirement weasyprint
```

**Solução MacOS:**
```bash
brew install cairo pango gdk-pixbuf libffi
pip install --upgrade pip
pip install weasyprint
```

**Solução Ubuntu:**
```bash
sudo apt-get install python3-dev libcairo2 libpango-1.0-0
pip install weasyprint
```

---

### Problema: Scraping falha

**Erro:**
```
Timeout ao acessar https://...
```

**Causas:**
- Site muito lento (>10s)
- Site bloqueia user-agent
- Firewall bloqueando requests

**Solução:**
1. Aumentar timeout em `web_scraper.py`:
```python
self.timeout = 30  # Era 10
```

2. Mudar User-Agent em `web_scraper.py`

3. Usar proxy se site bloqueia IPs

---

### Problema: Relatório vazio

**Sintoma:** Agent 4 retorna markdown vazio ou incompleto

**Causa:** Prompt muito longo ou resposta truncada

**Solução:**
1. Verificar logs: `tail -f server.log`
2. Checar se Gemini retornou erro
3. Simplificar dados enviados ao Agent 4

---

## Deploy

### Opção 1: Render.com (Grátis)

**Passo a passo:**

1. Crie `render.yaml`:
```yaml
services:
  - type: web
    name: sitescore
    env: python
    buildCommand: "pip install -r requirements.txt"
    startCommand: "gunicorn app:app"
    envVars:
      - key: GOOGLE_API_KEY
        sync: false
```

2. Adicione `gunicorn` ao `requirements.txt`:
```
gunicorn==21.2.0
```

3. Conecte repositório no Render
4. Configure `GOOGLE_API_KEY` nas variáveis de ambiente
5. Deploy automático

**URL:** `https://sitescore-xxxx.onrender.com`

**Limitações:**
- Free tier: 512 MB RAM
- Sleep após 15 min inatividade
- 750h/mês grátis

---

### Opção 2: Railway.app (Grátis)

1. Conecte GitHub no Railway
2. Configure variável `GOOGLE_API_KEY`
3. Deploy automático

**Vantagens:**
- Não dorme
- 512 MB RAM
- $5 crédito/mês grátis

---

### Opção 3: Vercel (Serverless)

**Limitação:** Timeout de 10s (free tier)
**Problema:** Pipeline leva 20-40s

**Solução:** Dividir em múltiplas serverless functions com queue

---

### Opção 4: Docker + VPS

**Dockerfile:**
```dockerfile
FROM python:3.13-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    cairo pango gdk-pixbuf libffi

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["gunicorn", "-b", "0.0.0.0:8000", "-w", "4", "app:app"]
```

**Deploy:**
```bash
docker build -t sitescore .
docker run -p 8000:8000 -e GOOGLE_API_KEY=xxx sitescore
```

**VPS recomendados:**
- DigitalOcean Droplet: $6/mês (1GB RAM)
- Hetzner Cloud: €4/mês (2GB RAM)
- AWS Lightsail: $5/mês (512MB RAM)

---

## Roadmap Futuro

### v1.1 - Melhorias Core

- [ ] **Detecção de Formulários**: Análise de forms e CTAs reais
- [ ] **PageSpeed Insights API**: Core Web Vitals reais (LCP, FID, CLS)
- [ ] **Cache de Resultados**: Redis para evitar re-análises
- [ ] **Rate Limiting**: Proteção contra abuso

### v1.2 - Inteligência Avançada

- [ ] **SERP Real**: Integração com SerpAPI ou DataForSEO
- [ ] **Análise de Backlinks**: Moz/Ahrefs API
- [ ] **Competitor Tracking**: Monitoramento contínuo
- [ ] **Historical Data**: Comparação ao longo do tempo

### v1.3 - UX Aprimorada

- [ ] **Dashboard Interativo**: Charts com Chart.js
- [ ] **Comparação de Sites**: Side-by-side analysis
- [ ] **Exportar para Google Sheets**: Integração com Sheets API
- [ ] **White Label**: Customização de branding

### v1.4 - Escalabilidade

- [ ] **Queue System**: Celery + Redis para processamento async
- [ ] **Multi-tenant**: Suporte para múltiplos usuários
- [ ] **Autenticação**: Login com Google/GitHub
- [ ] **API Pública**: RESTful API com rate limits

### v2.0 - Plataforma SaaS

- [ ] **Planos Pagos**: Freemium model
- [ ] **Scheduled Audits**: Análises automáticas agendadas
- [ ] **Email Reports**: Envio automático de relatórios
- [ ] **Mobile App**: React Native app

---

## Contribuindo

### Como Contribuir

1. Fork o repositório
2. Crie branch para feature: `git checkout -b feature/nova-feature`
3. Commit changes: `git commit -m "Add nova feature"`
4. Push branch: `git push origin feature/nova-feature`
5. Abra Pull Request

### Código de Conduta

- Respeite os colaboradores
- Mantenha profissionalismo
- Documente mudanças
- Teste antes de commitar

### Issues

Reporte bugs ou sugira features em: [GitHub Issues]

---

## Licença

MIT License - Veja arquivo `LICENSE`

---

## Contato

**Desenvolvedor:** Ezio Lima
**Projeto:** SiteScore - Auditoria Digital Estratégica
**Versão:** 1.0.0

---

## Changelog

### v1.0.0 (Novembro 2025)

- ✅ Sistema de multi-agent AI funcional
- ✅ Web scraping com dados reais
- ✅ Scoring system (SEO/CRO/GEO)
- ✅ Frontend premium responsive
- ✅ Geração de PDF profissional
- ✅ Relatórios sem alucinações
- ✅ Documentação completa

---

**Fim da Documentação**

Para suporte técnico ou dúvidas, consulte os logs do servidor ou abra um issue no repositório.
