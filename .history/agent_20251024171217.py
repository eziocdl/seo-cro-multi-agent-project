# agent.py

import os
# Importações do ADK
from google.adk.agents import LlmAgent, SequentialAgent
# MANTEMOS google_search aqui, pois será a ferramenta de raspagem e SERP
from google.adk.tools import google_search
from google.adk.tools.agent_tool import AgentTool
# REMOVEMOS: from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StdioServerParameters

# Importa os schemas Pydantic (ASSUMIDO: O schemas.py está preenchido corretamente)
from .schemas import PageAuditOutput, SerpAnalysis 


# --- 1. Configuração de Ferramentas (Tools) ---

# REMOVEMOS o bloco 1.1 (Firecrawl MCP Tool) para eliminar a dependência de chave/Node.js

# 1.2. Criação do Agente Auxiliar para Google Search (Workaround ADK)
# Este agente será usado para a Análise SERP (Agente 2)
search_executor_agent = LlmAgent(
    name="perform_google_search",
    model="gemini-2.5-flash",
    instruction= """Execute buscas no Google para a palavra-chave fornecida.
- Retorne JSON com a consulta (query) e um array de resultados (título, url, snippet).
- **APENAS** o texto JSON. Sem comentários adicionais.""",
    tools=[google_search] 
)

google_search_tool = AgentTool(search_executor_agent)

# --- 2. Definição dos Agentes Sequenciais (Pipeline) ---

# Agente 1: Page Auditor Agent (AGORA USA google_search PARA EXTRAÇÃO)
page_auditor_agent = LlmAgent(
    name="PageAuditorAgent",
    model="gemini-2.5-flash",
    instruction="""Você é o Agente 1 em um fluxo de trabalho sequencial de SEO. Sua função é auditar a página e inferir palavras-chave.

PASSO 1: Extraia a URL exata da mensagem do usuário (Ex: 'https://exemplo.com/').
PASSO 2: **Chame a ferramenta google_search** com a URL extraída como consulta, limitando a 1 resultado. Isso fornece o título e o snippet (resumo do conteúdo).
PASSO 3: Analise o Título e o Snippet (resumo do conteúdo) para inferir: palavra-chave primária, a intenção de busca (Search Intent) e palavras-chave secundárias. Faça uma análise de link/tamanho baseada no snippet.
PASSO 4: Preencha o JSON de saída PageAuditOutput com os dados encontrados e inferidos.
PASSO 5: Retorne um JSON estruturado **APENAS** seguindo o schema PageAuditOutput.""",
    # Usando a ferramenta google_search para "raspar" (via snippet)
    tools=[google_search], 
    output_schema=PageAuditOutput,
    output_key="page_audit" # Salva o resultado para o Agente 2
)


# Agente 2: Serp Analyst Agent (INALTERADO)
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
    output_key="serp_analysis" # Salva o resultado para o Agente 3
)


# Agente 3: Optimization Advisor Agent (INALTERADO)
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