# 🚀 Guia de Deploy Gratuito - AI SEO Audit Team

Este guia mostra como hospedar sua aplicação **gratuitamente** em diferentes plataformas.

## 📊 Comparação de Plataformas Gratuitas

| Plataforma | Tier Gratuito | Domínio | Tempo de Build | Recomendado |
|-----------|---------------|---------|----------------|-------------|
| **Render** | 750h/mês | `.onrender.com` | ~3-5 min | ⭐⭐⭐⭐⭐ |
| **Railway** | $5 créditos/mês | `.railway.app` | ~2-4 min | ⭐⭐⭐⭐ |
| **Fly.io** | 3 VMs gratuitas | `.fly.dev` | ~4-6 min | ⭐⭐⭐⭐ |
| **PythonAnywhere** | Limitado | `.pythonanywhere.com` | Manual | ⭐⭐⭐ |

---

## 🥇 OPÇÃO 1: Render (RECOMENDADO)

### Por que Render?
- ✅ **750 horas/mês grátis** (suficiente para 1 app 24/7)
- ✅ Deploy automático via Git
- ✅ SSL grátis
- ✅ Fácil configuração de variáveis de ambiente
- ✅ Sem cartão de crédito necessário
- ⚠️ Dorme após 15min de inatividade (primeira requisição demora ~30s)

### Passo a Passo

#### 1. Preparar o Código

Seu projeto já está pronto! Os seguintes arquivos foram criados:
- `render.yaml` - Configuração do Render
- `Procfile` - Comando de start
- `runtime.txt` - Versão do Python
- `.dockerignore` - Otimização de build

#### 2. Criar Conta no Render

1. Acesse: https://render.com
2. Clique em **"Get Started"**
3. Faça login com GitHub/GitLab (recomendado) ou email

#### 3. Fazer Push do Código para GitHub

```bash
# No diretório do projeto:
git init
git add .
git commit -m "Preparar para deploy no Render"

# Criar repositório no GitHub e fazer push
git remote add origin https://github.com/seu-usuario/ai-seo-audit-team.git
git branch -M main
git push -u origin main
```

#### 4. Criar Web Service no Render

1. No dashboard do Render, clique **"New +"** → **"Web Service"**
2. Conecte seu repositório GitHub
3. Configure:
   - **Name:** `ai-seo-audit-team` (ou outro nome)
   - **Region:** Oregon (US West)
   - **Branch:** `main`
   - **Runtime:** Python 3
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app --bind 0.0.0.0:$PORT`

4. **Adicionar Variável de Ambiente:**
   - Clique em **"Advanced"** → **"Add Environment Variable"**
   - Key: `GOOGLE_API_KEY`
   - Value: `sua_chave_google_genai_aqui`

5. Clique em **"Create Web Service"**

#### 5. Aguardar Deploy

O Render vai:
1. Clonar seu repositório
2. Instalar dependências (~3-5 min)
3. Iniciar a aplicação
4. Gerar URL pública: `https://ai-seo-audit-team.onrender.com`

#### 6. Testar

```bash
# Verificar se está online
curl https://ai-seo-audit-team.onrender.com/health

# Deve retornar:
# {"status":"healthy","service":"AI SEO Audit Team API","version":"1.0.0"}
```

#### 7. Configurar Auto-Deploy (Opcional)

No Render, vá em **Settings** → **Build & Deploy**:
- Ative **"Auto-Deploy"** = YES
- Agora todo push para `main` fará deploy automático

---

## 🥈 OPÇÃO 2: Railway.app

### Vantagens
- ✅ $5 de créditos grátis/mês
- ✅ Build mais rápido que Render
- ✅ Não dorme (sempre ativo)
- ⚠️ Requer cartão de crédito (mas não cobra além dos $5)

### Passo a Passo

1. **Criar conta:** https://railway.app
2. **Novo Projeto:**
   - Clique **"New Project"** → **"Deploy from GitHub repo"**
   - Selecione seu repositório
3. **Configurar Variáveis:**
   - Vá em **"Variables"**
   - Adicione: `GOOGLE_API_KEY=sua_chave`
4. **Deploy automático:**
   - Railway detecta o `Procfile` e faz deploy automaticamente
5. **Obter URL:**
   - Clique em **"Settings"** → **"Generate Domain"**
   - URL: `https://seu-app.up.railway.app`

---

## 🥉 OPÇÃO 3: Fly.io

### Vantagens
- ✅ 3 VMs compartilhadas grátis
- ✅ 160GB de tráfego grátis/mês
- ✅ Boa performance global
- ⚠️ Requer Dockerfile

### Passo a Passo

1. **Instalar CLI:**
```bash
curl -L https://fly.io/install.sh | sh
```

2. **Login:**
```bash
fly auth login
```

3. **Criar Dockerfile:**
```dockerfile
FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8080

CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:8080", "--timeout", "180"]
```

4. **Fazer Deploy:**
```bash
fly launch
# Responda as perguntas:
# - App name: ai-seo-audit-team
# - Region: São Paulo (gru) ou Miami (mia)
# - PostgreSQL? NO
# - Redis? NO

fly secrets set GOOGLE_API_KEY=sua_chave_aqui
fly deploy
```

5. **Acessar:**
```bash
fly open
# URL: https://ai-seo-audit-team.fly.dev
```

---

