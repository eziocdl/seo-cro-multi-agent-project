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
)