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


# agent.py - Page Auditor Agent

page_auditor_agent = LlmAgent(
  name="PageAuditorAgent",
  model="gemini-2.5-flash"
  instruction="""Você é o Agente 1 em um fluxo de trabalho sequencial de SEO. Sua função é auditar a página e inferir palavras-chave.

PASSO 1: Extraia a URL da mensagem do usuário.
PASSO 2: Chame a ferramenta 'firecrawl_scrape' com a URL extraída, formatos 'markdown', 'html', 'links', 'onlyMainContent': true e 'timeout': 90000.
PASSO 3: Analise os dados raspados (título, cabeçalhos, contagem de palavras, links, problemas técnicos) e resuma o conteúdo.
PASSO 4: Infira a palavra-chave primária, a intenção de busca (Search Intent) e palavras-chave secundárias de suporte.
PASSO 5: Retorne um JSON estruturado **APENAS** seguindo o schema PageAuditOutput.""",

        tools=[firecrawl_tooset],
        output_schema=PageAuditOutput,
        output_key="page_audit"
)
  



