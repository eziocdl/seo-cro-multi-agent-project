# agent.py

import os
from google.adk.agents import LlmAgent, SequentialAgent
# REMOVEMOS a importação 'from google.adk.tools import google_search'

from .schemas import PageAuditOutput, SerpAnalysis 


# 1: Page Auditor Agent (RACIOCÍNIO PURO)
page_auditor_agent = LlmAgent(
    name="PageAuditorAgent",
    model="gemini-2.5-flash", 
    instruction="""You are Agent 1 in a sequential SEO workflow. Your task is to perform a *simulated* on-page audit and keyword inference based ONLY on the URL provided in the user's message.

STEP 1: Infer the Title Tag, Content Summary, and primary/secondary keywords directly from the URL and its implied topic.
STEP 2: For technical fields (link_counts, word_count, findings), provide *reasonable estimates* or simplified assumptions (e.g., 'word_count': 500, 'link_counts': {'internal': 10, 'external': 5}) to simulate an audit.
STEP 3: Fill the PageAuditOutput JSON with the inferred data.
STEP 4: Return ONLY the structured JSON matching the PageAuditOutput schema.""",
    tools=[], # CORREÇÃO FINAL: Removido o tools=[google_search] para evitar o erro 400
    output_schema=PageAuditOutput,
    output_key="page_audit",
    disallow_transfer_to_parent=True, 
    disallow_transfer_to_peers=True
)

#2: Serp Analyst Agent (RACIOCÍNIO PURO)
serp_analyst_agent = LlmAgent(
    name="SerpeAnalystAgent",
    model="gemini-2.5-flash",
    instruction="""You are Agent 2. Your function is to analyze the competitive SERP.

STEP 1: Read the 'primary_keyword' from state['page_audit']['target_keywords']['primary_keyword'].
STEP 2: *Simulate* the competitive SERP for that keyword, inferring: top competitor titles, common content formats, and key themes/angles used by competitors in the SERP.
STEP 3: Return ONLY the structured JSON matching the SerpAnalysis schema.""",
    tools=[], # CORREÇÃO FINAL: Removido o tools=[google_search]
    output_schema=SerpAnalysis,
    output_key="serp_analysis",
    disallow_transfer_to_parent=True, 
    disallow_transfer_to_peers=True
)


#3: Optimization Advisor Agent (RACIOCÍNIO PURO)
optimization_advisor_agent = LlmAgent(
    name="OptimizationAdvisorAgent",
    model="gemini-2.5-flash", 
    instruction="""You are Agent 3 and the final expert in the workflow. Your goal is to consolidate the SIMULATED data from state['page_audit'] and state['serp_analysis'] into a professional, actionable SEO report.

STEP 1: Review the data from state['page_audit'] and state['serp_analysis'].
STEP 2: Create a COMPREHENSIVE report in Markdown format.

**CRITICAL CONSTRAINT: The entire final report MUST be generated in Portuguese (Brazil - pt-BR).**

The report must contain the following sections, using the specified Portuguese titles:
  - **# Relatório de Auditoria SEO** (SEO Audit Report)
  - **Resumo Executivo** (Executive Summary, covering main issues and opportunities)
  - **1. Achados Técnicos e On-Page** (Technical and On-Page Findings, based on Page Audit data)
  - **2. Análise de Palavra-Chave** (Keyword Analysis, based on inferred Intent and Keywords)
  - **3. Análise Competitiva SERP** (Competitive SERP Analysis, covering patterns and content formats)
  - **4. Recomendações Priorizadas** (Prioritized Recommendations, divided into P0: Crítico, P1: Alto Impacto, P2: Melhoria) with Rationale, Estimated Impact, and Estimated Effort.
  - **5. Próximas Etapas** (Next Steps)

STEP 3: Return ONLY the Markdown content (no JSON, no preamble).""",
    tools=[], # CORREÇÃO FINAL: Removido o tools=[] apenas por consistência, mas não afeta Agente 3
)

# Workflow Orchestration
seo_audit_team = SequentialAgent(
    name="SeoAuditTeam",
    description="Pipeline de três agentes: Auditoria On-Page (Simulada) → Análise SERP (Simulada) → Relatório de Otimização.",
    sub_agents=[
        page_auditor_agent,
        serp_analyst_agent,
        optimization_advisor_agent
    ]
)
root_agent = seo_audit_team