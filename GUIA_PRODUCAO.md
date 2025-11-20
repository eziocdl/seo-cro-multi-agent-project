# 🚀 Guia de Produção - AI SEO Audit Team

## 📋 O que foi feito para preparar o projeto para produção

### ✅ Problemas Identificados e Resolvidos

#### 1. **Backend não estava rodando**
**Problema:** O frontend tentava conectar ao backend, mas nenhum servidor estava ativo na porta 8000.

**Solução:**
- Criado script de inicialização automática `start.sh`
- Adicionado verificações de saúde do sistema

---

#### 2. **Endpoint de geração de PDF não existia**
**Problema:** O botão "Baixar PDF" no frontend chamava `/generate-pdf`, mas esse endpoint não estava implementado no `app.py`.

**Solução (`app.py:90-140`):**
```python
@app.route('/generate-pdf', methods=['POST'])
def generate_pdf():
    """Gera PDF do relatório Markdown"""
    # Recebe markdown e URL
    # Usa pdf_generator.py para converter
    # Retorna arquivo PDF para download
```

---

#### 3. **Falta de logs e monitoramento**
**Problema:** Difícil diagnosticar problemas sem logs claros.

**Solução:**
- Adicionado logs estruturados com prefixos `[INFO]`, `[ERROR]`, `[DEBUG]`
- Criado endpoint `/health` para verificar se o servidor está ativo

---

#### 4. **Variáveis de ambiente não carregadas**
**Problema:** `GOOGLE_API_KEY` no arquivo `.env` não era carregada automaticamente.

**Solução (`app.py:8-11`):**
```python
from dotenv import load_dotenv
load_dotenv()  # Carrega variáveis do .env
```

**Dependência adicionada:** `python-dotenv==1.0.0` no `requirements.txt`

---

#### 5. **Falta de validação e tratamento de erros**
**Problema:** Erros genéricos sem informações úteis.

**Solução:**
- Validação de URL antes de processar
- Tratamento específico de timeout (3 minutos)
- Mensagens de erro detalhadas em modo debug
- Verificação de API key na inicialização

---

## 🔧 Arquivos Modificados

### 1. `app.py` (Backend Flask)
**O que mudou:**
- ✅ Importado `python-dotenv` para carregar `.env`
- ✅ Adicionado endpoint `/health` (linha 17-24)
- ✅ Melhorado `/invoke` com logs e validações (linha 31-88)
- ✅ **NOVO:** Implementado `/generate-pdf` (linha 90-140)
- ✅ Adicionado verificação de API key na inicialização (linha 143-148)
- ✅ Logs informativos ao iniciar servidor (linha 150-153)

### 2. `requirements.txt`
**O que mudou:**
- ✅ Adicionado `python-dotenv==1.0.0` (necessário para carregar .env)

### 3. `start.sh` (NOVO)
**Script de inicialização automática que:**
1. Verifica se `venv` existe, se não, cria
2. Ativa o ambiente virtual
3. Instala dependências do `requirements.txt` se necessário
4. Verifica se `.env` existe e está configurado
5. Verifica se porta 8000 está disponível
6. Inicia o servidor Flask

---

## 🚀 Como Usar Agora

### Opção 1: Script Automático (RECOMENDADO)

```bash
# No terminal, dentro da pasta do projeto:
./start.sh
```

**O que acontece:**
- ✅ Cria e ativa o ambiente virtual automaticamente
- ✅ Instala todas as dependências
- ✅ Verifica configurações
- ✅ Inicia o servidor

### Opção 2: Manual

```bash
# 1. Ativar ambiente virtual
source venv/bin/activate

# 2. Instalar dependências (se necessário)
pip install -r requirements.txt

# 3. Verificar se .env está configurado
cat .env  # Deve ter GOOGLE_API_KEY=AIza...

# 4. Iniciar servidor
python app.py
```

---

## 🌐 Endpoints Disponíveis

| Endpoint | Método | Descrição | Status |
|----------|--------|-----------|--------|
| `/` | GET | Frontend (index.html) | ✅ |
| `/health` | GET | Verificação de saúde | ✅ **NOVO** |
| `/invoke` | POST | Executa análise SEO/CRO | ✅ Melhorado |
| `/generate-pdf` | POST | Gera PDF do relatório | ✅ **NOVO** |

### Testar os endpoints:

```bash
# 1. Verificar se servidor está rodando
curl http://localhost:8000/health

# Resposta esperada:
# {"status":"healthy","service":"AI SEO Audit Team API","version":"1.0.0"}

# 2. Testar análise (substitua pela URL real)
curl -X POST http://localhost:8000/invoke \
  -H "Content-Type: application/json" \
  -d '{"message":"https://exemplo.com"}'
```

---

## 🔍 Fluxo Completo Explicado

