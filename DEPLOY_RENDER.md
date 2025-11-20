# 🚀 Deploy no Render - Passo a Passo

## ✅ Pré-requisitos

- [x] Conta no GitHub
- [x] Google API Key (https://aistudio.google.com/app/apikey)
- [x] Projeto preparado (já está!)

---

## 📝 PASSO 1: Fazer Push do Código para GitHub

### Se você ainda não tem um repositório GitHub:

```bash
# No terminal, dentro da pasta do projeto:
cd /Users/eziolima/seo-multi-agent-project/ai_seo_audit_team

# 1. Inicializar git (se ainda não foi feito)
git init

# 2. Adicionar todos os arquivos
git add .

# 3. Fazer commit
git commit -m "Projeto pronto para deploy no Render"

# 4. Criar repositório no GitHub
# Vá em: https://github.com/new
# Nome: ai-seo-audit-team
# Público ou Privado (tanto faz)
# NÃO inicialize com README, .gitignore ou licença

# 5. Adicionar remote e fazer push
git remote add origin https://github.com/SEU-USUARIO/ai-seo-audit-team.git
git branch -M main
git push -u origin main
```

### Se você já tem o repositório:

```bash
cd /Users/eziolima/seo-multi-agent-project/ai_seo_audit_team

git add .
git commit -m "Preparar projeto para deploy no Render"
git push origin main
```

---

## 🌐 PASSO 2: Criar Conta no Render

1. Acesse: **https://render.com**
2. Clique em **"Get Started for Free"**
3. Faça login com **GitHub** (recomendado - mais fácil)
4. Autorize o Render a acessar seus repositórios

---

## 🚀 PASSO 3: Criar Web Service

### 3.1. No Dashboard do Render:

1. Clique no botão **"New +"** (canto superior direito)
2. Selecione **"Web Service"**

### 3.2. Conectar Repositório:

1. Encontre o repositório **"ai-seo-audit-team"** na lista
2. Clique em **"Connect"**

### 3.3. Configurar o Service:

Preencha os campos:

**Configurações Básicas:**
```
Name: ai-seo-audit-team
Region: Oregon (US West) - ou escolha a mais próxima
Branch: main
Runtime: Python 3
```

**Build & Deploy:**
```
Build Command: pip install -r requirements.txt
Start Command: gunicorn app:app --bind 0.0.0.0:$PORT --timeout 180
```

**Instance Type:**
```
Free (deixe selecionado)
```

### 3.4. Adicionar Variáveis de Ambiente:

1. Role para baixo até **"Environment Variables"**
2. Clique em **"Add Environment Variable"**
3. Adicione:

```
Key: GOOGLE_API_KEY
Value: sua_chave_google_genai_aqui
```

**Como obter a chave:**
- Acesse: https://aistudio.google.com/app/apikey
- Faça login com sua conta Google
- Clique em **"Create API Key"**
- Copie a chave (começa com AIza...)

### 3.5. Advanced Settings (Opcional):

Role até **"Advanced"** e configure:

```
Auto-Deploy: Yes (recomendado - deploy automático ao fazer push)
Health Check Path: /health
```

### 3.6. Criar o Service:

Clique no botão **"Create Web Service"** no final da página

---

## ⏳ PASSO 4: Aguardar o Deploy

O Render vai:

1. ✅ Clonar seu repositório do GitHub
2. ✅ Detectar que é um projeto Python
3. ✅ Instalar dependências do `requirements.txt` (~3-5 minutos)
4. ✅ Iniciar o servidor com Gunicorn
5. ✅ Gerar URL pública

**Tempo estimado:** 3-5 minutos

Você verá logs em tempo real:

```
==> Cloning from https://github.com/seu-usuario/ai-seo-audit-team...
==> Running build command: pip install -r requirements.txt
==> Successfully installed flask-3.0.0 google-genai-0.2.0 ...
==> Starting server...
==> Your service is live at https://ai-seo-audit-team.onrender.com
```

---

## ✅ PASSO 5: Testar a Aplicação

### 5.1. Obter a URL

No dashboard do Render, você verá:
```
https://ai-seo-audit-team.onrender.com
```

### 5.2. Testar Health Check

```bash
curl https://ai-seo-audit-team.onrender.com/health
```

Resposta esperada:
```json
{
  "status": "healthy",
  "service": "AI SEO Audit Team API",
  "version": "1.0.0"
}
```

### 5.3. Testar no Navegador

1. Abra: `https://ai-seo-audit-team.onrender.com`
2. Digite uma URL para análise (ex: `https://exemplo.com`)
3. Clique em **"Analisar Site"**
4. Aguarde o relatório (pode levar 1-2 minutos)

---

## 🎯 PASSO 6: Configurações Pós-Deploy

### 6.1. Configurar Domínio Customizado (Opcional)

1. No Render, vá em **Settings** → **Custom Domain**
2. Adicione seu domínio (ex: `seoreport.seusite.com`)
3. Configure DNS:
   - CNAME: `ai-seo-audit-team.onrender.com`
4. SSL automático será configurado

### 6.2. Evitar que o App Durma (Importante!)

O tier gratuito do Render coloca o app para "dormir" após 15 minutos de inatividade.
A primeira requisição após dormir demora ~30 segundos.

**Solução: Use UptimeRobot (Gratuito)**

1. Acesse: https://uptimerobot.com
2. Crie conta gratuita
3. Adicione um monitor:
   - Type: **HTTP(s)**
   - URL: `https://ai-seo-audit-team.onrender.com/health`
   - Monitoring Interval: **5 minutes**
4. Isso fará um "ping" a cada 5 minutos, mantendo o app acordado

### 6.3. Ver Logs

No Render dashboard:
1. Clique em **"Logs"** na sidebar
2. Veja logs em tempo real
3. Útil para debugar problemas

---

## 🔧 Troubleshooting

### Problema: "Deploy Failed"

**Solução:**
1. Verifique os logs no Render
2. Erro comum: `requirements.txt` com dependências erradas
   ```bash
   # Localmente, teste:
   pip install -r requirements.txt
   ```

### Problema: "Application Error" ao acessar

**Causa:** Variável `GOOGLE_API_KEY` não configurada

**Solução:**
1. Render Dashboard → Environment → Add Secret File
2. Adicione `GOOGLE_API_KEY=sua_chave`
3. Clique em **"Save Changes"**
4. Render fará redeploy automático

### Problema: "Timeout" durante análise

**Causa:** Agentes de IA demoram para processar

**Solução:** Já configurado no `Procfile`:
```
--timeout 180
```

Se persistir, aumente para 300:
1. Render → Settings → Start Command
2. Altere para: `gunicorn app:app --bind 0.0.0.0:$PORT --timeout 300`

### Problema: App muito lento na primeira requisição

**Causa:** App estava "dormindo" (tier gratuito)

**Solução:** Configure UptimeRobot (ver Passo 6.2)

---

## 📊 Monitoramento

### Métricas Disponíveis no Render Free:

- ✅ CPU Usage
- ✅ Memory Usage
- ✅ Request Count
- ✅ Response Times
- ✅ Logs em tempo real

Acesse: Dashboard → Metrics

---

## 🔄 Atualizações Futuras

### Deploy Automático (já configurado se ativou Auto-Deploy):

```bash
# Faça mudanças no código
git add .
git commit -m "Atualização X"
git push origin main

# Render detecta o push e faz deploy automático!
```

### Deploy Manual (se Auto-Deploy estiver desativado):

1. Render Dashboard → **Manual Deploy** → **Deploy latest commit**

---

## 💰 Limites do Tier Gratuito

| Recurso | Limite |
|---------|--------|
| Horas/mês | 750h (suficiente para 1 app 24/7) |
| Memória | 512 MB |
| Build Time | 90 segundos de CPU |
| Bandwidth | Sem limite |
| Custom Domain | Sim (grátis) |
| SSL | Sim (automático) |
| Sleep após | 15 min inatividade |

---

## 🎉 Pronto!

Seu app está no ar em:
```
https://ai-seo-audit-team.onrender.com
```

### Próximos passos:

1. ✅ Testar análise de diferentes sites
2. ✅ Configurar UptimeRobot para manter acordado
3. ✅ Compartilhar o link com usuários
4. ✅ Monitorar logs no Render Dashboard

---

## 📞 Ajuda Adicional

- **Render Docs:** https://render.com/docs
- **Status Page:** https://status.render.com
- **Community:** https://community.render.com

---

## ✅ Checklist Final

- [ ] Código no GitHub
- [ ] Conta no Render criada
- [ ] Web Service criado e conectado ao repo
- [ ] `GOOGLE_API_KEY` configurada
- [ ] Deploy completo (status: Live)
- [ ] Testado `/health` endpoint
- [ ] Testado análise de 1 site
- [ ] UptimeRobot configurado (opcional mas recomendado)
- [ ] URL compartilhada

**URL Final:** `https://ai-seo-audit-team.onrender.com`

Parabéns! 🎉
