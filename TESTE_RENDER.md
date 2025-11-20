# 🧪 Como Testar seu App no Render

Depois que o deploy terminar, teste assim:

## 1️⃣ Teste Básico - Health Check

Abra no navegador:
```
https://ai-seo-audit-team.onrender.com/health
```

**Resposta esperada:**
```json
{
  "status": "healthy",
  "service": "AI SEO Audit Team API",
  "version": "1.0.0"
}
```

Se aparecer isso = **Servidor está funcionando!** ✅

---

## 2️⃣ Teste do Frontend

Abra no navegador:
```
https://ai-seo-audit-team.onrender.com
```

Você deve ver:
- Título: "AI SEO Audit Team"
- Campo para digitar URL
- Botão "Analisar Site"

---

## 3️⃣ Teste Completo - Análise de Site

1. Digite uma URL no campo: `https://google.com`
2. Clique em **"Analisar Site"**
3. Aguarde **1-2 minutos** (primeira requisição pode demorar mais)
4. Você deve ver:
   - Loading spinner
   - Depois: Relatório completo em Markdown
   - Scores SEO, CRO, GEO
   - Recomendações detalhadas

---

## 4️⃣ Teste do PDF

1. Depois de gerar um relatório
2. Clique no botão **"Baixar PDF"**
3. Um arquivo PDF deve fazer download
4. Abra o PDF e veja o relatório formatado

---

## ⚠️ Problemas Comuns

### "Application Error"
- **Causa:** Variável `GOOGLE_API_KEY` não configurada
- **Solução:**
  1. Render Dashboard → seu service
  2. Environment → Edit
  3. Adicione: `GOOGLE_API_KEY=AIzaSyDG_G1ThZu9F2fDRCoo_RlN9dZYaobNX24`
  4. Save Changes

### "Timeout" ou muito lento
- **Causa:** Primeira requisição demora (app estava dormindo)
- **Normal no tier gratuito**
- **Solução:** Configure UptimeRobot para manter acordado

### "429 Quota Exceeded"
- **Causa:** Limite de requisições da API Gemini
- **Solução:** Aguarde 1 minuto e tente novamente

---

## 📊 Ver Logs no Render

Para debugar problemas:

1. Render Dashboard
2. Clique no seu service
3. Clique em **"Logs"** na sidebar esquerda
4. Veja logs em tempo real

Procure por:
- `[INFO]` - Informações
- `[ERROR]` - Erros
- `[SUCCESS]` - Sucesso

---

## 🎯 Checklist de Testes

- [ ] `/health` retorna JSON com status healthy
- [ ] Frontend carrega corretamente
- [ ] Consegue digitar URL e clicar em "Analisar"
- [ ] Relatório é gerado (aguardar 1-2 min)
- [ ] Scores aparecem (SEO, CRO, GEO)
- [ ] Botão "Baixar PDF" funciona
- [ ] PDF baixa e abre corretamente

---

**Tudo OK?** Parabéns! Seu app está no ar! 🎉

**Problemas?** Verifique os logs no Render Dashboard.
