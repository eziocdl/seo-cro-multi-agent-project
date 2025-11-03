# agent.py

import os
from google.adk.agents import LlmAgent, SequentialAgent
from google.adk.tools import google_search
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StdioServerParameters
from . schemas import PageAuditOutput, SerpAnalysis 


# Tools

# Firecraw 
firecrawl_toolset = MCPToolset(
  command='npx',
  args=["-y", "firecraw-mcp"],
  env = {
    "FIRECRAW_API_KEY": os.getenv("FIRECRAWL_API_KEY", "")
  }
),
tool_filter['firecraw_scrape']
)