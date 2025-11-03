import os
from google.adk.agents import LlmAgent, SequentialAgent
from google.adk.tools import google_search
from google.adk.tools.agent_tool import AgentTool
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolSet, StdioServerParameters


# 1. Configuracao do Firecrawl MCP Tool

firecrawl_tooset = MCPToolSet(
  connection_params=StdioServerParameters(
        command='npx',
        args=["-y", "firecrawl-mcp"],
        env={
            "FIRECRAWL_API_KEY": os.getenv("FIRECRAWL_API_KEY", "")
        }
    ),
)


#Page Auditor Agent
page_auditor_agent = LlmAgent(
    name="PageAuditorAgent",
    model="gemini-2.5-flash",
    instruction="""Você é o Agente 1 em um fluxo de trabalho sequencial de SEO. Sua função é auditar a página e inferir palavras-chave.

PASSO 1: Extraia a URL da mensagem do usuário.
PASSO 2: Chame a ferramenta 'firecrawl_scrape' com a URL extraída, formatos 'markdown', 'html', 'links', 'onlyMainContent': true e 'timeout': 90000.
PASSO 3: Analise os dados raspados (título, cabeçalhos, contagem de palavras, links, problemas técnicos) e resuma o conteúdo.
PASSO 4: Infira a palavra-chave primária, a intenção de busca (Search Intent) e palavras-chave secundárias de suporte.
PASSO 5: Retorne um JSON estruturado **APENAS** seguindo o schema PageAuditOutput.""",
    tools=[firecrawl_tooset],
    output_schema=PageAuditOutput,
    output_key="page_audit" # Salva o resultado no estado para o próximo agente
)


#Seach Executor Agent
serch_executor_agent = LlmAgent(
  name="perform_google_search",
  model="gemini-2.5-flash",
  instruction= """Execute buscas no Google para a palavra-chave fornecida.
- Retorne JSON com a consulta (query) e um array de resultados (título, url, snippet).
- **APENAS** o texto JSON. Sem comentários adicionais.""",
    tools=[google_search] 
)

google_search_tool = AgentTool(serch_executor_agent)

#Serp Analyst Agent
serp_analyst_agent = LlmAgent(
  name="SerpeAnalystAgent",
  model="gemini-2.5-flash",
  instruction="""Você é o Agente 2. Sua função é analisar a concorrência na SERP.

PASSO 1: Leia a palavra-chave primária de state['page_audit']['target_keywords']['primary_keyword'].
PASSO 2: Chame a ferramenta 'perform_google_search' com a palavra-chave primária.
PASSO 3: Analise os resultados de busca (rank, título, URL, snippet, content_type) dos top 10 concorrentes.
PASSO 4: Identifique padrões nos títulos, formatos de conteúdo dominantes e temas chave abordados pelos concorrentes.
PASSO 5: Retorne um JSON estruturado **APENAS** seguindo o schema SerpAnalysis.""",
    tools=[google_search_tool],
    output_schema=SerpAnalysis,
    output_key="serp_analysis" 

)


#Optimization Advisor Agent
optimization_advisor_agent = LlmAgent(
    name="OptimizationAdvisorAgent",
    model="gemini-2.5-flash",
    instruction="""Você é o Agente 3 e o especialista final no fluxo de trabalho. Seu objetivo é consolidar todas as informações em um relatório de SEO profissional, acionável e bem formatado.

PASSO 1: Revise os dados de state['page_audit'] e state['serp_analysis'].
PASSO 2: Crie um relatório COMPLETO no formato Markdown, contendo:
  - **# Relatório de Auditoria SEO**
  - **Resumo Executivo** (Principais problemas e oportunidades)
  - **1. Achados Técnicos e On-Page** (Com base no Page Audit)
  - **2. Análise de Palavra-Chave** (Intent e Keywords inferidas)
  - **3. Análise Competitiva SERP** (Padrões e Formatos de Conteúdo)
  - **4. Recomendações Priorizadas** (Divididas em P0: Crítico, P1: Alto Impacto, P2: Melhoria) com Racional, Impacto Estimado e Esforço Estimado.
  - **5. Próximas Etapas**

PASSO 3: Retorne **APENAS** o conteúdo Markdown (sem JSON, sem preâmbulo).""",
)


#SEO Audi Team



