# agent.py

import os
from google.adk.agents import LlmAgent, SequentialAgent
from google.adk.tools import google_search
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StdioServerParameters