### Quando você coloca uma URL no frontend:

```
1. [Frontend] Usuário digita URL e clica "Analisar"
   ↓
2. [script.js:63] Faz POST para /invoke com {"message": "https://..."}
   ↓
3. [app.py:31] Backend recebe requisição
   ↓
4. [app.py:48] Executa subprocess:
   python -m google.adk.cli agent run --agent agent:root_agent --user-message <URL>
   ↓
5. [agent.py] Pipeline de 4 agentes é executado:
   - PageAuditorAgent → Auditoria SEO
   - SerpAnalystAgent → Análise SERP
   - CROAnalystAgent → Análise CRO
   - StrategicAdvisorAgent → Relatório final em Markdown
   ↓
6. [app.py:74] Retorna JSON: {"output": "...markdown..."}
   ↓
7. [script.js:81] Frontend renderiza Markdown com marked.js
   ↓
8. [USUÁRIO] Vê relatório completo na tela
   ↓
9. [OPCIONAL] Clica "Baixar PDF"
   ↓
10. [script.js:106] POST para /generate-pdf
    ↓
11. [app.py:104] Usa pdf_generator.py → WeasyPrint
    ↓
12. [app.py:119] Retorna arquivo PDF
    ↓
13. [script.js:128] Browser faz download do PDF
```

---

## 📊 Logs do Sistema

Agora você verá logs claros ao executar:

```bash
[INFO] GOOGLE_API_KEY detectada
[INFO] Iniciando servidor Flask em http://0.0.0.0:8000
[INFO] Frontend disponível em: http://localhost:8000
[INFO] Health check em: http://localhost:8000/health
[INFO] Modo debug: Ativado

# Quando uma análise é feita:
[INFO] Iniciando análise para URL: https://exemplo.com
[DEBUG] Return code: 0
[DEBUG] STDOUT length: 5432
[SUCCESS] Análise concluída com sucesso

# Se houver erro:
[ERROR] Falha na execução: google.adk.cli not found
[WARNING] STDERR: ModuleNotFoundError...
```

---

## ⚠️ Troubleshooting

### Problema 1: "Nenhuma saída gerada pelo agente"
**Causa:** Google ADK não instalado ou GOOGLE_API_KEY inválida

**Solução:**
```bash
# Verificar se google-genai está instalado
pip show google-genai

# Reinstalar se necessário
pip install google-genai==0.2.0

# Verificar API key
echo $GOOGLE_API_KEY  # ou
cat .env | grep GOOGLE_API_KEY
```

### Problema 2: "Porta 8000 já está em uso"
**Solução:** O script `start.sh` mata processos automaticamente, mas manualmente:
```bash
# Encontrar processo
lsof -i :8000

# Matar processo
kill -9 <PID>
```

### Problema 3: "Erro ao gerar PDF"
**Causa:** WeasyPrint precisa de dependências do sistema

**Solução (macOS):**
```bash
brew install cairo pango gdk-pixbuf libffi
```

**Solução (Linux):**
```bash
sudo apt-get install python3-dev python3-pip python3-cffi libcairo2 libpango-1.0-0 libpangocairo-1.0-0 libgdk-pixbuf2.0-0 libffi-dev shared-mime-info
```

### Problema 4: Frontend não se conecta ao backend
**Verificações:**
```bash
# 1. Backend está rodando?
curl http://localhost:8000/health

# 2. Porta correta?
# Frontend usa: API_ENDPOINT = "/invoke" (relativo)
# Isso funciona porque frontend é servido pelo próprio Flask

# 3. CORS configurado?
# Sim, CORS(app) está ativo no app.py linha 14
```

---

## 🎯 Próximos Passos para Produção Completa

### Ainda faltam (opcionais):

1. **Segurança:**
   - [ ] Rotacionar API key exposta
   - [ ] Adicionar rate limiting
   - [ ] Implementar autenticação de usuários
   - [ ] Sanitizar inputs contra injection

2. **Performance:**
   - [ ] Adicionar cache de relatórios
   - [ ] Implementar processamento assíncrono (Celery)
   - [ ] Usar servidor WSGI para produção (Gunicorn)

3. **Funcionalidades:**
   - [ ] Integrar Firecrawl para scraping real
   - [ ] Salvar histórico de relatórios em banco de dados
   - [ ] Exportar para Word/Excel

4. **Deploy:**
   - [ ] Dockerizar aplicação
   - [ ] Configurar CI/CD
   - [ ] Deploy em cloud (AWS, GCP, Heroku)

---

## 📞 Contato

Se tiver dúvidas sobre as modificações, revise:
- `app.py` - Backend principal
- `start.sh` - Script de inicialização
- `GUIA_PRODUCAO.md` - Este arquivo

**Comando para iniciar:** `./start.sh`

**Acesse:** http://localhost:8000
