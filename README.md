# 🤖 AI SEO Audit Team

Sistema multi-agente de IA para análise profissional de SEO, CRO e GEO de websites.

## 🚀 Deploy Rápido (Gratuito)

### Opção 1: Render.com (Recomendado)

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy)

1. Crie conta em https://render.com
2. Conecte seu repositório GitHub
3. Configure `GOOGLE_API_KEY` nas variáveis de ambiente
4. Deploy automático!

**Tempo:** ~5 minutos
**Custo:** Grátis (750h/mês)
**URL:** `https://seu-app.onrender.com`

### Opção 2: Railway.app

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/new)

1. Faça login em https://railway.app
2. Deploy do GitHub repo
3. Adicione `GOOGLE_API_KEY`
4. Pronto!

**Tempo:** ~3 minutos
**Custo:** $5 créditos grátis/mês

### Opção 3: Fly.io

```bash
fly launch
fly secrets set GOOGLE_API_KEY=sua_chave
fly deploy
```

---

## 📖 Documentação Completa

- **[DEPLOY.md](./DEPLOY.md)** - Guia completo de hospedagem gratuita
- **[GUIA_PRODUCAO.md](./GUIA_PRODUCAO.md)** - Preparação para produção
- **[DOCUMENTATION.md](./DOCUMENTATION.md)** - Documentação técnica

---

## 🛠️ Desenvolvimento Local

### Requisitos

- Python 3.13+
- Google GenAI API Key ([obter aqui](https://aistudio.google.com/app/apikey))

### Instalação Rápida

```bash
# 1. Clonar repositório
git clone https://github.com/seu-usuario/ai-seo-audit-team.git
cd ai-seo-audit-team

# 2. Criar ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows

# 3. Instalar dependências
pip install -r requirements.txt

# 4. Configurar variáveis de ambiente
cp .env.example .env
# Edite .env e adicione sua GOOGLE_API_KEY

# 5. Iniciar servidor
python app.py
```

Acesse: http://localhost:8000

### Script de Inicialização Automática

```bash
chmod +x start.sh
./start.sh
```

---

## 🎯 Funcionalidades

- ✅ **Análise SEO Completa** - Title, meta tags, headings, links, images
- ✅ **Análise CRO** - Usabilidade, conversão, mobile-friendly
- ✅ **Análise GEO** - Structured data, preparação para IA search
- ✅ **Web Scraping Real** - BeautifulSoup + Requests
- ✅ **Sistema de Scoring** - 0-100 para SEO, CRO e GEO
- ✅ **Relatórios PDF** - Exportação profissional
- ✅ **Multi-Agente IA** - 4 agentes especializados (Google Gemini)

---

## 📊 Arquitetura

```
┌─────────────┐      ┌──────────────┐      ┌─────────────────┐
│  Frontend   │─────▶│   Flask API  │─────▶│  Google Gemini  │
│ HTML/CSS/JS │      │   (Backend)  │      │   (4 Agentes)   │
└─────────────┘      └──────────────┘      └─────────────────┘
                            │
                            ▼
                     ┌──────────────┐
                     │ Web Scraper  │
                     │ (Real Data)  │
                     └──────────────┘
```

### Agentes de IA

1. **Page Auditor** - Análise técnica SEO
2. **SERP Analyst** - Análise competitiva
3. **CRO Analyst** - Otimização de conversão
4. **Strategic Advisor** - Relatório estratégico final

---

## 🔧 API Endpoints

| Endpoint | Método | Descrição |
|----------|--------|-----------|
| `/` | GET | Frontend |
| `/health` | GET | Health check |
| `/invoke` | POST | Análise de website |
| `/generate-pdf` | POST | Gerar PDF do relatório |

### Exemplo de Uso

```bash
# Health check
curl http://localhost:8000/health

# Análise de site
curl -X POST http://localhost:8000/invoke \
  -H "Content-Type: application/json" \
  -d '{"message":"https://exemplo.com"}'
```

---

## 🌐 Variáveis de Ambiente

```bash
# Obrigatório
GOOGLE_API_KEY=AIzaSy...  # Google AI Studio API Key

# Opcional
FLASK_ENV=production  # production ou development
PORT=8000  # Porta do servidor (padrão: 8000)
```

---

## 📦 Dependências Principais

- **Flask 3.0.0** - Framework web
- **google-genai 0.2.0** - Google Gemini API
- **BeautifulSoup4 4.12.2** - Web scraping
- **WeasyPrint 60.1** - Geração de PDF
- **Gunicorn 21.2.0** - WSGI server (produção)

---

## 🧪 Testes

```bash
# Testar localmente
python app.py

# Abrir em http://localhost:8000
# Inserir URL de teste: https://exemplo.com
```

---

## 🚀 Deploy em Produção

Ver [DEPLOY.md](./DEPLOY.md) para instruções completas.

**Resumo rápido para Render:**

1. Push código para GitHub
2. Criar Web Service no Render
3. Conectar repositório
4. Adicionar `GOOGLE_API_KEY`
5. Deploy!

---

## 📝 Licença

MIT License - Veja [LICENSE](./LICENSE) para detalhes

---

## 🤝 Contribuindo

Contribuições são bem-vindas! Por favor:

1. Fork o projeto
2. Crie uma branch (`git checkout -b feature/nova-funcionalidade`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova funcionalidade'`)
4. Push para a branch (`git push origin feature/nova-funcionalidade`)
5. Abra um Pull Request

---

## 📞 Suporte

- **Documentação:** [DEPLOY.md](./DEPLOY.md)
- **Issues:** [GitHub Issues](https://github.com/seu-usuario/ai-seo-audit-team/issues)

---

## ⭐ Features Futuras

- [ ] Integração com Google Search Console
- [ ] Análise de backlinks
- [ ] Comparação histórica de scores
- [ ] Dashboard com múltiplos sites
- [ ] Exportação para Word/Excel
- [ ] Autenticação de usuários
- [ ] API pública com rate limiting

---

**Desenvolvido com ❤️ usando Google Gemini 2.0**
