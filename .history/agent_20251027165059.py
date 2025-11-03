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


# : Optimization Advisor Agent 
optimization_advisor_agent = LlmAgent(
    name="OptimizationAdvisorAgent",
    model="gemini-2.5-pro",
    instruction="""You are Agent 3 and the final expert in the workflow. Your goal is to consolidate all information into a professional, actionable, and well-formatted SEO report.

STEP 1: Review the data from state['page_audit'] and state['serp_analysis'].
STEP 2: Create a COMPREHENSIVE report in Markdown format.

**CRITICAL CONSTRAINT: The entire final report MUST be generated in Portuguese (Brazil - pt-BR).**

The report must contain:
  - **# Relatório de Auditoria SEO**
  - **Resumo Executivo** (Principais problemas e oportunidades)
  - **1. Achados Técnicos e On-Page** (Com base no Page Audit)
  - **2. Análise de Palavra-Chave** (Intent e Keywords inferidas)
  - **3. Análise Competitiva SERP** (Padrões e Formatos de Conteúdo)
  - **4. Recomendações Priorizadas** (Divididas em P0: Crítico, P1: Alto Impacto, P2: Melhoria) with Rationale, Estimated Impact, and Estimated Effort.
  - **5. Próximas Etapas**

STEP 3: Return ONLY the Markdown content (no JSON, no preamble).""",
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