# 🤖 AI SEO Audit Team

> **Sistema Multi-Agente de IA para Análise Profissional de SEO, CRO e GEO**

[![Deploy on Render](https://img.shields.io/badge/Deploy-Render-46E3B7?style=flat&logo=render)](https://render.com)
[![Python 3.11+](https://img.shields.io/badge/Python-3.11+-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![Google Gemini](https://img.shields.io/badge/AI-Google%20Gemini-4285F4?style=flat&logo=google&logoColor=white)](https://ai.google.dev/)
[![Flask](https://img.shields.io/badge/Framework-Flask-000000?style=flat&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Sistema inteligente que utiliza **4 agentes de IA especializados** (Google Gemini 2.5) para realizar análises profundas de websites, fornecendo relatórios estratégicos com scores objetivos e recomendações práticas.

---

## 🎯 Features

### ✨ Análise Multi-Dimensional

- **🔍 SEO Health** - Auditoria completa de otimização para motores de busca
  - On-Page SEO (tags, meta dados, headings)
  - Technical SEO (HTTPS, mobile-friendly, performance)
  - Content Quality (estrutura, palavras-chave, densidade)
  - Core Web Vitals (velocidade, responsividade)

- **📊 CRO Analysis** - Análise de taxa de conversão e usabilidade
  - Efetividade de CTAs
  - Otimização de formulários
  - Confiança e credibilidade
  - Experiência da página
  - Mobile readiness

- **🌐 GEO Optimization** - Preparação para IA Search Engines
  - Structured Data (Schema.org)
  - Compatibilidade com ChatGPT, Bard, Perplexity
  - Otimização de conteúdo para LLMs

### 🚀 Tecnologia de Ponta

- **4 Agentes IA Especializados** trabalhando em pipeline sequencial
- **Web Scraping Real** com BeautifulSoup (dados verificáveis)
- **Sistema de Scoring Objetivo** (0-100) baseado em métricas reais
- **Relatórios em Markdown** profissionais e exportáveis
- **Interface Web Responsiva** com visualização em tempo real

---

## 🏗️ Arquitetura do Sistema

```
┌─────────────────────────────────────────────────────────────────┐
│                        FRONTEND (SPA)                           │
│                   HTML5 + CSS3 + Vanilla JS                     │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             │ HTTP POST /invoke
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│                     FLASK API BACKEND                           │
│                  (Python 3.11 + Gunicorn)                       │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ┌──────────────┐      ┌────────────────┐                      │
│  │ Web Scraper  │─────▶│ Scoring System │                      │
│  │ (Real Data)  │      │  (0-100 Score) │                      │
│  └──────────────┘      └────────────────┘                      │
│         │                       │                               │
│         └───────────┬───────────┘                               │
│                     ▼                                           │
│         ┌───────────────────────┐                               │
│         │   4 AI AGENTS PIPELINE │                              │
│         │  (Google Gemini 2.5)  │                               │
│         └───────────┬───────────┘                               │
│                     │                                           │
│    ┌────────────────┼────────────────┬────────────────┐        │
│    ▼                ▼                ▼                ▼        │
│ ┌──────┐      ┌─────────┐      ┌─────────┐      ┌──────────┐  │
│ │Agent1│      │ Agent 2 │      │ Agent 3 │      │ Agent 4  │  │
│ │Page  │─────▶│  SERP   │─────▶│   CRO   │─────▶│Strategic │  │
│ │Audit │      │Analyst  │      │Analyst  │      │ Advisor  │  │
│ └──────┘      └─────────┘      └─────────┘      └──────────┘  │
│    │              │                 │                 │        │
│    └──────────────┴─────────────────┴─────────────────┘        │
│                           ▼                                     │
│              ┌────────────────────────┐                         │
│              │  MARKDOWN REPORT       │                         │
│              │  (Strategic Analysis)  │                         │
│              └────────────────────────┘                         │
└─────────────────────────────────────────────────────────────────┘
```

### 🔄 Pipeline de Agentes IA

1. **Agent 1: Page Auditor**
   - Analisa elementos on-page (title, meta, headings)
   - Extrai palavras-chave primárias e secundárias
   - Identifica problemas técnicos de SEO

2. **Agent 2: SERP Analyst**
   - Simula análise competitiva da SERP
   - Identifica oportunidades de conteúdo
   - Mapeia estratégias dos concorrentes

3. **Agent 3: CRO Analyst**
   - Avalia usabilidade e experiência do usuário
   - Identifica barreiras de conversão
   - Propõe melhorias de UX/UI

4. **Agent 4: Strategic Advisor**
   - Consolida análises dos 3 agentes anteriores
   - Gera relatório estratégico completo em PT-BR
   - Prioriza recomendações por impacto/esforço

---

## 📊 Sistema de Scoring

### Metodologia de Cálculo

Todos os scores são calculados a partir de **dados reais** extraídos do site:

#### 🔍 SEO Score (0-100)

| Componente | Peso | Critérios |
|------------|------|-----------|
| **On-Page SEO** | 25 pts | Title tag (50-60 chars), Meta description (150-160 chars), H1 único |
| **Technical SEO** | 25 pts | HTTPS, Mobile-friendly, Canonical tags |
| **Content Quality** | 25 pts | Word count (>300), Alt text em imagens, Densidade de keywords |
| **Performance** | 25 pts | Load time (<3s), Structured data, Link quality |

#### 📊 CRO Score (0-100)

| Componente | Peso | Critérios |
|------------|------|-----------|
| **CTA Effectiveness** | 20 pts | Presença, posicionamento, clareza |
| **Form Optimization** | 20 pts | Simplicidade, validação, feedback |
| **Trust & Credibility** | 20 pts | Testimonials, provas sociais, segurança |
| **Page Experience** | 20 pts | Navegação, hierarquia visual, consistência |
| **Mobile Readiness** | 20 pts | Responsividade, touch targets, viewport |

#### 🌐 GEO Score (0-100)

| Componente | Peso | Critérios |
|------------|------|-----------|
| **Structured Data** | 50 pts | Schema.org implementation, tipos relevantes |
| **AI-Friendly Content** | 30 pts | Formatação clara, FAQs, contexto semântico |
| **Metadata Quality** | 20 pts | Open Graph, Twitter Cards, JSON-LD |

### 📈 Classificação dos Scores

```
80-100 → Excelente   ✅ Site otimizado
60-79  → Bom         👍 Melhorias pontuais
40-59  → Regular     ⚠️  Requer otimização
0-39   → Crítico     🚨 Ação urgente necessária
```

---

## 🛠️ Stack Tecnológico

### Backend

- **Python 3.11** - Linguagem principal
- **Flask 3.0** - Framework web
- **Gunicorn 21.2** - WSGI server (produção)
- **Google Gemini 2.5 Flash** - LLM para agentes IA
- **BeautifulSoup 4.12** - Web scraping (parser HTML nativo)
- **Pydantic 2.9** - Validação de schemas estruturados
- **Python-dotenv 1.0** - Gerenciamento de variáveis de ambiente

### Frontend

- **HTML5 + CSS3** - Interface responsiva
- **Vanilla JavaScript** - Lógica do cliente (sem frameworks)
- **Marked.js** - Renderização de Markdown
- **Fetch API** - Comunicação com backend

### DevOps & Deploy

- **Render.com** - Hospedagem (tier gratuito)
- **Git/GitHub** - Controle de versão
- **Gunicorn (gthread worker)** - Otimizado para I/O assíncrono

---

## 📁 Estrutura do Projeto

```
ai_seo_audit_team/
├── 🔧 Core Application
│   ├── app.py                      # Flask API (main)
│   ├── agent.py                    # Pipeline de 4 agentes IA
│   ├── web_scraper.py              # Scraping real de sites
│   ├── scoring_system.py           # Cálculo de scores 0-100
│   ├── schemas.py                  # Pydantic schemas
│   └── __init__.py                 # Package initialization
│
├── 🎨 Frontend
│   └── public/
│       ├── index.html              # Interface principal
│       ├── script.js               # Lógica do cliente
│       └── style.css               # Estilos responsivos
│
├── ⚙️ Configuration
│   ├── requirements.txt            # Dependências Python
│   ├── runtime.txt                 # Versão Python (3.11.0)
│   ├── Procfile                    # Configuração Render/Heroku
│   ├── render.yaml                 # Blueprint Render
│   ├── .env.example                # Template de variáveis
│   └── .gitignore                  # Arquivos ignorados
│
├── 🚀 Deploy Scripts
│   ├── render-build.sh             # Script de build
│   ├── start-server.sh             # Script de inicialização
│   └── start.sh                    # Dev environment setup
│
├── 🧪 Testing
│   ├── test_app_startup.py         # Testes de inicialização
│   └── test_agent.py               # Testes dos agentes
│
└── 📚 Documentation
    ├── README.md                   # Este arquivo
    ├── DOCUMENTATION.md            # Documentação técnica
    ├── DEPLOY.md                   # Guia de deploy
    ├── DEPLOY_RENDER.md            # Deploy no Render (passo-a-passo)
    ├── GUIA_PRODUCAO.md            # Preparação para produção
    └── TESTE_RENDER.md             # Testes pós-deploy
```

**Total:** ~1.890 linhas de código Python | ~28KB de assets frontend

---

## 🚀 Instalação e Uso

### 📋 Pré-requisitos

- Python 3.11 ou superior
- Conta Google AI Studio (para API Key)
- Git

### 🔧 Instalação Local

#### 1. Clone o repositório

```bash
git clone https://github.com/eziocdl/seo-cro-multi-agent-project.git
cd ai_seo_audit_team
```

#### 2. Crie ambiente virtual

```bash
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows
```

#### 3. Instale dependências

```bash
pip install -r requirements.txt
```

#### 4. Configure variáveis de ambiente

```bash
cp .env.example .env
```

Edite `.env` e adicione sua Google API Key:

```env
GOOGLE_API_KEY=AIzaSy...sua_chave_aqui
```

**Obter API Key:** https://aistudio.google.com/app/apikey

#### 5. Inicie o servidor

```bash
# Opção 1: Script automático (recomendado)
./start.sh

# Opção 2: Manual
python app.py
```

#### 6. Acesse a aplicação

Abra no navegador:
```
http://localhost:8000
```

---

## 🌐 Deploy em Produção

### Deploy no Render.com (Gratuito)

**Tempo estimado:** 5 minutos

#### Método Rápido

1. **Fork/Clone** este repositório no GitHub

2. Acesse **[Render.com](https://render.com)** e faça login

3. Clique em **"New +"** → **"Web Service"**

4. Conecte seu repositório GitHub

5. **Configure:**

```yaml
Name: ai-seo-audit-team
Region: Oregon (US West)
Branch: main
Runtime: Python 3

Build Command:
pip install -r requirements.txt

Start Command:
gunicorn app:app --bind 0.0.0.0:$PORT --timeout 180 --workers 1 --threads 2 --worker-class gthread

Instance Type: Free
```

6. **Adicione Environment Variable:**

```
Key: GOOGLE_API_KEY
Value: sua_chave_aqui
```

7. Clique em **"Create Web Service"**

8. Aguarde ~3 minutos

9. ✅ **Pronto!** Sua URL:
```
https://ai-seo-audit-team.onrender.com
```

### Documentação Completa

Para guias detalhados de deploy:
- **[DEPLOY.md](./DEPLOY.md)** - Todas as plataformas (Render, Railway, Fly.io)
- **[DEPLOY_RENDER.md](./DEPLOY_RENDER.md)** - Render.com passo-a-passo
- **[GUIA_PRODUCAO.md](./GUIA_PRODUCAO.md)** - Preparação para produção

---

## 🎮 Como Usar

### Interface Web

1. **Acesse a aplicação** (local ou deploy)
2. **Digite a URL** do site que deseja analisar
3. **Clique em "Analisar Site"**
4. **Aguarde 1-2 minutos** (pipeline de 4 agentes IA processando)
5. **Visualize o relatório completo** com:
   - Scores SEO, CRO, GEO (0-100)
   - Análise detalhada de cada componente
   - Recomendações estratégicas priorizadas
   - Roadmap de implementação (30 dias)

### API REST

#### Endpoint: Health Check

```bash
GET /health

# Resposta
{
  "status": "healthy",
  "service": "AI SEO Audit Team API",
  "version": "1.0.0"
}
```

#### Endpoint: Análise de Site

```bash
POST /invoke
Content-Type: application/json

{
  "message": "https://exemplo.com"
}

# Resposta
{
  "output": "# Relatório de Auditoria Digital Estratégica\n\n..."
}
```

---

## 📊 Exemplo de Relatório

O sistema gera relatórios em Markdown com esta estrutura:

```markdown
# Relatório de Auditoria Digital Estratégica

> Análise realizada em: 20/11/2025 às 13:46:26

**URL Analisada:** https://exemplo.com

---

## Índice de Performance Digital

╔══════════════════════════════════════════════════════╗
║  SCORE GERAL: 78/100 - Bom                          ║
╠══════════════════════════════════════════════════════╣
║  SEO Health:        85/100  ████████▌░              ║
║  CRO Readiness:     72/100  ███████▏░░             ║
║  GEO Optimization:  65/100  ██████▌░░░             ║
╚══════════════════════════════════════════════════════╝

## Sumário Executivo

[Análise consolidada dos 3 pilares]

## 1. Auditoria SEO

### On-Page Elements
- Title Tag: "Exemplo - Título do Site" (21 caracteres)
- Meta Description: ...

### Technical SEO
- HTTPS: ✅ Implementado
- Mobile-Friendly: ✅ Configurado
- Load Time: 2.3s (Bom)

## 2. Análise Competitiva - SERP Intelligence

[Insights sobre concorrentes e oportunidades]

## 3. Auditoria CRO

[Análise de conversão e usabilidade]

## 4. Otimização GEO

[Preparação para IA Search Engines]

## Recomendações Estratégicas Priorizadas

### Prioridade Alta
1. [Recomendação com impacto/esforço]
2. [...]

### Prioridade Média
[...]

## Roadmap de Implementação (30 Dias)

**Semana 1:**
- [ ] Implementar HTTPS
- [ ] Otimizar meta tags

[...]
```

---

## 🧪 Testes

### Testes Automatizados

```bash
# Teste de inicialização
python test_app_startup.py

# Teste dos agentes (se configurado)
python test_agent.py
```

### Teste Manual (Local)

```bash
# 1. Iniciar servidor
python app.py

# 2. Teste de health check
curl http://localhost:8000/health

# 3. Teste de análise
curl -X POST http://localhost:8000/invoke \
  -H "Content-Type: application/json" \
  -d '{"message":"https://google.com"}'
```

---

## ⚙️ Configuração Avançada

### Variáveis de Ambiente

```env
# Obrigatório
GOOGLE_API_KEY=AIzaSy...     # Google AI Studio API Key

# Opcional
FLASK_ENV=production          # production | development
PORT=8000                     # Porta do servidor (default: 8000)
```

### Customização de Agentes

Edite `agent.py` para ajustar:
- Instruções dos agentes
- Modelo do Gemini (gemini-2.5-flash, gemini-pro, etc)
- Schemas de saída (Pydantic)

### Customização de Scoring

Edite `scoring_system.py` para ajustar:
- Pesos de cada componente
- Critérios de pontuação
- Limites de classificação

---

## 🐛 Troubleshooting

### Problema: "GOOGLE_API_KEY não encontrada"

**Solução:**
```bash
# Verifique se o .env existe
cat .env

# Configure a variável
echo "GOOGLE_API_KEY=sua_chave" >> .env
```

### Problema: "Bad Gateway" no Render

**Solução:**
```bash
# No Render Dashboard → Settings → Start Command
# Cole exatamente:
gunicorn app:app --bind 0.0.0.0:$PORT --timeout 180 --workers 1 --threads 2 --worker-class gthread
```

### Problema: "429 Quota Exceeded"

**Causa:** Limite de requisições gratuitas do Gemini (15 req/min)

**Solução:** Aguarde 1 minuto ou faça upgrade da API key

### Mais problemas?

Consulte:
- [DEPLOY.md](./DEPLOY.md) - Troubleshooting de deploy
- [Issues do GitHub](https://github.com/eziocdl/seo-cro-multi-agent-project/issues)

---

## 🗺️ Roadmap

### ✅ Versão 1.0 (Atual)

- [x] Pipeline de 4 agentes IA
- [x] Web scraping real com BeautifulSoup
- [x] Sistema de scoring objetivo (0-100)
- [x] Relatórios em Markdown
- [x] Interface web responsiva
- [x] Deploy gratuito no Render

### 🚧 Versão 1.1 (Próxima)

- [ ] Geração de PDF profissional
- [ ] Integração com Google Search Console
- [ ] Análise de backlinks
- [ ] Comparação histórica de scores
- [ ] Cache de relatórios

### 🔮 Versão 2.0 (Futuro)

- [ ] Dashboard multi-site
- [ ] Autenticação de usuários
- [ ] API pública com rate limiting
- [ ] Exportação para Word/Excel
- [ ] Integração com ferramentas SEO (Ahrefs, SEMrush)
- [ ] Análise de Core Web Vitals real (não simulado)

---

## 🤝 Contribuindo

Contribuições são bem-vindas! Veja como contribuir:

### 1. Fork o projeto

### 2. Crie uma branch para sua feature

```bash
git checkout -b feature/nova-funcionalidade
```

### 3. Commit suas mudanças

```bash
git commit -m 'feat: adiciona nova funcionalidade X'
```

### 4. Push para a branch

```bash
git push origin feature/nova-funcionalidade
```

### 5. Abra um Pull Request

### Padrões de Código

- **Python:** PEP 8
- **Commits:** Conventional Commits
- **Docstrings:** Google Style

---

## 📄 Licença

Este projeto está licenciado sob a **MIT License** - veja o arquivo [LICENSE](LICENSE) para detalhes.

```
MIT License

Copyright (c) 2025 Ezio Lima

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction...
```

---

## 👤 Autor

**Ezio Lima**

- GitHub: [@eziocdl](https://github.com/eziocdl)
- LinkedIn: [Ezio Lima](https://www.linkedin.com/in/ezio-lima)
- Email: contato@eziolima.com

---

## 🙏 Agradecimentos

- **Google AI** - Gemini 2.5 Flash API
- **Render.com** - Hospedagem gratuita
- **Flask Community** - Framework web
- **BeautifulSoup** - Web scraping
- **Comunidade Open Source** - Inspiração e ferramentas

---

## 📞 Suporte

### Documentação

- 📖 [Documentação Técnica](./DOCUMENTATION.md)
- 🚀 [Guia de Deploy](./DEPLOY.md)
- 🔧 [Guia de Produção](./GUIA_PRODUCAO.md)

### Comunidade

- 💬 [GitHub Discussions](https://github.com/eziocdl/seo-cro-multi-agent-project/discussions)
- 🐛 [Report Issues](https://github.com/eziocdl/seo-cro-multi-agent-project/issues)

### Links Úteis

- 🔗 **Demo Live:** https://ai-seo-audit-team.onrender.com
- 📚 **Google AI Studio:** https://aistudio.google.com
- 🎨 **Render Dashboard:** https://dashboard.render.com

---

<div align="center">

**⭐ Se este projeto foi útil, considere dar uma estrela no GitHub! ⭐**

Feito com ❤️ e ☕ usando **Google Gemini 2.5 Flash**

[⬆ Voltar ao topo](#-ai-seo-audit-team)

</div>
