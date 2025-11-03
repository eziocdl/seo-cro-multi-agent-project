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
    instruction="""You are Agent 1 in a sequential SEO workflow. Your task is to perform an on-page audit and infer target keywords.

STEP 1: Extract the exact URL from the user's message.
STEP 2: Call the 'firecrawl_scrape' tool with the following parameters:
- url: <extracted URL>
- formats: ["markdown", "html", "links"]
- onlyMainContent: true
- timeout: 90000

STEP 3: Analyze the scraped data (title, word count, links, headings) and fill the AuditResults schema.
STEP 4: Infer the primary keyword, search intent, and secondary keywords based on content analysis, and fill the TargetKeywords schema.
STEP 5: Return ONLY the structured JSON matching the PageAuditOutput schema.""",
    tools=[firecrawl_toolset],
    output_schema=PageAuditOutput,
    output_key="page_audit",
    disallow_transfer_to_parent=True, 
    disallow_transfer_to_peers=True
)

#2: Serp Analyst Agent (
serp_analyst_agent = LlmAgent(
    name="SerpeAnalystAgent",
    model="gemini-2.5-flash",
    instruction="""You are Agent 2. Your function is to analyze the competitive SERP (Search Engine Results Page).

STEP 1: Read the 'primary_keyword' from state['page_audit']['target_keywords']['primary_keyword'].
STEP 2: Call the 'google_search' tool with the primary keyword.
STEP 3: Analyze the top 10 search results (rank, title, URL, snippet).
STEP 4: Identify common title patterns, dominant content formats, and key themes/angles used by competitors.
STEP 5: Return ONLY the structured JSON matching the SerpAnalysis schema.""",
    tools=[google_search],
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