import os
from google.adk.agents import LlmAgent, SequentialAgent
from google.adk.tools import google_search
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
    tool_filter=['firecrawl_scrape'], 
    tool_invocation_timeout=60.0  #
)

# 1: Page Auditor Agent 
page_auditor_agent = LlmAgent(
    name="PageAuditorAgent",
    model="gemini-2.5-pro", # Mantemos o PRO para estabilidade
    instruction="""You are Agent 1 in a sequential SEO workflow. Your task is to audit the page using its SERP snippet and infer keywords.

STEP 1: Extract the exact URL from the user's message (e.g., 'https://example.com/').
STEP 2: **Call the 'google_search' tool** with the extracted URL as the query, limiting to 1 result. This provides the title and the snippet (content summary).
STEP 3: Analyze the Title and Snippet to infer: primary keyword, search intent, and secondary keywords.
STEP 4: For fields like link_counts and word_count, provide reasonable estimates based on the snippet length or return 0, as full scraping is unavailable due to performance constraints.
STEP 5: Fill the PageAuditOutput JSON with the inferred data.
STEP 6: Return ONLY the structured JSON matching the PageAuditOutput schema.""",
    tools=[google_search], # Usando a ferramenta nativa e RÁPIDA
    output_schema=PageAuditOutput,
    output_key="page_audit",
    disallow_transfer_to_parent=True, 
    disallow_transfer_to_peers=True
)

#2: Serp Analyst Agent (
serp_analyst_agent = LlmAgent(
    name="SerpeAnalystAgent",
    model="gemini-2.5-pro",
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


#3: Optimization Advisor Agent 
optimization_advisor_agent = LlmAgent(
    name="OptimizationAdvisorAgent",
    model="gemini-2.5-pro", 
    instruction="""You are Agent 3 and the final expert in the workflow. Your goal is to consolidate all information into a professional, actionable, and well-formatted SEO report.

STEP 1: Review the data from state['page_audit'] and state['serp_analysis'].
STEP 2: Create a COMPREHENSIVE report in Markdown format.

**CRITICAL CONSTRAINT: The entire final report MUST be generated in Portuguese (Brazil - pt-BR).**

The report must contain the following sections, using the specified Portuguese titles:
  - **# Relatório de Auditoria SEO** (SEO Audit Report)
  - **Resumo Executivo** (Executive Summary, covering main issues and opportunities)
  - **1. Achados Técnicos e On-Page** (Technical and On-Page Findings, based on Page Audit data)
  - **2. Análise de Palavra-Chave** (Keyword Analysis, based on inferred Intent and Keywords)
  - **3. Análise Competitiva SERP** (Competitive SERP Analysis, covering patterns and content formats)
  - **4. Recomendações Priorizadas** (Prioritized Recommendations, divided into P0: Critical, P1: High Impact, P2: Improvement) with Rationale, Estimated Impact, and Estimated Effort.
  - **5. Próximas Etapas** (Next Steps)

STEP 3: Return ONLY the Markdown content (no JSON, no preamble).""",
)

# Workflow Orchestration
seo_audit_team = SequentialAgent(
    name="SeoAuditTeam",
    description="Pipeline de três agentes: Auditoria On-Page → Análise SERP → Relatório de Otimização.",
    sub_agents=[
        page_auditor_agent,
        serp_analyst_agent,
        optimization_advisor_agent
    ]
)
root_agent = seo_audit_team