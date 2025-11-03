# agent.py

import os
from google.adk.agents import LlmAgent, SequentialAgent

# Importa todos os schemas Pydantic (INCLUI CROAnalysis)
from .schemas import PageAuditOutput, SerpAnalysis, CROAnalysis 


# --- 1. Definição dos Agentes Sequenciais (Pipeline) ---

# Agente 1: Page Auditor Agent (RACIOCÍNIO PURO)
page_auditor_agent = LlmAgent(
    name="PageAuditorAgent",
    model="gemini-2.5-flash", 
    instruction="""You are Agent 1 in a sequential SEO workflow. Your task is to perform a *simulated* on-page audit and keyword inference based ONLY on the URL provided in the user's message.

STEP 1: Infer the Title Tag, Content Summary, and primary/secondary keywords directly from the URL and its implied topic.
STEP 2: For technical fields (link_counts, word_count, findings), provide *reasonable estimates* or simplified assumptions (e.g., 'word_count': 500, 'link_counts': {'internal': 10, 'external': 5}) to simulate an audit.
STEP 3: Fill the PageAuditOutput JSON with the inferred data.
STEP 4: Return ONLY the structured JSON matching the PageAuditOutput schema.""",
    tools=[], # Raciocínio Puro: Solução para erro 400 INVALID_ARGUMENT
    output_schema=PageAuditOutput,
    output_key="page_audit",
    disallow_transfer_to_parent=True, 
    disallow_transfer_to_peers=True
)

# Agente 2: Serp Analyst Agent (RACIOCÍNIO PURO)
serp_analyst_agent = LlmAgent(
    name="SerpeAnalystAgent",
    model="gemini-2.5-flash",
    instruction="""You are Agent 2. Your function is to analyze the competitive SERP.

STEP 1: Read the 'primary_keyword' from state['page_audit']['target_keywords']['primary_keyword'].
STEP 2: *Simulate* the competitive SERP for that keyword, inferring: top competitor titles, common content formats, and key themes/angles used by competitors in the SERP.
STEP 3: Return ONLY the structured JSON matching the SerpAnalysis schema.""",
    tools=[], # Raciocínio Puro
    output_schema=SerpAnalysis,
    output_key="serp_analysis",
    disallow_transfer_to_parent=True, 
    disallow_transfer_to_peers=True
)


# Agente 3: CRO Analyst Agent (NOVO - Foco em Usabilidade e Conversão)
cro_analyst_agent = LlmAgent(
    name="CROAnalystAgent",
    model="gemini-2.5-flash",
    instruction="""You are Agent 3 in the sequential workflow, specialized in CRO and UX. Your task is to perform a *simulated* analysis of the page's conversion potential, usabilty, and funnel based on the inferred data from state['page_audit'].

STEP 1: Analyze the content summary, target keywords, and page structure from the audit data.
STEP 2: Infer common usability issues (e.g., lack of mobile clarity, weak hierarchy) and potential friction points (e.g., missing social proof, vague CTA).
STEP 3: Suggest high-impact CRO opportunities related to the page's search intent.
STEP 4: Return ONLY the structured JSON matching the CROAnalysis schema.""",
    tools=[], # Raciocínio Puro
    output_schema=CROAnalysis,
    output_key="cro_analysis",
    disallow_transfer_to_parent=True, 
    disallow_transfer_to_peers=True
)


# Agente 4: Strategic Advisor Agent (RELATÓRIO FINAL CONSOLIDADO)
strategic_advisor_agent = LlmAgent(
    name="StrategicAdvisorAgent",
    model="gemini-2.5-flash", 
    instruction="""You are the final expert in the workflow, the Strategic Advisor. Your goal is to consolidate all information (SEO, SERP, and CRO) into a professional, actionable, and comprehensive Strategic Digital Audit Report.

STEP 1: Review the data from state['page_audit'], state['serp_analysis'], AND state['cro_analysis'].
STEP 2: Create a COMPREHENSIVE report in Markdown format.

**CRITICAL CONSTRAINT: The entire final report MUST be generated in Portuguese (Brazil - pt-BR).**

The report must contain the following sections:
  - **# Relatório de Auditoria Estratégica Digital** (New comprehensive title)
  - **Resumo Executivo** (Consolidando SEO, CRO, e UX)
  - **1. Auditoria SEO & On-Page** (Achados de PageAuditOutput)
  - **2. Análise Competitiva de Mercado** (Análise de SERP e Oportunidades)
  - **3. Auditoria de Conversão (CRO & UX)** (Achados de CROAnalysis)
  - **4. Recomendações Priorizadas Consolidadas** (Divididas em P0: Crítico, P1: Alto Impacto, P2: Melhoria) cobrindo SEO, UX e CRO, com Racional, Impacto Estimado e Esforço Estimado.
  - **5. Próximas Etapas**

STEP 3: Return ONLY the Markdown content (no JSON, no preamble).""",
    tools=[], # Raciocínio Puro
)

# --- Orquestração do Workflow (SequentialAgent) ---
seo_cro_audit_team = SequentialAgent(
    name="SEOCROAuditTeam",
    description="Pipeline de quatro agentes para Auditoria Estratégica Digital: SEO On-Page → Análise SERP → Análise CRO/UX → Relatório Estratégico Consolidado.",
    sub_agents=[
        page_auditor_agent,
        serp_analyst_agent,
        cro_analyst_agent, 
        strategic_advisor_agent
    ]
)
root_agent = seo_cro_audit_team