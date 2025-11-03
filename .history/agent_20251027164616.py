import os

from google.adk.agents import LlmAgent, SequentialAgent

from google.adk.tools import google_search

from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StdioServerParameters

from .schemas import PageAuditOutput, SerpAnalysis 


# Tools

firecrawl_toolset = MCPToolset(
    connection_params=StdioServerParameters(
        command='npx',
        args=["-y", "firecrawl-mcp"],
       
        env={
            "FIRECRAWL_API_KEY": os.getenv("FIRECRAWL_API_KEY", "")
        }
    ),
    tool_filter=['firecrawl_scrape'] 
)

# 1: Page Auditor Agent 
page_auditor_agent = LlmAgent(
    name="PageAuditorAgent",
    model="gemini-2.5-flash",
    instruction="""Você é o Agente 1 em um fluxo de trabalho sequencial de SEO.

PASSO 1: Extraia a URL exata da mensagem do usuário.
PASSO 2: Chame a ferramenta firecrawl_scrape com parâmetros:
- url: <extracted URL>
- formats: ["markdown", "html", "links"]
- onlyMainContent: true
- timeout: 90000

PASSO 3: Analise os dados raspados (título, word count, links, headings)
PASSO 4: Inferir palavras-chave primárias e secundárias, e intenção de busca.
PASSO 5: Retorne um JSON estruturado APENAS seguindo o schema PageAuditOutput.""",
    tools=[firecrawl_toolset], # Usando o Firecrawl para o scrape
    output_schema=PageAuditOutput,
    output_key="page_audit",
    disallow_transfer_to_parent=True, 
    disallow_transfer_to_peers=True
)


# Agente 2: Serp Analyst Agent (USA google_search DIRETAMENTE)
serp_analyst_agent = LlmAgent(
    name="SerpeAnalystAgent",
    model="gemini-2.5-flash", # MANTÉM Flash para performance/custo
    instruction="""Você é o Agente 2. Sua função é analisar a concorrência na SERP.

PASSO 1: Leia a palavra-chave primária de state['page_audit']['target_keywords']['primary_keyword'].
PASSO 2: Chame a ferramenta 'google_search' com a palavra-chave primária.
PASSO 3: Analise os resultados de busca (rank, título, URL, snippet, content_type) dos top 10 concorrentes.
PASSO 4: Identifique padrões nos títulos, formatos de conteúdo dominantes e temas chave abordados pelos concorrentes.
PASSO 5: Retorne um JSON estruturado APENAS seguindo o schema SerpAnalysis.""",
    tools=[google_search], # INJEÇÃO DIRETA DA FERRAMENTA! (KISS aplicado)
    output_schema=SerpAnalysis,
    output_key="serp_analysis",
    disallow_transfer_to_parent=True, 
    disallow_transfer_to_peers=True
)


# Agente 3: Optimization Advisor Agent (USA PRO para raciocínio superior e relatório)
optimization_advisor_agent = LlmAgent(
    name="OptimizationAdvisorAgent",
    model="gemini-2.5-pro", # MODELO PRO PARA QUALIDADE DO RELATÓRIO FINAL
    instruction="""Você é o Agente 3 e o especialista final no fluxo de trabalho. Seu objetivo é consolidar todas as informações em um relatório de SEO profissional, acionável e bem formatado.

PASSO 1: Revise os dados de state['page_audit'] e state['serp_analysis'].
PASSO 2: Crie um relatório COMPLETO no formato Markdown, contendo:
  - **# Relatório de Auditoria SEO**
  - **Resumo Executivo**
  - **1. Achados Técnicos e On-Page** - **2. Análise de Palavra-Chave** - **3. Análise Competitiva SERP** - **4. Recomendações Priorizadas** (P0: Crítico, P1: Alto Impacto, P2: Melhoria) com Racional, Impacto Estimado e Esforço Estimado.
  - **5. Próximas Etapas**

PASSO 3: Retorne APENAS o conteúdo Markdown (sem JSON, sem preâmbulo).""",
)


# --- 3. Orquestração do Workflow (SequentialAgent) ---

seo_audit_team = SequentialAgent(
    name="SeoAuditTeam",
    description="Pipeline de três agentes: Auditoria On-Page → Análise SERP → Relatório de Otimização.",
    sub_agents=[
        page_auditor_agent,
        serp_analyst_agent,
        optimization_advisor_agent
    ]
)

# A raiz do aplicativo ADK
root_agent = seo_audit_team