## 🔧 OPÇÃO 4: PythonAnywhere

### Limitações
- ⚠️ Tier gratuito tem limitações de CPU
- ⚠️ Não permite requisições externas no tier gratuito (problema para web scraping)
- ⚠️ Configuração manual

**NÃO RECOMENDADO** para este projeto devido às limitações de requisições HTTP.

---

## 🎯 Configuração de Produção

### Variáveis de Ambiente Necessárias

```bash
# Obrigatório
GOOGLE_API_KEY=AIzaSy...  # Obtenha em: https://aistudio.google.com/app/apikey

# Opcional
FLASK_ENV=production
PORT=8000  # Render/Railway definem automaticamente
```

### Como Obter GOOGLE_API_KEY

1. Acesse: https://aistudio.google.com/app/apikey
2. Faça login com sua conta Google
3. Clique em **"Create API Key"**
4. Copie a chave (começa com `AIza...`)
5. Cole nas variáveis de ambiente da plataforma escolhida

---

## ⚡ Melhorias para Produção

### 1. Evitar Sleep do Render (Free Tier)

Use um serviço de "ping" gratuito:

**UptimeRobot** (https://uptimerobot.com):
1. Criar monitor HTTP
2. URL: `https://seu-app.onrender.com/health`
3. Intervalo: 5 minutos
4. Isso mantém seu app acordado

### 2. Domínio Personalizado

**Opções gratuitas:**
- Render/Railway/Fly permitem domínio customizado gratuito
- Use Cloudflare para DNS gratuito + SSL

Exemplo:
```
seoreport.seudominio.com.br → Render
```

### 3. Monitoramento

Adicione ao seu código (já está):
```python
@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'healthy'})
```

Use serviços gratuitos:
- **UptimeRobot:** Monitoramento de uptime
- **Better Uptime:** Alertas por email
- **Cronitor:** Monitoramento de cron jobs

---

## 🐛 Troubleshooting

### Erro: "Application failed to start"

**Causa:** Dependências não instaladas ou Python incompatível

**Solução:**
```bash
# Verificar logs no Render/Railway
# Garantir que runtime.txt tem: python-3.13.0
# Verificar se requirements.txt está correto
```

### Erro: "Timeout aguardando resposta"

**Causa:** Agentes de IA demoram para processar (pode levar 2-3 min)

**Solução:**
- No Render: aumentar timeout em Settings → Health & Alerts
- No Railway: já configurado no Procfile (180s)
- No Fly.io: adicionar `grace_period = "180s"` no fly.toml

### Erro: "GOOGLE_API_KEY not found"

**Causa:** Variável de ambiente não configurada

**Solução:**
1. Render: Settings → Environment → Add Environment Variable
2. Railway: Variables tab
3. Fly.io: `fly secrets set GOOGLE_API_KEY=...`

### Site muito lento na primeira requisição (Render)

**Causa:** Tier gratuito dorme após 15min de inatividade

**Solução:**
- Use UptimeRobot para pingar a cada 5min
- Ou upgrade para plano pago ($7/mês) que nunca dorme

---

## 📊 Custos Estimados (após tier gratuito)

| Plataforma | Custo Mensal | Vantagens |
|-----------|--------------|-----------|
| **Render** | $7/mês (Starter) | Nunca dorme, 400GB tráfego |
| **Railway** | $5/mês + uso | Pay-as-you-go |
| **Fly.io** | ~$3-5/mês | Ótima performance global |

---

## ✅ Checklist de Deploy

Antes de fazer deploy, verifique:

- [ ] `requirements.txt` tem todas as dependências
- [ ] `Procfile` existe e está correto
- [ ] `.env.example` criado (não commitar `.env` real!)
- [ ] `.gitignore` inclui `.env`, `venv/`, `__pycache__/`
- [ ] `GOOGLE_API_KEY` obtida e testada localmente
- [ ] Código funcionando em `http://localhost:8000`
- [ ] Endpoint `/health` retorna status healthy
- [ ] Testar análise de 1 site para confirmar que funciona

---

## 🎬 Tutorial em Vídeo (Render)

1. **Fazer push para GitHub**
2. **Render:** New Web Service
3. **Conectar repositório**
4. **Adicionar GOOGLE_API_KEY**
5. **Deploy!**

**Tempo total:** ~5 minutos

---

## 🔗 Links Úteis

- **Render Dashboard:** https://dashboard.render.com
- **Railway Dashboard:** https://railway.app/dashboard
- **Fly.io Dashboard:** https://fly.io/dashboard
- **Google AI Studio (API Key):** https://aistudio.google.com/app/apikey
- **UptimeRobot (Keep-alive):** https://uptimerobot.com

---

## 🆘 Precisa de Ajuda?

Problemas durante o deploy? Verifique:

1. **Logs da plataforma** (Render/Railway/Fly)
2. **Status das dependências:**
   ```bash
   pip install -r requirements.txt
   python app.py  # Testa localmente
   ```
3. **Variáveis de ambiente:** Confirmou que `GOOGLE_API_KEY` está configurada?

---

**Recomendação Final:** Use **Render** para começar (100% gratuito, sem cartão). Se precisar de mais performance, migre para **Railway** ou **Fly.io**.

**URL esperada após deploy:**
```
https://ai-seo-audit-team.onrender.com
```

Boa sorte! 🚀
