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
         "FIRECRAWL_API_KEY": os.getenv()
    }
  )
)