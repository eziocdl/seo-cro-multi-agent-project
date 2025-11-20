Repository: eziocdl/seo-cro-multi-agent-project
Files analyzed: 122

Estimated tokens: 63.8k

Directory structure:
└── eziocdl-seo-cro-multi-agent-project/
├── **init**.py
├── agent.py
├── app_runner.py
├── package.json
├── report_generator.py
├── requirements.txt
├── schemas.py
└── .history/
├── **init\_**20251024153937.py
├── **init\_**20251024153957.py
├── agent_20251024144848.py
├── agent_20251024145153.py
├── agent_20251024151717.py
├── agent_20251024152020.py
├── agent_20251024152227.py
├── agent_20251024152310.py
├── agent_20251024152620.py
├── agent_20251024152658.py
├── agent_20251024152715.py
├── agent_20251024153001.py
├── agent_20251024153050.py
├── agent_20251024153426.py
├── agent_20251024153634.py
├── agent_20251024153715.py
├── agent_20251024153853.py
├── agent_20251024153942.py
├── agent_20251024161351.py
├── agent_20251024161509.py
├── agent_20251024165348.py
├── agent_20251024165636.py
├── agent_20251024170400.py
├── agent_20251024171217.py
├── agent_20251027163818.py
├── agent_20251027164348.py
├── agent_20251027164450.py
├── agent_20251027164616.py
├── agent_20251027164939.py
├── agent_20251027165009.py
├── agent_20251027165059.py
├── agent_20251027165316.py
├── agent_20251027165413.py
├── agent_20251027165415.py
├── agent_20251027174248.py
├── agent_20251027174727.py
├── agent_20251027174919.py
├── agent_20251027175734.py
├── agent_20251027175800.py
├── agent_20251027175936.py
├── agent_20251027175942.py
├── agent_20251027175948.py
├── agent_20251027180328.py
├── agent_20251027181027.py
├── agent_20251027181137.py
├── agent_20251027182618.py
├── app_runner_20251031120621.py
├── app_runner_20251031120646.py
├── app_runner_20251031120726.py
├── report_generator_20251031120158.py
├── report_generator_20251031120316.py
├── requirements_20251024111445.txt
├── requirements_20251024111456.txt
├── requirements_20251031120125.txt
├── schemas_20251024134800.py
├── schemas_20251024135043.py
├── schemas_20251024135053.py
├── schemas_20251024135247.py
├── schemas_20251024135346.py
├── schemas_20251024135430.py
├── schemas_20251024135518.py
├── schemas_20251024140631.py
├── schemas_20251024140821.py
├── schemas_20251024140932.py
├── schemas_20251024140944.py
├── schemas_20251024141028.py
├── schemas_20251024141108.py
├── schemas_20251024141141.py
├── schemas_20251024141225.py
├── schemas_20251024141331.py
├── schemas_20251024141736.py
├── schemas_20251024141759.py
├── schemas_20251024141849.py
├── schemas_20251024142529.py
├── schemas_20251024142553.py
├── schemas_20251024142701.py
├── schemas_20251024142736.py
├── schemas_20251024143047.py
├── schemas_20251024143420.py
├── schemas_20251024143531.py
├── schemas_20251024143545.py
├── schemas_20251024143602.py
├── schemas_20251024143621.py
├── schemas_20251024144004.py
├── schemas_20251024144033.py
├── schemas_20251024144109.py
├── schemas_20251024144200.py
├── schemas_20251024144258.py
├── schemas_20251024144331.py
├── schemas_20251024144356.py
├── schemas_20251024144409.py
├── schemas_20251024144820.py
├── schemas_20251024161321.py
├── schemas_20251027165600.py
├── schemas_20251027165638.py
├── schemas_20251027165709.py
├── schemas_20251027171538.py
├── schemas_20251027171605.py
├── schemas_20251027171622.py
├── schemas_20251027171643.py
├── schemas_20251027171700.py
├── schemas_20251027182547.py
├── .env_20251024154627
├── .env_20251024154640
├── .env_20251024155721
├── .env_20251024160715
├── .env_20251024163334
├── .env_20251024172119
├── .env_20251024172701
├── .env_20251027172524
├── .env_20251027172548
├── .env_20251027172859
├── .env_20251027180503
├── .gitignore_20251024110235
└── .gitignore_20251024110436

================================================
FILE: **init**.py
================================================

# **init**.py

from .agent import root_agent

**all** = ["root_agent"]

================================================
FILE: agent.py
================================================

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
instruction="""You are Agent 1 in a sequential SEO workflow. Your task is to perform a _simulated_ on-page audit and keyword inference based ONLY on the URL provided in the user's message.

STEP 1: Infer the Title Tag, Content Summary, and primary/secondary keywords directly from the URL and its implied topic.
STEP 2: For technical fields (link_counts, word_count, findings), provide _reasonable estimates_ or simplified assumptions (e.g., 'word_count': 500, 'link_counts': {'internal': 10, 'external': 5}) to simulate an audit.
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
STEP 2: _Simulate_ the competitive SERP for that keyword, inferring: top competitor titles, common content formats, and key themes/angles used by competitors in the SERP.
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
instruction="""You are Agent 3 in the sequential workflow, specialized in CRO and UX. Your task is to perform a _simulated_ analysis of the page's conversion potential, usabilty, and funnel based on the inferred data from state['page_audit'].

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

================================================
FILE: app_runner.py
================================================
from pydantic import BaseModel, Field
from enum import Enum
from typing import List, Optional
import docx
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.colors import black
from reportlab.lib.enums import TA_CENTER
from io import BytesIO
import markdown
import os

# --- CONFIGURAÇÕES DE DADOS (Para comunicação com FastAPI) ---

class ReportFormat(str, Enum):
"""Define os formatos de relatório disponíveis."""
WORD = "word"
PDF = "pdf"
MARKDOWN = "markdown"

class ReportGenerationRequest(BaseModel):
"""Schema para a requisição da API de geração de relatório."""
url: str
report_format: ReportFormat = Field(
default=ReportFormat.PDF,
description="Formato desejado para o relatório"
)
language: str = Field(
default="pt-BR",
description="Idioma do relatório (ajusta o Agente 4)"
)

# --- CLASSE DE ESTILO PARA PDF (ReportLab) ---

class ReportStyleConfig:
"""Configurações de estilo para relatórios PDF (ReportLab)."""

    @staticmethod
    def get_pdf_styles():
        """Configura estilos de parágrafo e cabeçalho."""
        styles = getSampleStyleSheet()

        styles.add(ParagraphStyle(
            name='H1Style',
            parent=styles['Title'],
            fontName='Helvetica-Bold',
            fontSize=18,
            textColor=black,
            alignment=TA_CENTER,
            spaceAfter=18
        ))

        styles.add(ParagraphStyle(
            name='H2Style',
            parent=styles['Heading2'],
            fontName='Helvetica-Bold',
            fontSize=14,
            textColor=black,
            spaceAfter=6
        ))

        styles.add(ParagraphStyle(
            name='NormalStyle',
            parent=styles['Normal'],
            fontName='Helvetica',
            fontSize=10,
            textColor=black,
            leading=12,
            spaceAfter=8
        ))

        return styles

# --- CLASSE PRINCIPAL DE GERAÇÃO DE ARQUIVOS (SRP) ---

class ReportGenerator:
"""Responsável por converter conteúdo Markdown em arquivos binários."""

    @staticmethod
    def generate_report(content: str, format: ReportFormat, url: str) -> BytesIO:
        """
        Gera relatório no formato especificado (PDF, DOCX ou MARKDOWN),
        retornando um objeto BytesIO para o FastAPI.
        """
        if format == ReportFormat.WORD:
            return ReportGenerator._generate_word_report(content)

        elif format == ReportFormat.PDF:
            return ReportGenerator._generate_pdf_report(content)

        elif format == ReportFormat.MARKDOWN:
            return BytesIO(content.encode('utf-8'))

        raise ValueError(f"Formato {format.value} não suportado.")

    @staticmethod
    def _generate_word_report(content: str) -> BytesIO:
        """Gera relatório em Word (.docx)."""
        doc = docx.Document()
        doc.add_heading('Relatório de Auditoria Estratégica Digital', 0)

        # Converte Markdown para parágrafos simples
        lines = content.split('\n')
        for line in lines:
            line = line.strip()
            if line.startswith('# '):
                doc.add_heading(line.replace('# ', ''), level=1)
            elif line.startswith('## '):
                doc.add_heading(line.replace('## ', ''), level=2)
            elif line:
                doc.add_paragraph(line)

        file_stream = BytesIO()
        doc.save(file_stream)
        file_stream.seek(0)
        return file_stream

    @staticmethod
    def _generate_pdf_report(content: str) -> BytesIO:
        """Gera relatório em PDF (ReportLab)."""
        file_stream = BytesIO()
        doc = SimpleDocTemplate(file_stream, pagesize=letter)
        styles = ReportStyleConfig.get_pdf_styles()
        elements = []

        # Processa o Markdown linha por linha para formatação PDF
        lines = content.split('\n')
        for line in lines:
            line = line.strip()
            if line.startswith('# '):
                elements.append(Paragraph(line.replace('# ', ''), styles['H1Style']))
            elif line.startswith('## '):
                elements.append(Paragraph(line.replace('## ', ''), styles['H2Style']))
            elif line.startswith('- '):
                # Formatação de lista simples
                elements.append(Paragraph(f'&bull; {line.replace("- ", "").strip()}', styles['NormalStyle']))
            elif line:
                elements.append(Paragraph(line, styles['NormalStyle']))

            elements.append(Spacer(1, 6))

        doc.build(elements)
        file_stream.seek(0)
        return file_stream

================================================
FILE: package.json
================================================
{
"dependencies": {
"firecrawl-mcp": "^3.5.2"
}
}

================================================
FILE: report_generator.py
================================================

from pydantic import BaseModel, Field
from enum import Enum
from typing import List, Optional
import docx
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.colors import black
from reportlab.lib.enums import TA_CENTER
from io import BytesIO
import markdown
import os

# --- CONFIGURAÇÕES DE DADOS (Padrão Pydantic/Enum) ---

class ReportFormat(str, Enum):
"""Enum para formatos de relatório"""
WORD = "word"
PDF = "pdf"
MARKDOWN = "markdown"

class ReportGenerationRequest(BaseModel):
"""Schema para a requisição da API de geração de relatório."""
url: str
report_format: ReportFormat = Field(
default=ReportFormat.PDF,
description="Formato desejado para o relatório"
)
language: str = Field(
default="pt-BR",
description="Idioma do relatório"
)

# --- CLASSE DE ESTILO PARA PDF (ReportLab) ---

class ReportStyleConfig:
"""Configurações de estilo para geração de relatórios PDF (ReportLab)."""

    @staticmethod
    def get_pdf_styles():
        """Configura estilos personalizados para PDF."""
        styles = getSampleStyleSheet()

        styles.add(ParagraphStyle(
            name='H1Style',
            parent=styles['Title'],
            fontName='Helvetica-Bold',
            fontSize=18,
            textColor=black,
            alignment=TA_CENTER,
            spaceAfter=18
        ))

        styles.add(ParagraphStyle(
            name='H2Style',
            parent=styles['Heading2'],
            fontName='Helvetica-Bold',
            fontSize=14,
            textColor=black,
            spaceAfter=6
        ))

        styles.add(ParagraphStyle(
            name='NormalStyle',
            parent=styles['Normal'],
            fontName='Helvetica',
            fontSize=10,
            textColor=black,
            leading=12,
            spaceAfter=8
        ))

        return styles

# --- CLASSE PRINCIPAL DE GERAÇÃO DE ARQUIVOS (SRP) ---

class ReportGenerator:
"""Responsável por converter conteúdo Markdown em arquivos binários."""

    @staticmethod
    def generate_report(content: str, format: ReportFormat, url: str) -> BytesIO:
        """
        Gera relatório no formato especificado, retornando um objeto BytesIO.
        """
        if format == ReportFormat.WORD:
            return ReportGenerator._generate_word_report(content)

        elif format == ReportFormat.PDF:
            return ReportGenerator._generate_pdf_report(content)

        elif format == ReportFormat.MARKDOWN:
            return BytesIO(content.encode('utf-8'))

        raise ValueError(f"Formato {format.value} não suportado.")

    @staticmethod
    def _generate_word_report(content: str) -> BytesIO:
        """Gera relatório em Word (.docx)."""
        doc = docx.Document()
        doc.add_heading('Relatório de Auditoria Estratégica Digital', 0)

        # Converte Markdown para parágrafos simples
        lines = content.split('\n')
        for line in lines:
            line = line.strip()
            if line.startswith('# '):
                doc.add_heading(line.replace('# ', ''), level=1)
            elif line.startswith('## '):
                doc.add_heading(line.replace('## ', ''), level=2)
            elif line:
                doc.add_paragraph(line)

        file_stream = BytesIO()
        doc.save(file_stream)
        file_stream.seek(0)
        return file_stream

    @staticmethod
    def _generate_pdf_report(content: str) -> BytesIO:
        """Gera relatório em PDF (ReportLab)."""
        file_stream = BytesIO()
        doc = SimpleDocTemplate(file_stream, pagesize=letter)
        styles = ReportStyleConfig.get_pdf_styles()
        elements = []

        lines = content.split('\n')
        for line in lines:
            line = line.strip()
            if line.startswith('# '):
                elements.append(Paragraph(line.replace('# ', ''), styles['H1Style']))
            elif line.startswith('## '):
                elements.append(Paragraph(line.replace('## ', ''), styles['H2Style']))
            elif line.startswith('- '):
                elements.append(Paragraph(f'&bull; {line.replace("- ", "").strip()}', styles['NormalStyle']))
            elif line:
                elements.append(Paragraph(line, styles['NormalStyle']))

            elements.append(Spacer(1, 6))

        doc.build(elements)
        file_stream.seek(0)
        return file_stream

================================================
FILE: requirements.txt
================================================

# requirements.txt

google-adk
pydantic
python-docx
reportlab
markdown
fastapi
uvicorn
python-multipart

================================================
FILE: schemas.py
================================================

# schemas.py

from pydantic import BaseModel, Field
from typing import List, Optional

# --- ESTRUTURAS AUXILIARES PADRÃO SEO ---

class LinkCounts(BaseModel):
internal: int = Field(..., description="Number of internal links found on the page.")
external: int = Field(..., description="Number of external links found on the page.")

class HeadingItem(BaseModel):
tag: str = Field(..., description="Heading tag such as h1, h2, h3.")
text: str = Field(..., description="Text content of the heading.")

class TargetKeywords(BaseModel):
primary_keyword: str = Field(..., description="The main keyword the page is optimized for.")
search_intent: str = Field(..., description="Inferred search intent (e.g., informational, commercial, transactional).")
secondary_keywords: List[str] = Field(default_factory=list, description="A list of supporting, long-tail, or related keywords.")

class AuditResults(BaseModel):
title_tag: str
meta_description: str
primary_heading: str
secondary_headings: List[HeadingItem]
word_count: Optional[int]
content_summary: str
link_counts: LinkCounts
technical_findings: List[str] = Field(default_factory=list, description="List of technical SEO issues found.")
content_opportunities: List[str] = Field(default_factory=list, description="List of immediate content opportunities.")

# --- SAÍDAS DE AGENTES SEO ---

class PageAuditOutput(BaseModel):
audit_results: AuditResults
target_keywords: TargetKeywords

class SerpResult(BaseModel):
rank: int = Field(..., description="The organic search rank (1-10).")
title: str = Field(..., description="The title tag of the search result.")
url: str = Field(..., description="The URL of the competitor page.")
snippet: str = Field(..., description="The short description/snippet from the search result.")
content_type: str = Field(..., description="Inferred content format (e.g., blog post, landing page, video, product page).")

class SerpAnalysis(BaseModel):
keyword_searched: str
top_competitors: List[SerpResult]
common_title_patterns: List[str] = Field(default_factory=list, description="Common phrases or structures in the top-ranking titles.")
dominant_content_format: str = Field(..., description="The most common content format (e.g., 'How-to guides', 'Listicles').")
key_themes_and_angles: List[str] = Field(default_factory=list, description="Key topics, themes, or differentiation angles to cover.")
serp_opportunities: List[str] = Field(default_factory=list, description="Specific opportunities based on SERP analysis.")

# --- NOVAS ESTRUTURAS CRO/UX (ADICIONADAS) ---

class UsabilityItem(BaseModel):
area: str = Field(..., description="Area of focus (e.g., Clarity, Frictions, Mobile).")
finding: str = Field(..., description="Specific finding or issue related to the area.")

class ConversionOpportunity(BaseModel):
opportunity: str = Field(..., description="Specific, high-impact recommendation (e.g., Test new CTA copy).")
rationale: str = Field(..., description="Justification for the recommendation.")

# --- NOVA SAÍDA DO AGENTE CRO/UX ---

class CROAnalysis(BaseModel):
usability_findings: List[UsabilityItem] = Field(default_factory=list, description="Detailed findings on UX/Usability (simulated).")
conversion_friction_points: List[str] = Field(default_factory=list, description="Points in the funnel where conversion is likely dropping.")
high_impact_cro_opportunities: List[ConversionOpportunity] = Field(default_factory=list, description="Prioritized recommendations for conversion lift.")
inferred_user_journey: str = Field(..., description="The inferred steps a user takes on this page (e.g., Arrive -> Read Benefit -> Click CTA).")

================================================
FILE: .history/**init\_**20251024153937.py
================================================

================================================
FILE: .history/**init\_**20251024153957.py
================================================

# **init**.py

from .agent import root_agent

**all** = ["root_agent"]

================================================
FILE: .history/agent_20251024144848.py
================================================

================================================
FILE: .history/agent_20251024145153.py
================================================
import os
from google.adk.agents import LlmAgent, SequentialAgent
from google.adk.tools import google_search
from google.adk.tools.agent_tool import AgentTool
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolSet, StdioServerParameters

================================================
FILE: .history/agent_20251024151717.py
================================================
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
""
}
)
)

================================================
FILE: .history/agent_20251024152020.py
================================================
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

================================================
FILE: .history/agent_20251024152227.py
================================================
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
"FIRECRAWL_API_KEY": os.getenv("FIRECRAW_API_KEY", "")

    }

),
tool_filter=['firecrawl_scrape']
)

================================================
FILE: .history/agent_20251024152310.py
================================================
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

================================================
FILE: .history/agent_20251024152620.py
================================================
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
instruction=""""""
)

================================================
FILE: .history/agent_20251024152658.py
================================================
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

================================================
FILE: .history/agent_20251024152715.py
================================================
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
)

================================================
FILE: .history/agent_20251024153001.py
================================================
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

================================================
FILE: .history/agent_20251024153050.py
================================================
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

================================================
FILE: .history/agent_20251024153426.py
================================================
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

#Page Auditor Agent
page_auditor_agent = LlmAgent(
name="PageAuditorAgent",
model="gemini-2.5-flash",
instruction="""Você é o Agente 1 em um fluxo de trabalho sequencial de SEO. Sua função é auditar a página e inferir palavras-chave.

PASSO 1: Extraia a URL da mensagem do usuário.
PASSO 2: Chame a ferramenta 'firecrawl_scrape' com a URL extraída, formatos 'markdown', 'html', 'links', 'onlyMainContent': true e 'timeout': 90000.
PASSO 3: Analise os dados raspados (título, cabeçalhos, contagem de palavras, links, problemas técnicos) e resuma o conteúdo.
PASSO 4: Infira a palavra-chave primária, a intenção de busca (Search Intent) e palavras-chave secundárias de suporte.
PASSO 5: Retorne um JSON estruturado **APENAS** seguindo o schema PageAuditOutput.""",
tools=[firecrawl_tooset],
output_schema=PageAuditOutput,
output_key="page_audit" # Salva o resultado no estado para o próximo agente
)

#Seach Executor Agent
serch_executor_agent = LlmAgent(
name="perform_google_search",
model="gemini-2.5-flash",
instruction=
)

================================================
FILE: .history/agent_20251024153634.py
================================================
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

#Page Auditor Agent
page_auditor_agent = LlmAgent(
name="PageAuditorAgent",
model="gemini-2.5-flash",
instruction="""Você é o Agente 1 em um fluxo de trabalho sequencial de SEO. Sua função é auditar a página e inferir palavras-chave.

PASSO 1: Extraia a URL da mensagem do usuário.
PASSO 2: Chame a ferramenta 'firecrawl_scrape' com a URL extraída, formatos 'markdown', 'html', 'links', 'onlyMainContent': true e 'timeout': 90000.
PASSO 3: Analise os dados raspados (título, cabeçalhos, contagem de palavras, links, problemas técnicos) e resuma o conteúdo.
PASSO 4: Infira a palavra-chave primária, a intenção de busca (Search Intent) e palavras-chave secundárias de suporte.
PASSO 5: Retorne um JSON estruturado **APENAS** seguindo o schema PageAuditOutput.""",
tools=[firecrawl_tooset],
output_schema=PageAuditOutput,
output_key="page_audit" # Salva o resultado no estado para o próximo agente
)

#Seach Executor Agent
serch_executor_agent = LlmAgent(
name="perform_google_search",
model="gemini-2.5-flash",
instruction= """Execute buscas no Google para a palavra-chave fornecida.

- Retorne JSON com a consulta (query) e um array de resultados (título, url, snippet).
- **APENAS** o texto JSON. Sem comentários adicionais.""",
  tools=[google_search]
  )

google_search_tool = AgentTool(serch_executor_agent)

#Serp Analyst Agent
serp_analyst_agent = LlmAgent(
name="SerpeAnalystAgent",
model="gemini-2.5-flash",

)

================================================
FILE: .history/agent_20251024153715.py
================================================
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

#Page Auditor Agent
page_auditor_agent = LlmAgent(
name="PageAuditorAgent",
model="gemini-2.5-flash",
instruction="""Você é o Agente 1 em um fluxo de trabalho sequencial de SEO. Sua função é auditar a página e inferir palavras-chave.

PASSO 1: Extraia a URL da mensagem do usuário.
PASSO 2: Chame a ferramenta 'firecrawl_scrape' com a URL extraída, formatos 'markdown', 'html', 'links', 'onlyMainContent': true e 'timeout': 90000.
PASSO 3: Analise os dados raspados (título, cabeçalhos, contagem de palavras, links, problemas técnicos) e resuma o conteúdo.
PASSO 4: Infira a palavra-chave primária, a intenção de busca (Search Intent) e palavras-chave secundárias de suporte.
PASSO 5: Retorne um JSON estruturado **APENAS** seguindo o schema PageAuditOutput.""",
tools=[firecrawl_tooset],
output_schema=PageAuditOutput,
output_key="page_audit" # Salva o resultado no estado para o próximo agente
)

#Seach Executor Agent
serch_executor_agent = LlmAgent(
name="perform_google_search",
model="gemini-2.5-flash",
instruction= """Execute buscas no Google para a palavra-chave fornecida.

- Retorne JSON com a consulta (query) e um array de resultados (título, url, snippet).
- **APENAS** o texto JSON. Sem comentários adicionais.""",
  tools=[google_search]
  )

google_search_tool = AgentTool(serch_executor_agent)

#Serp Analyst Agent
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
output_key="serp_analysis"

)

================================================
FILE: .history/agent_20251024153853.py
================================================
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

#Page Auditor Agent
page_auditor_agent = LlmAgent(
name="PageAuditorAgent",
model="gemini-2.5-flash",
instruction="""Você é o Agente 1 em um fluxo de trabalho sequencial de SEO. Sua função é auditar a página e inferir palavras-chave.

PASSO 1: Extraia a URL da mensagem do usuário.
PASSO 2: Chame a ferramenta 'firecrawl_scrape' com a URL extraída, formatos 'markdown', 'html', 'links', 'onlyMainContent': true e 'timeout': 90000.
PASSO 3: Analise os dados raspados (título, cabeçalhos, contagem de palavras, links, problemas técnicos) e resuma o conteúdo.
PASSO 4: Infira a palavra-chave primária, a intenção de busca (Search Intent) e palavras-chave secundárias de suporte.
PASSO 5: Retorne um JSON estruturado **APENAS** seguindo o schema PageAuditOutput.""",
tools=[firecrawl_tooset],
output_schema=PageAuditOutput,
output_key="page_audit" # Salva o resultado no estado para o próximo agente
)

#Seach Executor Agent
serch_executor_agent = LlmAgent(
name="perform_google_search",
model="gemini-2.5-flash",
instruction= """Execute buscas no Google para a palavra-chave fornecida.

- Retorne JSON com a consulta (query) e um array de resultados (título, url, snippet).
- **APENAS** o texto JSON. Sem comentários adicionais.""",
  tools=[google_search]
  )

google_search_tool = AgentTool(serch_executor_agent)

#Serp Analyst Agent
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
output_key="serp_analysis"

)

#Optimization Advisor Agent
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

#SEO Audi Team

================================================
FILE: .history/agent_20251024153942.py
================================================
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

#Page Auditor Agent
page_auditor_agent = LlmAgent(
name="PageAuditorAgent",
model="gemini-2.5-flash",
instruction="""Você é o Agente 1 em um fluxo de trabalho sequencial de SEO. Sua função é auditar a página e inferir palavras-chave.

PASSO 1: Extraia a URL da mensagem do usuário.
PASSO 2: Chame a ferramenta 'firecrawl_scrape' com a URL extraída, formatos 'markdown', 'html', 'links', 'onlyMainContent': true e 'timeout': 90000.
PASSO 3: Analise os dados raspados (título, cabeçalhos, contagem de palavras, links, problemas técnicos) e resuma o conteúdo.
PASSO 4: Infira a palavra-chave primária, a intenção de busca (Search Intent) e palavras-chave secundárias de suporte.
PASSO 5: Retorne um JSON estruturado **APENAS** seguindo o schema PageAuditOutput.""",
tools=[firecrawl_tooset],
output_schema=PageAuditOutput,
output_key="page_audit" # Salva o resultado no estado para o próximo agente
)

#Seach Executor Agent
serch_executor_agent = LlmAgent(
name="perform_google_search",
model="gemini-2.5-flash",
instruction= """Execute buscas no Google para a palavra-chave fornecida.

- Retorne JSON com a consulta (query) e um array de resultados (título, url, snippet).
- **APENAS** o texto JSON. Sem comentários adicionais.""",
  tools=[google_search]
  )

google_search_tool = AgentTool(serch_executor_agent)

#Serp Analyst Agent
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
output_key="serp_analysis"

)

#Optimization Advisor Agent
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

#SEO Audi Team

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

================================================
FILE: .history/agent_20251024161351.py
================================================

# agent.py

import os

# Importações do ADK

from google.adk.agents import LlmAgent, SequentialAgent
from google.adk.tools import google_search
from google.adk.tools.agent_tool import AgentTool
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StdioServerParameters

# ^^^^^^^ CORRIGIDO: Nome da classe

# Importa os schemas Pydantic definidos em schemas.py (Linha que estava faltando!)

from .schemas import PageAuditOutput, SerpAnalysis

# --- 1. Configuração de Ferramentas (Tools) ---

# 1.1. Configuração do Firecrawl MCP Tool

# Usando o nome de variável correto: firecrawl_toolset

firecrawl_toolset = MCPToolset(

# ^^^^^^^^^ CORRIGIDO

connection_params=StdioServerParameters(
command='npx',
args=["-y", "firecrawl-mcp"],
env={
"FIRECRAWL_API_KEY": os.getenv("FIRECRAWL_API_KEY", "")
}
),
tool_filter=['firecrawl_scrape'] # Adicionando o filtro, melhor prática
)

# 1.2. Criação do Agente Auxiliar para Google Search (Workaround ADK)

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

# Agente 1: Page Auditor Agent

page_auditor_agent = LlmAgent(
name="PageAuditorAgent",
model="gemini-2.5-flash",
instruction="""Você é o Agente 1 em um fluxo de trabalho sequencial de SEO. Sua função é auditar a página e inferir palavras-chave.

PASSO 1: Extraia a URL da mensagem do usuário.
PASSO 2: Chame a ferramenta 'firecrawl_scrape' com a URL extraída, formatos 'markdown', 'html', 'links', 'onlyMainContent': true e 'timeout': 90000.
PASSO 3: Analise os dados raspados (título, cabeçalhos, contagem de palavras, links, problemas técnicos) e resuma o conteúdo.
PASSO 4: Infira a palavra-chave primária, a intenção de busca (Search Intent) e palavras-chave secundárias de suporte.
PASSO 5: Retorne um JSON estruturado **APENAS** seguindo o schema PageAuditOutput.""",
tools=[firecrawl_toolset], # Usando a variável corrigida
output_schema=PageAuditOutput,
output_key="page_audit" # Salva o resultado no estado para o próximo agente
)

# Agente 2: Serp Analyst Agent

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
output_key="serp_analysis"

)

# Agente 3: Optimization Advisor Agent

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

================================================
FILE: .history/agent_20251024161509.py
================================================

# agent.py

import os

# Importações do ADK

from google.adk.agents import LlmAgent, SequentialAgent
from google.adk.tools import google_search
from google.adk.tools.agent_tool import AgentTool
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StdioServerParameters

# Importa os schemas Pydantic definidos em schemas.py (Linha que estava faltando!)

from .schemas import PageAuditOutput, SerpAnalysis

# --- 1. Configuração de Ferramentas (Tools) ---

# 1.1. Configuração do Firecrawl MCP Tool

# Usando o nome de variável correto: firecrawl_toolset

firecrawl_toolset = MCPToolset(

# ^^^^^^^^^ CORRIGIDO

connection_params=StdioServerParameters(
command='npx',
args=["-y", "firecrawl-mcp"],
env={
"FIRECRAWL_API_KEY": os.getenv("FIRECRAWL_API_KEY", "")
}
),
tool_filter=['firecrawl_scrape'] # Adicionando o filtro, melhor prática
)

# 1.2. Criação do Agente Auxiliar para Google Search (Workaround ADK)

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

# Agente 1: Page Auditor Agent

page_auditor_agent = LlmAgent(
name="PageAuditorAgent",
model="gemini-2.5-flash",
instruction="""Você é o Agente 1 em um fluxo de trabalho sequencial de SEO. Sua função é auditar a página e inferir palavras-chave.

PASSO 1: Extraia a URL da mensagem do usuário.
PASSO 2: Chame a ferramenta 'firecrawl_scrape' com a URL extraída, formatos 'markdown', 'html', 'links', 'onlyMainContent': true e 'timeout': 90000.
PASSO 3: Analise os dados raspados (título, cabeçalhos, contagem de palavras, links, problemas técnicos) e resuma o conteúdo.
PASSO 4: Infira a palavra-chave primária, a intenção de busca (Search Intent) e palavras-chave secundárias de suporte.
PASSO 5: Retorne um JSON estruturado **APENAS** seguindo o schema PageAuditOutput.""",
tools=[firecrawl_toolset], # Usando a variável corrigida
output_schema=PageAuditOutput,
output_key="page_audit" # Salva o resultado no estado para o próximo agente
)

# Agente 2: Serp Analyst Agent

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
output_key="serp_analysis"

)

# Agente 3: Optimization Advisor Agent

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

================================================
FILE: .history/agent_20251024165348.py
================================================

# agent.py

import os

# Importações do ADK

from google.adk.agents import LlmAgent, SequentialAgent
from google.adk.tools import google_search
from google.adk.tools.agent_tool import AgentTool
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StdioServerParameters

# Importa os schemas Pydantic definidos em schemas.py (Linha que estava faltando!)

from .schemas import PageAuditOutput, SerpAnalysis

# --- 1. Configuração de Ferramentas (Tools) ---

# 1.1. Configuração do Firecrawl MCP Tool

# Usando o nome de variável correto: firecrawl_toolset

firecrawl_toolset = MCPToolset(
connection_params=StdioServerParameters( # USANDO 'node' e o 'mcp' explicitamente. Isso é mais robusto que 'npx'
command='node',
args=[
# O Node precisa saber onde está o módulo firecrawl-mcp
"/Users/eziolima/seo-multi-agent-project/ai_seo_audit_team/venv/lib/node_modules/firecrawl-mcp/bin/cli.js",
],
env={ # Esta chave deve ser passada. Ela já está exportada no shell.
"FIRECRAWL_API_KEY": os.getenv("FIRECRAWL_API_KEY", "")
}
),
tool_filter=['firecrawl_scrape']
)

# 1.2. Criação do Agente Auxiliar para Google Search (Workaround ADK)

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

# Agente 1: Page Auditor Agent

page_auditor_agent = LlmAgent(
name="PageAuditorAgent",
model="gemini-2.5-flash",
instruction="""Você é o Agente 1 em um fluxo de trabalho sequencial de SEO. Sua função é auditar a página e inferir palavras-chave.

PASSO 1: Extraia a URL da mensagem do usuário.
PASSO 2: Chame a ferramenta 'firecrawl_scrape' com a URL extraída, formatos 'markdown', 'html', 'links', 'onlyMainContent': true e 'timeout': 90000.
PASSO 3: Analise os dados raspados (título, cabeçalhos, contagem de palavras, links, problemas técnicos) e resuma o conteúdo.
PASSO 4: Infira a palavra-chave primária, a intenção de busca (Search Intent) e palavras-chave secundárias de suporte.
PASSO 5: Retorne um JSON estruturado **APENAS** seguindo o schema PageAuditOutput.""",
tools=[firecrawl_toolset], # Usando a variável corrigida
output_schema=PageAuditOutput,
output_key="page_audit" # Salva o resultado no estado para o próximo agente
)

# Agente 2: Serp Analyst Agent

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
output_key="serp_analysis"

)

# Agente 3: Optimization Advisor Agent

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

================================================
FILE: .history/agent_20251024165636.py
================================================

# agent.py

import os

# Importações do ADK

from google.adk.agents import LlmAgent, SequentialAgent
from google.adk.tools import google_search
from google.adk.tools.agent_tool import AgentTool
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StdioServerParameters

# Importa os schemas Pydantic definidos em schemas.py (Linha que estava faltando!)

from .schemas import PageAuditOutput, SerpAnalysis

# --- 1. Configuração de Ferramentas (Tools) ---

# 1.1. Configuração do Firecrawl MCP Tool

# Usando o nome de variável correto: firecrawl_toolset

firecrawl_toolset = MCPToolset(
connection_params=StdioServerParameters( # Usando 'node' e o caminho absoluto do script local
command='node',
args=[
# ATENÇÃO: Verifique e ajuste ESTE CAMINHO para seu Mac.
# O caminho DEVE ser: /Users/<seu_usuario>/<seu_projeto>/ai_seo_audit_team/venv/lib/node_modules/firecrawl-mcp/bin/cli.js
"/Users/eziolima/seo-multi-agent-project/ai_seo_audit_team/venv/lib/node_modules/firecrawl-mcp/bin/cli.js",
# Adicione o argumento -y para evitar prompts de confirmação de instalação
"-y"
],
env={ # O ADK pegará a chave que você definiu no shell com 'export'
"FIRECRAWL_API_KEY": os.getenv("FIRECRAWL_API_KEY", "")
}
),
tool_filter=['firecrawl_scrape']
)

# 1.2. Criação do Agente Auxiliar para Google Search (Workaround ADK)

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

# Agente 1: Page Auditor Agent

page_auditor_agent = LlmAgent(
name="PageAuditorAgent",
model="gemini-2.5-flash",
instruction="""Você é o Agente 1 em um fluxo de trabalho sequencial de SEO. Sua função é auditar a página e inferir palavras-chave.

PASSO 1: Extraia a URL da mensagem do usuário.
PASSO 2: Chame a ferramenta 'firecrawl_scrape' com a URL extraída, formatos 'markdown', 'html', 'links', 'onlyMainContent': true e 'timeout': 90000.
PASSO 3: Analise os dados raspados (título, cabeçalhos, contagem de palavras, links, problemas técnicos) e resuma o conteúdo.
PASSO 4: Infira a palavra-chave primária, a intenção de busca (Search Intent) e palavras-chave secundárias de suporte.
PASSO 5: Retorne um JSON estruturado **APENAS** seguindo o schema PageAuditOutput.""",
tools=[firecrawl_toolset], # Usando a variável corrigida
output_schema=PageAuditOutput,
output_key="page_audit" # Salva o resultado no estado para o próximo agente
)

# Agente 2: Serp Analyst Agent

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
output_key="serp_analysis"

)

# Agente 3: Optimization Advisor Agent

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

================================================
FILE: .history/agent_20251024170400.py
================================================

# agent.py

import os

# Importações do ADK

from google.adk.agents import LlmAgent, SequentialAgent
from google.adk.tools import google_search
from google.adk.tools.agent_tool import AgentTool
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StdioServerParameters

# Importa os schemas Pydantic (ASSUMIDO: O schemas.py está preenchido corretamente)

from .schemas import PageAuditOutput, SerpAnalysis

# --- 1. Configuração de Ferramentas (Tools) ---

# 1.1. Configuração do Firecrawl MCP Tool

# Usando NPX, que deve funcionar agora com o Node v22.

firecrawl_toolset = MCPToolset(
connection_params=StdioServerParameters(
command='npx',
args=[
"-y", # Auto-confirma a instalação do pacote Node (crítico para o ADK)
"firecrawl-mcp"
],
env={ # Pega a chave do .env (que deve estar preenchido)
"FIRECRAWL_API_KEY": os.getenv("FIRECRAWL_API_KEY", "")
}
),
tool_filter=['firecrawl_scrape']
)

# 1.2. Criação do Agente Auxiliar para Google Search (Workaround ADK)

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

# Agente 1: Page Auditor Agent

page_auditor_agent = LlmAgent(
name="PageAuditorAgent",
model="gemini-2.5-flash",
instruction="""Você é o Agente 1 em um fluxo de trabalho sequencial de SEO. Sua função é auditar a página e inferir palavras-chave.

PASSO 1: Extraia a URL da mensagem do usuário.
PASSO 2: Chame a ferramenta 'firecrawl_scrape' com parâmetros:

- url: <extracted URL>
- formats: ["markdown", "html", "links"]
- onlyMainContent: true
- timeout: 90000

PASSO 3: Analise dados raspados (título, headings, word count, links, technical issues).
PASSO 4: Infira a palavra-chave primária, a intenção de busca (Search Intent) e palavras-chave secundárias.
PASSO 5: Retorne um JSON estruturado **APENAS** seguindo o schema PageAuditOutput.""",
tools=[firecrawl_toolset],
output_schema=PageAuditOutput,
output_key="page_audit" # Salva o resultado para o Agente 2
)

# Agente 2: Serp Analyst Agent

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

# Agente 3: Optimization Advisor Agent

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
- **4. Recomendações Priorizadas** (Divididas em P0/P1/P2) com Racional, Impacto Estimado e Esforço Estimado.
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

================================================
FILE: .history/agent_20251024171217.py
================================================

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
PASSO 5: Retorne um JSON estruturado **APENAS** seguindo o schema PageAuditOutput.""", # Usando a ferramenta google_search para "raspar" (via snippet)
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

================================================
FILE: .history/agent_20251027163818.py
================================================

# agent.py

import os
from google.adk.agents import LlmAgent, SequentialAgent
from google.adk.tools import google_search
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StdioServerParameters

================================================
FILE: .history/agent_20251027164348.py
================================================

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

================================================
FILE: .history/agent_20251027164450.py
================================================

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
tool_filter=['firecrawl_scrape']
)

# 1 - Auditor Agent

page_auditor_agent = LlmAgent

================================================
FILE: .history/agent_20251027164616.py
================================================
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
instruction="""Você é o Agente 1 em um fluxo de trabalho sequencial de SEO.

PASSO 1: Extraia a URL exata da mensagem do usuário.
PASSO 2: Chame a ferramenta firecrawl_scrape com parâmetros:

- url: <extracted URL>
- formats: ["markdown", "html", "links"]
- onlyMainContent: true
- timeout: 90000

PASSO 3: Analise os dados raspados (título, word count, links, headings)
PASSO 4: Inferir palavras-chave primárias e secundárias, e intenção de busca.
PASSO 5: Retorne um JSON estruturado APENAS seguindo o schema PageAuditOutput.""",
tools=[firecrawl_toolset], # Usando o Firecrawl para o scrape
output_schema=PageAuditOutput,
output_key="page_audit",
disallow_transfer_to_parent=True,
disallow_transfer_to_peers=True
)

# Agente 2: Serp Analyst Agent (USA google_search DIRETAMENTE)

serp_analyst_agent = LlmAgent(
name="SerpeAnalystAgent",
model="gemini-2.5-flash", # MANTÉM Flash para performance/custo
instruction="""Você é o Agente 2. Sua função é analisar a concorrência na SERP.

PASSO 1: Leia a palavra-chave primária de state['page_audit']['target_keywords']['primary_keyword'].
PASSO 2: Chame a ferramenta 'google_search' com a palavra-chave primária.
PASSO 3: Analise os resultados de busca (rank, título, URL, snippet, content_type) dos top 10 concorrentes.
PASSO 4: Identifique padrões nos títulos, formatos de conteúdo dominantes e temas chave abordados pelos concorrentes.
PASSO 5: Retorne um JSON estruturado APENAS seguindo o schema SerpAnalysis.""",
tools=[google_search], # INJEÇÃO DIRETA DA FERRAMENTA! (KISS aplicado)
output_schema=SerpAnalysis,
output_key="serp_analysis",
disallow_transfer_to_parent=True,
disallow_transfer_to_peers=True
)

# Agente 3: Optimization Advisor Agent (USA PRO para raciocínio superior e relatório)

optimization_advisor_agent = LlmAgent(
name="OptimizationAdvisorAgent",
model="gemini-2.5-pro", # MODELO PRO PARA QUALIDADE DO RELATÓRIO FINAL
instruction="""Você é o Agente 3 e o especialista final no fluxo de trabalho. Seu objetivo é consolidar todas as informações em um relatório de SEO profissional, acionável e bem formatado.

PASSO 1: Revise os dados de state['page_audit'] e state['serp_analysis'].
PASSO 2: Crie um relatório COMPLETO no formato Markdown, contendo:

- **# Relatório de Auditoria SEO**
- **Resumo Executivo**
- **1. Achados Técnicos e On-Page** - **2. Análise de Palavra-Chave** - **3. Análise Competitiva SERP** - **4. Recomendações Priorizadas** (P0: Crítico, P1: Alto Impacto, P2: Melhoria) com Racional, Impacto Estimado e Esforço Estimado.
- **5. Próximas Etapas**

PASSO 3: Retorne APENAS o conteúdo Markdown (sem JSON, sem preâmbulo).""",
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

================================================
FILE: .history/agent_20251027164939.py
================================================
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

# Agente 2: Serp Analyst Agent (USA google_search DIRETAMENTE)

serp_analyst_agent = LlmAgent(
name="SerpeAnalystAgent",
model="gemini-2.5-flash", # MANTÉM Flash para performance/custo
instruction="""Você é o Agente 2. Sua função é analisar a concorrência na SERP.

PASSO 1: Leia a palavra-chave primária de state['page_audit']['target_keywords']['primary_keyword'].
PASSO 2: Chame a ferramenta 'google_search' com a palavra-chave primária.
PASSO 3: Analise os resultados de busca (rank, título, URL, snippet, content_type) dos top 10 concorrentes.
PASSO 4: Identifique padrões nos títulos, formatos de conteúdo dominantes e temas chave abordados pelos concorrentes.
PASSO 5: Retorne um JSON estruturado APENAS seguindo o schema SerpAnalysis.""",
tools=[google_search], # INJEÇÃO DIRETA DA FERRAMENTA! (KISS aplicado)
output_schema=SerpAnalysis,
output_key="serp_analysis",
disallow_transfer_to_parent=True,
disallow_transfer_to_peers=True
)

# Agente 3: Optimization Advisor Agent (USA PRO para raciocínio superior e relatório)

optimization_advisor_agent = LlmAgent(
name="OptimizationAdvisorAgent",
model="gemini-2.5-pro", # MODELO PRO PARA QUALIDADE DO RELATÓRIO FINAL
instruction="""Você é o Agente 3 e o especialista final no fluxo de trabalho. Seu objetivo é consolidar todas as informações em um relatório de SEO profissional, acionável e bem formatado.

PASSO 1: Revise os dados de state['page_audit'] e state['serp_analysis'].
PASSO 2: Crie um relatório COMPLETO no formato Markdown, contendo:

- **# Relatório de Auditoria SEO**
- **Resumo Executivo**
- **1. Achados Técnicos e On-Page** - **2. Análise de Palavra-Chave** - **3. Análise Competitiva SERP** - **4. Recomendações Priorizadas** (P0: Crítico, P1: Alto Impacto, P2: Melhoria) com Racional, Impacto Estimado e Esforço Estimado.
- **5. Próximas Etapas**

PASSO 3: Retorne APENAS o conteúdo Markdown (sem JSON, sem preâmbulo).""",
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

================================================
FILE: .history/agent_20251027165009.py
================================================
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

# Agente 3: Optimization Advisor Agent (USA PRO para raciocínio superior e relatório)

optimization_advisor_agent = LlmAgent(
name="OptimizationAdvisorAgent",
model="gemini-2.5-pro", # MODELO PRO PARA QUALIDADE DO RELATÓRIO FINAL
instruction="""Você é o Agente 3 e o especialista final no fluxo de trabalho. Seu objetivo é consolidar todas as informações em um relatório de SEO profissional, acionável e bem formatado.

PASSO 1: Revise os dados de state['page_audit'] e state['serp_analysis'].
PASSO 2: Crie um relatório COMPLETO no formato Markdown, contendo:

- **# Relatório de Auditoria SEO**
- **Resumo Executivo**
- **1. Achados Técnicos e On-Page** - **2. Análise de Palavra-Chave** - **3. Análise Competitiva SERP** - **4. Recomendações Priorizadas** (P0: Crítico, P1: Alto Impacto, P2: Melhoria) com Racional, Impacto Estimado e Esforço Estimado.
- **5. Próximas Etapas**

PASSO 3: Retorne APENAS o conteúdo Markdown (sem JSON, sem preâmbulo).""",
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

================================================
FILE: .history/agent_20251027165059.py
================================================
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

================================================
FILE: .history/agent_20251027165316.py
================================================
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

# Orquestration of workflow

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

================================================
FILE: .history/agent_20251027165413.py
================================================
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

================================================
FILE: .history/agent_20251027165415.py
================================================
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

================================================
FILE: .history/agent_20251027174248.py
================================================
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
model="gemini-2.5-pro",
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

================================================
FILE: .history/agent_20251027174727.py
================================================
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
tool_invocation_timeout=60.0
)

# 1: Page Auditor Agent

page_auditor_agent = LlmAgent(
name="PageAuditorAgent",
model="gemini-2.5-pro",
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

================================================
FILE: .history/agent_20251027174919.py
================================================
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
tool_filter=['firecrawl_scrape'],
tool_invocation_timeout=60.0 #
)

# 1: Page Auditor Agent

page_auditor_agent = LlmAgent(
name="PageAuditorAgent",
model="gemini-2.5-pro",
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

================================================
FILE: .history/agent_20251027175734.py
================================================
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
tool_invocation_timeout=60.0 #
)

# 1: Page Auditor Agent

page_auditor_agent = LlmAgent(
name="PageAuditorAgent",
model="gemini-2.5-pro",
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

================================================
FILE: .history/agent_20251027175800.py
================================================
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
tool_invocation_timeout=60.0 #
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

================================================
FILE: .history/agent_20251027175936.py
================================================
import os
from google.adk.agents import LlmAgent, SequentialAgent
from google.adk.tools import google_search
from .schemas import PageAuditOutput, SerpAnalysis

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

================================================
FILE: .history/agent_20251027175942.py
================================================
import os
from google.adk.agents import LlmAgent, SequentialAgent
from google.adk.tools import google_search
from .schemas import PageAuditOutput, SerpAnalysis

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
tools=[google_search],
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

================================================
FILE: .history/agent_20251027175948.py
================================================
import os
from google.adk.agents import LlmAgent, SequentialAgent
from google.adk.tools import google_search
from .schemas import PageAuditOutput, SerpAnalysis

# 1: Page Auditor Agent

page_auditor_agent = LlmAgent(
name="PageAuditorAgent",
model="gemini-2.5-pro",
instruction="""You are Agent 1 in a sequential SEO workflow. Your task is to audit the page using its SERP snippet and infer keywords.

STEP 1: Extract the exact URL from the user's message (e.g., 'https://example.com/').
STEP 2: **Call the 'google_search' tool** with the extracted URL as the query, limiting to 1 result. This provides the title and the snippet (content summary).
STEP 3: Analyze the Title and Snippet to infer: primary keyword, search intent, and secondary keywords.
STEP 4: For fields like link_counts and word_count, provide reasonable estimates based on the snippet length or return 0, as full scraping is unavailable due to performance constraints.
STEP 5: Fill the PageAuditOutput JSON with the inferred data.
STEP 6: Return ONLY the structured JSON matching the PageAuditOutput schema.""",
tools=[google_search],
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

================================================
FILE: .history/agent_20251027180328.py
================================================
import os
from google.adk.agents import LlmAgent, SequentialAgent
from google.adk.tools import google_search
from .schemas import PageAuditOutput, SerpAnalysis

# 1: Page Auditor Agent

page_auditor_agent = LlmAgent(
name="PageAuditorAgent",
model="gemini-2.5-flash",
instruction="""You are Agent 1 in a sequential SEO workflow. Your task is to audit the page using its SERP snippet and infer keywords.

STEP 1: Extract the exact URL from the user's message (e.g., 'https://example.com/').
STEP 2: **Call the 'google_search' tool** with the extracted URL as the query, limiting to 1 result. This provides the title and the snippet (content summary).
STEP 3: Analyze the Title and Snippet to infer: primary keyword, search intent, and secondary keywords.
STEP 4: For fields like link_counts and word_count, provide reasonable estimates based on the snippet length or return 0, as full scraping is unavailable due to performance constraints.
STEP 5: Fill the PageAuditOutput JSON with the inferred data.
STEP 6: Return ONLY the structured JSON matching the PageAuditOutput schema.""",
tools=[google_search],
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

#3: Optimization Advisor Agent
optimization_advisor_agent = LlmAgent(
name="OptimizationAdvisorAgent",
model="gemini-2.5-flash",
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

================================================
FILE: .history/agent_20251027181027.py
================================================
import os
from google.adk.agents import LlmAgent, SequentialAgent

from .schemas import PageAuditOutput, SerpAnalysis

# 1: Page Auditor Agent

page_auditor_agent = LlmAgent(
name="PageAuditorAgent",
model="gemini-2.5-flash",
instruction="""You are Agent 1 in a sequential SEO workflow. Your task is to audit the page using its SERP snippet and infer keywords.

STEP 1: Extract the exact URL from the user's message (e.g., 'https://example.com/').
STEP 2: **Call the 'google_search' tool** with the extracted URL as the query, limiting to 1 result. This provides the title and the snippet (content summary).
STEP 3: Analyze the Title and Snippet to infer: primary keyword, search intent, and secondary keywords.
STEP 4: For fields like link_counts and word_count, provide reasonable estimates based on the snippet length or return 0, as full scraping is unavailable due to performance constraints.
STEP 5: Fill the PageAuditOutput JSON with the inferred data.
STEP 6: Return ONLY the structured JSON matching the PageAuditOutput schema.""",
tools=[google_search],
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

#3: Optimization Advisor Agent
optimization_advisor_agent = LlmAgent(
name="OptimizationAdvisorAgent",
model="gemini-2.5-flash",
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

================================================
FILE: .history/agent_20251027181137.py
================================================

# agent.py

import os
from google.adk.agents import LlmAgent, SequentialAgent

# REMOVEMOS a importação 'from google.adk.tools import google_search'

from .schemas import PageAuditOutput, SerpAnalysis

# 1: Page Auditor Agent (RACIOCÍNIO PURO)

page_auditor_agent = LlmAgent(
name="PageAuditorAgent",
model="gemini-2.5-flash",
instruction="""You are Agent 1 in a sequential SEO workflow. Your task is to perform a _simulated_ on-page audit and keyword inference based ONLY on the URL provided in the user's message.

STEP 1: Infer the Title Tag, Content Summary, and primary/secondary keywords directly from the URL and its implied topic.
STEP 2: For technical fields (link_counts, word_count, findings), provide _reasonable estimates_ or simplified assumptions (e.g., 'word_count': 500, 'link_counts': {'internal': 10, 'external': 5}) to simulate an audit.
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
STEP 2: _Simulate_ the competitive SERP for that keyword, inferring: top competitor titles, common content formats, and key themes/angles used by competitors in the SERP.
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

================================================
FILE: .history/agent_20251027182618.py
================================================

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
instruction="""You are Agent 1 in a sequential SEO workflow. Your task is to perform a _simulated_ on-page audit and keyword inference based ONLY on the URL provided in the user's message.

STEP 1: Infer the Title Tag, Content Summary, and primary/secondary keywords directly from the URL and its implied topic.
STEP 2: For technical fields (link_counts, word_count, findings), provide _reasonable estimates_ or simplified assumptions (e.g., 'word_count': 500, 'link_counts': {'internal': 10, 'external': 5}) to simulate an audit.
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
STEP 2: _Simulate_ the competitive SERP for that keyword, inferring: top competitor titles, common content formats, and key themes/angles used by competitors in the SERP.
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
instruction="""You are Agent 3 in the sequential workflow, specialized in CRO and UX. Your task is to perform a _simulated_ analysis of the page's conversion potential, usabilty, and funnel based on the inferred data from state['page_audit'].

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

================================================
FILE: .history/app_runner_20251031120621.py
================================================

================================================
FILE: .history/app_runner_20251031120646.py
================================================
from pydantic import BaseModel, Field
from enum import Enum
from typing import List, Optional
import docx
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.colors import black
from reportlab.lib.enums import TA_CENTER
from io import BytesIO
import markdown
import os

# --- CONFIGURAÇÕES DE DADOS (Para comunicação com FastAPI) ---

class ReportFormat(str, Enum):
"""Define os formatos de relatório disponíveis."""
WORD = "word"
PDF = "pdf"
MARKDOWN = "markdown"

class ReportGenerationRequest(BaseModel):
"""Schema para a requisição da API de geração de relatório."""
url: str
report_format: ReportFormat = Field(
default=ReportFormat.PDF,
description="Formato desejado para o relatório"
)
language: str = Field(
default="pt-BR",
description="Idioma do relatório (ajusta o Agente 4)"
)

# --- CLASSE DE ESTILO PARA PDF (ReportLab) ---

class ReportStyleConfig:
"""Configurações de estilo para relatórios PDF (ReportLab)."""

    @staticmethod
    def get_pdf_styles():
        """Configura estilos de parágrafo e cabeçalho."""
        styles = getSampleStyleSheet()

        styles.add(ParagraphStyle(
            name='H1Style',
            parent=styles['Title'],
            fontName='Helvetica-Bold',
            fontSize=18,
            textColor=black,
            alignment=TA_CENTER,
            spaceAfter=18
        ))

        styles.add(ParagraphStyle(
            name='H2Style',
            parent=styles['Heading2'],
            fontName='Helvetica-Bold',
            fontSize=14,
            textColor=black,
            spaceAfter=6
        ))

        styles.add(ParagraphStyle(
            name='NormalStyle',
            parent=styles['Normal'],
            fontName='Helvetica',
            fontSize=10,
            textColor=black,
            leading=12,
            spaceAfter=8
        ))

        return styles

# --- CLASSE PRINCIPAL DE GERAÇÃO DE ARQUIVOS (SRP) ---

class ReportGenerator:
"""Responsável por converter conteúdo Markdown em arquivos binários."""

    @staticmethod
    def generate_report(content: str, format: ReportFormat, url: str) -> BytesIO:
        """
        Gera relatório no formato especificado (PDF, DOCX ou MARKDOWN),
        retornando um objeto BytesIO para o FastAPI.
        """
        if format == ReportFormat.WORD:
            return ReportGenerator._generate_word_report(content)

        elif format == ReportFormat.PDF:
            return ReportGenerator._generate_pdf_report(content)

        elif format == ReportFormat.MARKDOWN:
            return BytesIO(content.encode('utf-8'))

        raise ValueError(f"Formato {format.value} não suportado.")

    @staticmethod
    def _generate_word_report(content: str) -> BytesIO:
        """Gera relatório em Word (.docx)."""
        doc = docx.Document()
        doc.add_heading('Relatório de Auditoria Estratégica Digital', 0)

        # Converte Markdown para parágrafos simples
        lines = content.split('\n')
        for line in lines:
            line = line.strip()
            if line.startswith('# '):
                doc.add_heading(line.replace('# ', ''), level=1)
            elif line.startswith('## '):
                doc.add_heading(line.replace('## ', ''), level=2)
            elif line:
                doc.add_paragraph(line)

        file_stream = BytesIO()
        doc.save(file_stream)
        file_stream.seek(0)
        return file_stream

    @staticmethod
    def _generate_pdf_report(content: str) -> BytesIO:
        """Gera relatório em PDF (ReportLab)."""
        file_stream = BytesIO()
        doc = SimpleDocTemplate(file_stream, pagesize=letter)
        styles = ReportStyleConfig.get_pdf_styles()
        elements = []

        # Processa o Markdown linha por linha para formatação PDF
        lines = content.split('\n')
        for line in lines:
            line = line.strip()
            if line.startswith('# '):
                elements.append(Paragraph(line.replace('# ', ''), styles['H1Style']))
            elif line.startswith('## '):
                elements.append(Paragraph(line.replace('## ', ''), styles['H2Style']))
            elif line.startswith('- '):
                # Formatação de lista simples
                elements.append(Paragraph(f'&bull; {line.replace("- ", "").strip()}', styles['NormalStyle']))
            elif line:
                elements.append(Paragraph(line, styles['NormalStyle']))

            elements.append(Spacer(1, 6))

        doc.build(elements)
        file_stream.seek(0)
        return file_stream

================================================
FILE: .history/app_runner_20251031120726.py
================================================
from pydantic import BaseModel, Field
from enum import Enum
from typing import List, Optional
import docx
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.colors import black
from reportlab.lib.enums import TA_CENTER
from io import BytesIO
import markdown
import os

# --- CONFIGURAÇÕES DE DADOS (Para comunicação com FastAPI) ---

class ReportFormat(str, Enum):
"""Define os formatos de relatório disponíveis."""
WORD = "word"
PDF = "pdf"
MARKDOWN = "markdown"

class ReportGenerationRequest(BaseModel):
"""Schema para a requisição da API de geração de relatório."""
url: str
report_format: ReportFormat = Field(
default=ReportFormat.PDF,
description="Formato desejado para o relatório"
)
language: str = Field(
default="pt-BR",
description="Idioma do relatório (ajusta o Agente 4)"
)

# --- CLASSE DE ESTILO PARA PDF (ReportLab) ---

class ReportStyleConfig:
"""Configurações de estilo para relatórios PDF (ReportLab)."""

    @staticmethod
    def get_pdf_styles():
        """Configura estilos de parágrafo e cabeçalho."""
        styles = getSampleStyleSheet()

        styles.add(ParagraphStyle(
            name='H1Style',
            parent=styles['Title'],
            fontName='Helvetica-Bold',
            fontSize=18,
            textColor=black,
            alignment=TA_CENTER,
            spaceAfter=18
        ))

        styles.add(ParagraphStyle(
            name='H2Style',
            parent=styles['Heading2'],
            fontName='Helvetica-Bold',
            fontSize=14,
            textColor=black,
            spaceAfter=6
        ))

        styles.add(ParagraphStyle(
            name='NormalStyle',
            parent=styles['Normal'],
            fontName='Helvetica',
            fontSize=10,
            textColor=black,
            leading=12,
            spaceAfter=8
        ))

        return styles

# --- CLASSE PRINCIPAL DE GERAÇÃO DE ARQUIVOS (SRP) ---

class ReportGenerator:
"""Responsável por converter conteúdo Markdown em arquivos binários."""

    @staticmethod
    def generate_report(content: str, format: ReportFormat, url: str) -> BytesIO:
        """
        Gera relatório no formato especificado (PDF, DOCX ou MARKDOWN),
        retornando um objeto BytesIO para o FastAPI.
        """
        if format == ReportFormat.WORD:
            return ReportGenerator._generate_word_report(content)

        elif format == ReportFormat.PDF:
            return ReportGenerator._generate_pdf_report(content)

        elif format == ReportFormat.MARKDOWN:
            return BytesIO(content.encode('utf-8'))

        raise ValueError(f"Formato {format.value} não suportado.")

    @staticmethod
    def _generate_word_report(content: str) -> BytesIO:
        """Gera relatório em Word (.docx)."""
        doc = docx.Document()
        doc.add_heading('Relatório de Auditoria Estratégica Digital', 0)

        # Converte Markdown para parágrafos simples
        lines = content.split('\n')
        for line in lines:
            line = line.strip()
            if line.startswith('# '):
                doc.add_heading(line.replace('# ', ''), level=1)
            elif line.startswith('## '):
                doc.add_heading(line.replace('## ', ''), level=2)
            elif line:
                doc.add_paragraph(line)

        file_stream = BytesIO()
        doc.save(file_stream)
        file_stream.seek(0)
        return file_stream

    @staticmethod
    def _generate_pdf_report(content: str) -> BytesIO:
        """Gera relatório em PDF (ReportLab)."""
        file_stream = BytesIO()
        doc = SimpleDocTemplate(file_stream, pagesize=letter)
        styles = ReportStyleConfig.get_pdf_styles()
        elements = []

        # Processa o Markdown linha por linha para formatação PDF
        lines = content.split('\n')
        for line in lines:
            line = line.strip()
            if line.startswith('# '):
                elements.append(Paragraph(line.replace('# ', ''), styles['H1Style']))
            elif line.startswith('## '):
                elements.append(Paragraph(line.replace('## ', ''), styles['H2Style']))
            elif line.startswith('- '):
                # Formatação de lista simples
                elements.append(Paragraph(f'&bull; {line.replace("- ", "").strip()}', styles['NormalStyle']))
            elif line:
                elements.append(Paragraph(line, styles['NormalStyle']))

            elements.append(Spacer(1, 6))

        doc.build(elements)
        file_stream.seek(0)
        return file_stream

================================================
FILE: .history/report_generator_20251031120158.py
================================================

================================================
FILE: .history/report_generator_20251031120316.py
================================================

from pydantic import BaseModel, Field
from enum import Enum
from typing import List, Optional
import docx
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.colors import black
from reportlab.lib.enums import TA_CENTER
from io import BytesIO
import markdown
import os

# --- CONFIGURAÇÕES DE DADOS (Padrão Pydantic/Enum) ---

class ReportFormat(str, Enum):
"""Enum para formatos de relatório"""
WORD = "word"
PDF = "pdf"
MARKDOWN = "markdown"

class ReportGenerationRequest(BaseModel):
"""Schema para a requisição da API de geração de relatório."""
url: str
report_format: ReportFormat = Field(
default=ReportFormat.PDF,
description="Formato desejado para o relatório"
)
language: str = Field(
default="pt-BR",
description="Idioma do relatório"
)

# --- CLASSE DE ESTILO PARA PDF (ReportLab) ---

class ReportStyleConfig:
"""Configurações de estilo para geração de relatórios PDF (ReportLab)."""

    @staticmethod
    def get_pdf_styles():
        """Configura estilos personalizados para PDF."""
        styles = getSampleStyleSheet()

        styles.add(ParagraphStyle(
            name='H1Style',
            parent=styles['Title'],
            fontName='Helvetica-Bold',
            fontSize=18,
            textColor=black,
            alignment=TA_CENTER,
            spaceAfter=18
        ))

        styles.add(ParagraphStyle(
            name='H2Style',
            parent=styles['Heading2'],
            fontName='Helvetica-Bold',
            fontSize=14,
            textColor=black,
            spaceAfter=6
        ))

        styles.add(ParagraphStyle(
            name='NormalStyle',
            parent=styles['Normal'],
            fontName='Helvetica',
            fontSize=10,
            textColor=black,
            leading=12,
            spaceAfter=8
        ))

        return styles

# --- CLASSE PRINCIPAL DE GERAÇÃO DE ARQUIVOS (SRP) ---

class ReportGenerator:
"""Responsável por converter conteúdo Markdown em arquivos binários."""

    @staticmethod
    def generate_report(content: str, format: ReportFormat, url: str) -> BytesIO:
        """
        Gera relatório no formato especificado, retornando um objeto BytesIO.
        """
        if format == ReportFormat.WORD:
            return ReportGenerator._generate_word_report(content)

        elif format == ReportFormat.PDF:
            return ReportGenerator._generate_pdf_report(content)

        elif format == ReportFormat.MARKDOWN:
            return BytesIO(content.encode('utf-8'))

        raise ValueError(f"Formato {format.value} não suportado.")

    @staticmethod
    def _generate_word_report(content: str) -> BytesIO:
        """Gera relatório em Word (.docx)."""
        doc = docx.Document()
        doc.add_heading('Relatório de Auditoria Estratégica Digital', 0)

        # Converte Markdown para parágrafos simples
        lines = content.split('\n')
        for line in lines:
            line = line.strip()
            if line.startswith('# '):
                doc.add_heading(line.replace('# ', ''), level=1)
            elif line.startswith('## '):
                doc.add_heading(line.replace('## ', ''), level=2)
            elif line:
                doc.add_paragraph(line)

        file_stream = BytesIO()
        doc.save(file_stream)
        file_stream.seek(0)
        return file_stream

    @staticmethod
    def _generate_pdf_report(content: str) -> BytesIO:
        """Gera relatório em PDF (ReportLab)."""
        file_stream = BytesIO()
        doc = SimpleDocTemplate(file_stream, pagesize=letter)
        styles = ReportStyleConfig.get_pdf_styles()
        elements = []

        lines = content.split('\n')
        for line in lines:
            line = line.strip()
            if line.startswith('# '):
                elements.append(Paragraph(line.replace('# ', ''), styles['H1Style']))
            elif line.startswith('## '):
                elements.append(Paragraph(line.replace('## ', ''), styles['H2Style']))
            elif line.startswith('- '):
                elements.append(Paragraph(f'&bull; {line.replace("- ", "").strip()}', styles['NormalStyle']))
            elif line:
                elements.append(Paragraph(line, styles['NormalStyle']))

            elements.append(Spacer(1, 6))

        doc.build(elements)
        file_stream.seek(0)
        return file_stream

================================================
FILE: .history/requirements_20251024111445.txt
================================================

================================================
FILE: .history/requirements_20251024111456.txt
================================================
google-adk
pydantic

================================================
FILE: .history/requirements_20251031120125.txt
================================================

# requirements.txt

google-adk
pydantic
python-docx
reportlab
markdown
fastapi
uvicorn
python-multipart

================================================
FILE: .history/schemas_20251024134800.py
================================================

================================================
FILE: .history/schemas_20251024135043.py
================================================
from pydantic import BaseModel, Field
from typing import List, Optional

#-- Estruturas auxiliares para o Page Auditor ---
class LinkCounts(BaseModel);
internal: int = Field(..., description="Number of Internal links found on the ")

================================================
FILE: .history/schemas_20251024135053.py
================================================
from pydantic import BaseModel, Field
from typing import List, Optional

#-- Estruturas auxiliares para o Page Auditor ---
class LinkCounts(BaseModel);
internal: int = Field(..., description="Number of Internal links found on the page")

================================================
FILE: .history/schemas_20251024135247.py
================================================
from pydantic import BaseModel, Field
from typing import List, Optional

#-- Estruturas auxiliares para o Page Auditor ---
class LinkCounts(BaseModel):
internal: int = Field(..., description="Number of Internal links found on the page")
external: int = Field(..., description="Number of External links found on the page")

class HeadingItem(BaseModel):
internal int = Field(..., description="Number of internal links found on the page")

================================================
FILE: .history/schemas_20251024135346.py
================================================
from pydantic import BaseModel, Field
from typing import List, Optional

#-- Estruturas auxiliares para o Page Auditor ---
class LinkCounts(BaseModel):
internal: int = Field(..., description="Number of Internal links found on the page")
external: int = Field(..., description="Number of External links found on the page")

class HeadingItem(BaseModel):
internal: int = Field(..., description="Number of internal links found on the page")
external: int = Field(..., description="Number of external links found on the page")

================================================
FILE: .history/schemas_20251024135430.py
================================================
from pydantic import BaseModel, Field
from typing import List, Optional

#-- Estruturas auxiliares para o Page Auditor ---
class LinkCounts(BaseModel):
internal: int = Field(..., description="Number of Internal links found on the page")
external: int = Field(..., description="Number of External links found on the page")

class HeadingItem(BaseModel):
internal: int = Field(..., description="Number of internal links found on the page")
external: int = Field(..., description="Number of external links found on the page")

================================================
FILE: .history/schemas_20251024135518.py
================================================
from pydantic import BaseModel, Field
from typing import List, Optional

class LinkCounts(BaseModel):
internal: int = Field(..., description="Number of Internal links found on the page")
external: int = Field(..., description="Number of External links found on the page")

class HeadingItem(BaseModel):
internal: int = Field(..., description="Number of internal links found on the page")
external: int = Field(..., description="Number of external links found on the page")

================================================
FILE: .history/schemas_20251024140631.py
================================================
from pydantic import BaseModel, Field
from typing import List, Optional

class LinkCounts(BaseModel):
internal: int = Field(..., description="Number of Internal links found on the page")
external: int = Field(..., description="Number of External links found on the page")

class HeadingItem(BaseModel):
internal: int = Field(..., description="Number of internal links found on the page")
external: int = Field(..., description="Number of external links found on the page")

class HeadingItem(BaseModel);

================================================
FILE: .history/schemas_20251024140821.py
================================================
from pydantic import BaseModel, Field
from typing import List, Optional

class LinkCounts(BaseModel):
internal: int = Field(..., description="Number of Internal links found on the page")
external: int = Field(..., description="Number of External links found on the page")

class HeadingItem(BaseModel):
internal: int = Field(..., description="Number of internal links found on the page")
external: int = Field(..., description="Number of external links found on the page")

class HeadingItem(BaseModel):
tag: str = Field(..., description="Heading tag such as h1, h2, h3.")
text: str = Field(..., description="Text content of the heading.")

class TargetKeywords(BaseModel):

================================================
FILE: .history/schemas_20251024140932.py
================================================
from pydantic import BaseModel, Field
from typing import List, Optional

class LinkCounts(BaseModel):
internal: int = Field(..., description="Number of Internal links found on the page")
external: int = Field(..., description="Number of External links found on the page")

class HeadingItem(BaseModel):
internal: int = Field(..., description="Number of internal links found on the page")
external: int = Field(..., description="Number of external links found on the page")

class HeadingItem(BaseModel):
tag: str = Field(..., description="Heading tag such as h1, h2, h3.")
text: str = Field(..., description="Text content of the heading.")

class TargetKeywords(BaseModel):
primary_keyword: str = Field(..., description="The main keyword the page is optional")

================================================
FILE: .history/schemas_20251024140944.py
================================================
from pydantic import BaseModel, Field
from typing import List, Optional

class LinkCounts(BaseModel):
internal: int = Field(..., description="Number of Internal links found on the page")
external: int = Field(..., description="Number of External links found on the page")

class HeadingItem(BaseModel):
internal: int = Field(..., description="Number of internal links found on the page")
external: int = Field(..., description="Number of external links found on the page")

class HeadingItem(BaseModel):
tag: str = Field(..., description="Heading tag such as h1, h2, h3.")
text: str = Field(..., description="Text content of the heading.")

class TargetKeywords(BaseModel):
primary_keyword: str = Field(..., description="The main keyword the page is optional for.")

================================================
FILE: .history/schemas_20251024141028.py
================================================
from pydantic import BaseModel, Field
from typing import List, Optional

class LinkCounts(BaseModel):
internal: int = Field(..., description="Number of Internal links found on the page")
external: int = Field(..., description="Number of External links found on the page")

class HeadingItem(BaseModel):
internal: int = Field(..., description="Number of internal links found on the page")
external: int = Field(..., description="Number of external links found on the page")

class HeadingItem(BaseModel):
tag: str = Field(..., description="Heading tag such as h1, h2, h3.")
text: str = Field(..., description="Text content of the heading.")

class TargetKeywords(BaseModel):
primary_keyword: str = Field(..., description="The main keyword the page is optimized for.")

================================================
FILE: .history/schemas_20251024141108.py
================================================
from pydantic import BaseModel, Field
from typing import List, Optional

class LinkCounts(BaseModel):
internal: int = Field(..., description="Number of Internal links found on the page")
external: int = Field(..., description="Number of External links found on the page")

class HeadingItem(BaseModel):
internal: int = Field(..., description="Number of internal links found on the page")
external: int = Field(..., description="Number of external links found on the page")

class HeadingItem(BaseModel):
tag: str = Field(..., description="Heading tag such as h1, h2, h3.")
text: str = Field(..., description="Text content of the heading.")

class TargetKeywords(BaseModel):
primary_keyword: str = Field(..., description="The main keyword the page is optimized for.")
search_intent: str = Field(..., description="Inferred search intent (e.g., )")

================================================
FILE: .history/schemas_20251024141141.py
================================================
from pydantic import BaseModel, Field
from typing import List, Optional

class LinkCounts(BaseModel):
internal: int = Field(..., description="Number of Internal links found on the page")
external: int = Field(..., description="Number of External links found on the page")

class HeadingItem(BaseModel):
internal: int = Field(..., description="Number of internal links found on the page")
external: int = Field(..., description="Number of external links found on the page")

class HeadingItem(BaseModel):
tag: str = Field(..., description="Heading tag such as h1, h2, h3.")
text: str = Field(..., description="Text content of the heading.")

class TargetKeywords(BaseModel):
primary_keyword: str = Field(..., description="The main keyword the page is optimized for.")
search_intent: str = Field(..., description="Inferred search intent (e.g., informational, commercial, transactional).")

================================================
FILE: .history/schemas_20251024141225.py
================================================
from pydantic import BaseModel, Field
from typing import List, Optional

class LinkCounts(BaseModel):
internal: int = Field(..., description="Number of Internal links found on the page")
external: int = Field(..., description="Number of External links found on the page")

class HeadingItem(BaseModel):
internal: int = Field(..., description="Number of internal links found on the page")
external: int = Field(..., description="Number of external links found on the page")

class HeadingItem(BaseModel):
tag: str = Field(..., description="Heading tag such as h1, h2, h3.")
text: str = Field(..., description="Text content of the heading.")

class TargetKeywords(BaseModel):
primary_keyword: str = Field(..., description="The main keyword the page is optimized for.")
search_intent: str = Field(..., description="Inferred search intent (e.g., informational, commercial, transactional).")
secondary_keyword: List[str] = Field(..., description="A list supporting, ")

================================================
FILE: .history/schemas_20251024141331.py
================================================
from pydantic import BaseModel, Field
from typing import List, Optional

class LinkCounts(BaseModel):
internal: int = Field(..., description="Number of Internal links found on the page")
external: int = Field(..., description="Number of External links found on the page")

class HeadingItem(BaseModel):
internal: int = Field(..., description="Number of internal links found on the page")
external: int = Field(..., description="Number of external links found on the page")

class HeadingItem(BaseModel):
tag: str = Field(..., description="Heading tag such as h1, h2, h3.")
text: str = Field(..., description="Text content of the heading.")

class TargetKeywords(BaseModel):
primary_keyword: str = Field(..., description="The main keyword the page is optimized for.")
search_intent: str = Field(..., description="Inferred search intent (e.g., informational, commercial, transactional).")
secondary_keyword: List[str] = Field(..., description="A list of supporting, long-tail, or related keywords.")

================================================
FILE: .history/schemas_20251024141736.py
================================================
from pydantic import BaseModel, Field
from typing import List, Optional

class LinkCounts(BaseModel):
internal: int = Field(..., description="Number of Internal links found on the page")
external: int = Field(..., description="Number of External links found on the page")

class HeadingItem(BaseModel):
internal: int = Field(..., description="Number of internal links found on the page")
external: int = Field(..., description="Number of external links found on the page")

class HeadingItem(BaseModel):
tag: str = Field(..., description="Heading tag such as h1, h2, h3.")
text: str = Field(..., description="Text content of the heading.")

class TargetKeywords(BaseModel):
primary_keyword: str = Field(..., description="The main keyword the page is optimized for.")
search_intent: str = Field(..., description="Inferred search intent (e.g., informational, commercial, transactional).")
secondary_keyword: List[str] = Field(..., description="A list of supporting, long-tail, or related keywords.")

class AuditResults(BaseModel):
title_tag: str
meta_description: str
primary_heading: str
secondary_headings: List[HeadingItem]
word

================================================
FILE: .history/schemas_20251024141759.py
================================================
from pydantic import BaseModel, Field
from typing import List, Optional

class LinkCounts(BaseModel):
internal: int = Field(..., description="Number of Internal links found on the page")
external: int = Field(..., description="Number of External links found on the page")

class HeadingItem(BaseModel):
internal: int = Field(..., description="Number of internal links found on the page")
external: int = Field(..., description="Number of external links found on the page")

class HeadingItem(BaseModel):
tag: str = Field(..., description="Heading tag such as h1, h2, h3.")
text: str = Field(..., description="Text content of the heading.")

class TargetKeywords(BaseModel):
primary_keyword: str = Field(..., description="The main keyword the page is optimized for.")
search_intent: str = Field(..., description="Inferred search intent (e.g., informational, commercial, transactional).")
secondary_keyword: List[str] = Field(..., description="A list of supporting, long-tail, or related keywords.")

class AuditResults(BaseModel):
title_tag: str
meta_description: str
primary_heading: str
secondary_headings: List[HeadingItem]
word_count: Optional[int]

================================================
FILE: .history/schemas_20251024141849.py
================================================
from pydantic import BaseModel, Field
from typing import List, Optional

class LinkCounts(BaseModel):
internal: int = Field(..., description="Number of Internal links found on the page")
external: int = Field(..., description="Number of External links found on the page")

class HeadingItem(BaseModel):
internal: int = Field(..., description="Number of internal links found on the page")
external: int = Field(..., description="Number of external links found on the page")

class HeadingItem(BaseModel):
tag: str = Field(..., description="Heading tag such as h1, h2, h3.")
text: str = Field(..., description="Text content of the heading.")

class TargetKeywords(BaseModel):
primary_keyword: str = Field(..., description="The main keyword the page is optimized for.")
search_intent: str = Field(..., description="Inferred search intent (e.g., informational, commercial, transactional).")
secondary_keyword: List[str] = Field(..., description="A list of supporting, long-tail, or related keywords.")

class AuditResults(BaseModel):
title_tag: str
meta_description: str
primary_heading: str
secondary_headings: List[HeadingItem]
word_count: Optional[int]
content_summary:

================================================
FILE: .history/schemas_20251024142529.py
================================================
from pydantic import BaseModel, Field
from typing import List, Optional

class LinkCounts(BaseModel):
internal: int = Field(..., description="Number of Internal links found on the page")
external: int = Field(..., description="Number of External links found on the page")

class HeadingItem(BaseModel):
internal: int = Field(..., description="Number of internal links found on the page")
external: int = Field(..., description="Number of external links found on the page")

class HeadingItem(BaseModel):
tag: str = Field(..., description="Heading tag such as h1, h2, h3.")
text: str = Field(..., description="Text content of the heading.")

class TargetKeywords(BaseModel):
primary_keyword: str = Field(..., description="The main keyword the page is optimized for.")
search_intent: str = Field(..., description="Inferred search intent (e.g., informational, commercial, transactional).")
secondary_keyword: List[str] = Field(..., description="A list of supporting, long-tail, or related keywords.")

class AuditResults(BaseModel):
title_tag: str
meta_description: str
primary_heading: str
secondary_headings: List[HeadingItem]
word_count: Optional[int]
content_summary: str
link_counts: LinkCounts
technical_findings: List[str] = Field(default_factory=list, description="List of")

================================================
FILE: .history/schemas_20251024142553.py
================================================
from pydantic import BaseModel, Field
from typing import List, Optional

class LinkCounts(BaseModel):
internal: int = Field(..., description="Number of Internal links found on the page")
external: int = Field(..., description="Number of External links found on the page")

class HeadingItem(BaseModel):
internal: int = Field(..., description="Number of internal links found on the page")
external: int = Field(..., description="Number of external links found on the page")

class HeadingItem(BaseModel):
tag: str = Field(..., description="Heading tag such as h1, h2, h3.")
text: str = Field(..., description="Text content of the heading.")

class TargetKeywords(BaseModel):
primary_keyword: str = Field(..., description="The main keyword the page is optimized for.")
search_intent: str = Field(..., description="Inferred search intent (e.g., informational, commercial, transactional).")
secondary_keyword: List[str] = Field(..., description="A list of supporting, long-tail, or related keywords.")

class AuditResults(BaseModel):
title_tag: str
meta_description: str
primary_heading: str
secondary_headings: List[HeadingItem]
word_count: Optional[int]
content_summary: str
link_counts: LinkCounts
technical_findings: List[str] = Field(default_factory=list, description="List of technical SEO issues found.")

================================================
FILE: .history/schemas_20251024142701.py
================================================
from pydantic import BaseModel, Field
from typing import List, Optional

class LinkCounts(BaseModel):
internal: int = Field(..., description="Number of Internal links found on the page")
external: int = Field(..., description="Number of External links found on the page")

class HeadingItem(BaseModel):
internal: int = Field(..., description="Number of internal links found on the page")
external: int = Field(..., description="Number of external links found on the page")

class HeadingItem(BaseModel):
tag: str = Field(..., description="Heading tag such as h1, h2, h3.")
text: str = Field(..., description="Text content of the heading.")

class TargetKeywords(BaseModel):
primary_keyword: str = Field(..., description="The main keyword the page is optimized for.")
search_intent: str = Field(..., description="Inferred search intent (e.g., informational, commercial, transactional).")
secondary_keyword: List[str] = Field(..., description="A list of supporting, long-tail, or related keywords.")

class AuditResults(BaseModel):
title_tag: str
meta_description: str
primary_heading: str
secondary_headings: List[HeadingItem]
word_count: Optional[int]
content_summary: str
link_counts: LinkCounts
technical_findings: List[str] = Field(default_factory=list, description="List of technical SEO issues found.")
content_opportunities: List[str] = Field(default_factory=list, description="List of")

================================================
FILE: .history/schemas_20251024142736.py
================================================
from pydantic import BaseModel, Field
from typing import List, Optional

class LinkCounts(BaseModel):
internal: int = Field(..., description="Number of Internal links found on the page")
external: int = Field(..., description="Number of External links found on the page")

class HeadingItem(BaseModel):
internal: int = Field(..., description="Number of internal links found on the page")
external: int = Field(..., description="Number of external links found on the page")

class HeadingItem(BaseModel):
tag: str = Field(..., description="Heading tag such as h1, h2, h3.")
text: str = Field(..., description="Text content of the heading.")

class TargetKeywords(BaseModel):
primary_keyword: str = Field(..., description="The main keyword the page is optimized for.")
search_intent: str = Field(..., description="Inferred search intent (e.g., informational, commercial, transactional).")
secondary_keyword: List[str] = Field(..., description="A list of supporting, long-tail, or related keywords.")

class AuditResults(BaseModel):
title_tag: str
meta_description: str
primary_heading: str
secondary_headings: List[HeadingItem]
word_count: Optional[int]
content_summary: str
link_counts: LinkCounts
technical_findings: List[str] = Field(default_factory=list, description="List of technical SEO issues found.")
content_opportunities: List[str] = Field(default_factory=list, description="List of immediate content opportunities")

================================================
FILE: .history/schemas_20251024143047.py
================================================
from pydantic import BaseModel, Field
from typing import List, Optional

class LinkCounts(BaseModel):
internal: int = Field(..., description="Number of Internal links found on the page")
external: int = Field(..., description="Number of External links found on the page")

class HeadingItem(BaseModel):
internal: int = Field(..., description="Number of internal links found on the page")
external: int = Field(..., description="Number of external links found on the page")

class HeadingItem(BaseModel):
tag: str = Field(..., description="Heading tag such as h1, h2, h3.")
text: str = Field(..., description="Text content of the heading.")

class TargetKeywords(BaseModel):
primary_keyword: str = Field(..., description="The main keyword the page is optimized for.")
search_intent: str = Field(..., description="Inferred search intent (e.g., informational, commercial, transactional).")
secondary_keyword: List[str] = Field(..., description="A list of supporting, long-tail, or related keywords.")

class AuditResults(BaseModel):
title_tag: str
meta_description: str
primary_heading: str
secondary_headings: List[HeadingItem]
word_count: Optional[int]
content_summary: str
link_counts: LinkCounts
technical_findings: List[str] = Field(default_factory=list, description="List of technical SEO issues found.")
content_opportunities: List[str] = Field(default_factory=list, description="List of immediate content opportunities")

class PageAuditOutput(BaseModel):
audit_results: AuditResults
target_keywords: TargetKeywords

================================================
FILE: .history/schemas_20251024143420.py
================================================
from pydantic import BaseModel, Field
from typing import List, Optional

class LinkCounts(BaseModel):
internal: int = Field(..., description="Number of Internal links found on the page")
external: int = Field(..., description="Number of External links found on the page")

class HeadingItem(BaseModel):
internal: int = Field(..., description="Number of internal links found on the page")
external: int = Field(..., description="Number of external links found on the page")

class HeadingItem(BaseModel):
tag: str = Field(..., description="Heading tag such as h1, h2, h3.")
text: str = Field(..., description="Text content of the heading.")

class TargetKeywords(BaseModel):
primary_keyword: str = Field(..., description="The main keyword the page is optimized for.")
search_intent: str = Field(..., description="Inferred search intent (e.g., informational, commercial, transactional).")
secondary_keyword: List[str] = Field(..., description="A list of supporting, long-tail, or related keywords.")

class AuditResults(BaseModel):
title_tag: str
meta_description: str
primary_heading: str
secondary_headings: List[HeadingItem]
word_count: Optional[int]
content_summary: str
link_counts: LinkCounts
technical_findings: List[str] = Field(default_factory=list, description="List of technical SEO issues found.")
content_opportunities: List[str] = Field(default_factory=list, description="List of immediate content opportunities")

class PageAuditOutput(BaseModel):
audit_results: AuditResults
target_keywords: TargetKeywords

class SerpResult(BaseModel):
rank: int = Field(..., description="The organic search rank (1-10).")
title: str = Field(..., description="The title tag of the search result.")
url: str = Field(..., description="The URL of competitor page.")
snippet: str = Field(..., description="The short description/snippet from the search result")

================================================
FILE: .history/schemas_20251024143531.py
================================================
from pydantic import BaseModel, Field
from typing import List, Optional

class LinkCounts(BaseModel):
internal: int = Field(..., description="Number of Internal links found on the page")
external: int = Field(..., description="Number of External links found on the page")

class HeadingItem(BaseModel):
internal: int = Field(..., description="Number of internal links found on the page")
external: int = Field(..., description="Number of external links found on the page")

class HeadingItem(BaseModel):
tag: str = Field(..., description="Heading tag such as h1, h2, h3.")
text: str = Field(..., description="Text content of the heading.")

class TargetKeywords(BaseModel):
primary_keyword: str = Field(..., description="The main keyword the page is optimized for.")
search_intent: str = Field(..., description="Inferred search intent (e.g., informational, commercial, transactional).")
secondary_keyword: List[str] = Field(..., description="A list of supporting, long-tail, or related keywords.")

class AuditResults(BaseModel):
title_tag: str
meta_description: str
primary_heading: str
secondary_headings: List[HeadingItem]
word_count: Optional[int]
content_summary: str
link_counts: LinkCounts
technical_findings: List[str] = Field(default_factory=list, description="List of technical SEO issues found.")
content_opportunities: List[str] = Field(default_factory=list, description="List of immediate content opportunities")

class PageAuditOutput(BaseModel):
audit_results: AuditResults
target_keywords: TargetKeywords

class SerpResult(BaseModel):
rank: int = Field(..., description="The organic search rank (1-10).")
title: str = Field(..., description="The title tag of the search result.")
url: str = Field(..., description="The URL of competitor page.")
snippet: str = Field(..., description="The short description/snippet from the search result.")
content_type: str = Field(..., description="Inferred content format (e.g., blog post)")

================================================
FILE: .history/schemas_20251024143545.py
================================================
from pydantic import BaseModel, Field
from typing import List, Optional

class LinkCounts(BaseModel):
internal: int = Field(..., description="Number of Internal links found on the page")
external: int = Field(..., description="Number of External links found on the page")

class HeadingItem(BaseModel):
internal: int = Field(..., description="Number of internal links found on the page")
external: int = Field(..., description="Number of external links found on the page")

class HeadingItem(BaseModel):
tag: str = Field(..., description="Heading tag such as h1, h2, h3.")
text: str = Field(..., description="Text content of the heading.")

class TargetKeywords(BaseModel):
primary_keyword: str = Field(..., description="The main keyword the page is optimized for.")
search_intent: str = Field(..., description="Inferred search intent (e.g., informational, commercial, transactional).")
secondary_keyword: List[str] = Field(..., description="A list of supporting, long-tail, or related keywords.")

class AuditResults(BaseModel):
title_tag: str
meta_description: str
primary_heading: str
secondary_headings: List[HeadingItem]
word_count: Optional[int]
content_summary: str
link_counts: LinkCounts
technical_findings: List[str] = Field(default_factory=list, description="List of technical SEO issues found.")
content_opportunities: List[str] = Field(default_factory=list, description="List of immediate content opportunities")

class PageAuditOutput(BaseModel):
audit_results: AuditResults
target_keywords: TargetKeywords

class SerpResult(BaseModel):
rank: int = Field(..., description="The organic search rank (1-10).")
title: str = Field(..., description="The title tag of the search result.")
url: str = Field(..., description="The URL of competitor page.")
snippet: str = Field(..., description="The short description/snippet from the search result.")
content_type: str = Field(..., description="Inferred content format (e.g., blog post, landing page, video. )")

================================================
FILE: .history/schemas_20251024143602.py
================================================
from pydantic import BaseModel, Field
from typing import List, Optional

class LinkCounts(BaseModel):
internal: int = Field(..., description="Number of Internal links found on the page")
external: int = Field(..., description="Number of External links found on the page")

class HeadingItem(BaseModel):
internal: int = Field(..., description="Number of internal links found on the page")
external: int = Field(..., description="Number of external links found on the page")

class HeadingItem(BaseModel):
tag: str = Field(..., description="Heading tag such as h1, h2, h3.")
text: str = Field(..., description="Text content of the heading.")

class TargetKeywords(BaseModel):
primary_keyword: str = Field(..., description="The main keyword the page is optimized for.")
search_intent: str = Field(..., description="Inferred search intent (e.g., informational, commercial, transactional).")
secondary_keyword: List[str] = Field(..., description="A list of supporting, long-tail, or related keywords.")

class AuditResults(BaseModel):
title_tag: str
meta_description: str
primary_heading: str
secondary_headings: List[HeadingItem]
word_count: Optional[int]
content_summary: str
link_counts: LinkCounts
technical_findings: List[str] = Field(default_factory=list, description="List of technical SEO issues found.")
content_opportunities: List[str] = Field(default_factory=list, description="List of immediate content opportunities")

class PageAuditOutput(BaseModel):
audit_results: AuditResults
target_keywords: TargetKeywords

class SerpResult(BaseModel):
rank: int = Field(..., description="The organic search rank (1-10).")
title: str = Field(..., description="The title tag of the search result.")
url: str = Field(..., description="The URL of competitor page.")
snippet: str = Field(..., description="The short description/snippet from the search result.")
content_type: str = Field(..., description="Inferred content format (e.g., blog post, landing page, video, product page.)")

================================================
FILE: .history/schemas_20251024143621.py
================================================
from pydantic import BaseModel, Field
from typing import List, Optional

class LinkCounts(BaseModel):
internal: int = Field(..., description="Number of Internal links found on the page")
external: int = Field(..., description="Number of External links found on the page")

class HeadingItem(BaseModel):
internal: int = Field(..., description="Number of internal links found on the page")
external: int = Field(..., description="Number of external links found on the page")

class HeadingItem(BaseModel):
tag: str = Field(..., description="Heading tag such as h1, h2, h3.")
text: str = Field(..., description="Text content of the heading.")

class TargetKeywords(BaseModel):
primary_keyword: str = Field(..., description="The main keyword the page is optimized for.")
search_intent: str = Field(..., description="Inferred search intent (e.g., informational, commercial, transactional).")
secondary_keyword: List[str] = Field(..., description="A list of supporting, long-tail, or related keywords.")

class AuditResults(BaseModel):
title_tag: str
meta_description: str
primary_heading: str
secondary_headings: List[HeadingItem]
word_count: Optional[int]
content_summary: str
link_counts: LinkCounts
technical_findings: List[str] = Field(default_factory=list, description="List of technical SEO issues found.")
content_opportunities: List[str] = Field(default_factory=list, description="List of immediate content opportunities")

class PageAuditOutput(BaseModel):
audit_results: AuditResults
target_keywords: TargetKeywords

class SerpResult(BaseModel):
rank: int = Field(..., description="The organic search rank (1-10).")
title: str = Field(..., description="The title tag of the search result.")
url: str = Field(..., description="The URL of competitor page.")
snippet: str = Field(..., description="The short description/snippet from the search result.")
content_type: str = Field(..., description="Inferred content format (e.g., blog post, landing page, video, product page.)")

================================================
FILE: .history/schemas_20251024144004.py
================================================
from pydantic import BaseModel, Field
from typing import List, Optional

class LinkCounts(BaseModel):
internal: int = Field(..., description="Number of Internal links found on the page")
external: int = Field(..., description="Number of External links found on the page")

class HeadingItem(BaseModel):
internal: int = Field(..., description="Number of internal links found on the page")
external: int = Field(..., description="Number of external links found on the page")

class HeadingItem(BaseModel):
tag: str = Field(..., description="Heading tag such as h1, h2, h3.")
text: str = Field(..., description="Text content of the heading.")

class TargetKeywords(BaseModel):
primary_keyword: str = Field(..., description="The main keyword the page is optimized for.")
search_intent: str = Field(..., description="Inferred search intent (e.g., informational, commercial, transactional).")
secondary_keyword: List[str] = Field(..., description="A list of supporting, long-tail, or related keywords.")

class AuditResults(BaseModel):
title_tag: str
meta_description: str
primary_heading: str
secondary_headings: List[HeadingItem]
word_count: Optional[int]
content_summary: str
link_counts: LinkCounts
technical_findings: List[str] = Field(default_factory=list, description="List of technical SEO issues found.")
content_opportunities: List[str] = Field(default_factory=list, description="List of immediate content opportunities")

class PageAuditOutput(BaseModel):
audit_results: AuditResults
target_keywords: TargetKeywords

class SerpResult(BaseModel):
rank: int = Field(..., description="The organic search rank (1-10).")
title: str = Field(..., description="The title tag of the search result.")
url: str = Field(..., description="The URL of competitor page.")
snippet: str = Field(..., description="The short description/snippet from the search result.")
content_type: str = Field(..., description="Inferred content format (e.g., blog post, landing page, video, product page.)")

class SerpAnalysis(BaseModel):
keyword_searched: str
top_competitors: List[SerpResult]
common_title_patterns: List[str] = Field(..., description="Common phrases of structu")

================================================
FILE: .history/schemas_20251024144033.py
================================================
from pydantic import BaseModel, Field
from typing import List, Optional

class LinkCounts(BaseModel):
internal: int = Field(..., description="Number of Internal links found on the page")
external: int = Field(..., description="Number of External links found on the page")

class HeadingItem(BaseModel):
internal: int = Field(..., description="Number of internal links found on the page")
external: int = Field(..., description="Number of external links found on the page")

class HeadingItem(BaseModel):
tag: str = Field(..., description="Heading tag such as h1, h2, h3.")
text: str = Field(..., description="Text content of the heading.")

class TargetKeywords(BaseModel):
primary_keyword: str = Field(..., description="The main keyword the page is optimized for.")
search_intent: str = Field(..., description="Inferred search intent (e.g., informational, commercial, transactional).")
secondary_keyword: List[str] = Field(..., description="A list of supporting, long-tail, or related keywords.")

class AuditResults(BaseModel):
title_tag: str
meta_description: str
primary_heading: str
secondary_headings: List[HeadingItem]
word_count: Optional[int]
content_summary: str
link_counts: LinkCounts
technical_findings: List[str] = Field(default_factory=list, description="List of technical SEO issues found.")
content_opportunities: List[str] = Field(default_factory=list, description="List of immediate content opportunities")

class PageAuditOutput(BaseModel):
audit_results: AuditResults
target_keywords: TargetKeywords

class SerpResult(BaseModel):
rank: int = Field(..., description="The organic search rank (1-10).")
title: str = Field(..., description="The title tag of the search result.")
url: str = Field(..., description="The URL of competitor page.")
snippet: str = Field(..., description="The short description/snippet from the search result.")
content_type: str = Field(..., description="Inferred content format (e.g., blog post, landing page, video, product page.)")

class SerpAnalysis(BaseModel):
keyword_searched: str
top_competitors: List[SerpResult]
common_title_patterns: List[str] = Field(..., description="Common phrases of structures in the top-ranking titles")

================================================
FILE: .history/schemas_20251024144109.py
================================================
from pydantic import BaseModel, Field
from typing import List, Optional

class LinkCounts(BaseModel):
internal: int = Field(..., description="Number of Internal links found on the page")
external: int = Field(..., description="Number of External links found on the page")

class HeadingItem(BaseModel):
internal: int = Field(..., description="Number of internal links found on the page")
external: int = Field(..., description="Number of external links found on the page")

class HeadingItem(BaseModel):
tag: str = Field(..., description="Heading tag such as h1, h2, h3.")
text: str = Field(..., description="Text content of the heading.")

class TargetKeywords(BaseModel):
primary_keyword: str = Field(..., description="The main keyword the page is optimized for.")
search_intent: str = Field(..., description="Inferred search intent (e.g., informational, commercial, transactional).")
secondary_keyword: List[str] = Field(..., description="A list of supporting, long-tail, or related keywords.")

class AuditResults(BaseModel):
title_tag: str
meta_description: str
primary_heading: str
secondary_headings: List[HeadingItem]
word_count: Optional[int]
content_summary: str
link_counts: LinkCounts
technical_findings: List[str] = Field(default_factory=list, description="List of technical SEO issues found.")
content_opportunities: List[str] = Field(default_factory=list, description="List of immediate content opportunities")

class PageAuditOutput(BaseModel):
audit_results: AuditResults
target_keywords: TargetKeywords

class SerpResult(BaseModel):
rank: int = Field(..., description="The organic search rank (1-10).")
title: str = Field(..., description="The title tag of the search result.")
url: str = Field(..., description="The URL of competitor page.")
snippet: str = Field(..., description="The short description/snippet from the search result.")
content_type: str = Field(..., description="Inferred content format (e.g., blog post, landing page, video, product page.)")

class SerpAnalysis(BaseModel):
keyword_searched: str
top_competitors: List[SerpResult]
common_title_patterns: List[str] = Field(..., description="Common phrases of structures in the top-ranking titles")
dominant_content_format: str = Field(..., description="The most content format")

================================================
FILE: .history/schemas_20251024144200.py
================================================
from pydantic import BaseModel, Field
from typing import List, Optional

class LinkCounts(BaseModel):
internal: int = Field(..., description="Number of Internal links found on the page")
external: int = Field(..., description="Number of External links found on the page")

class HeadingItem(BaseModel):
internal: int = Field(..., description="Number of internal links found on the page")
external: int = Field(..., description="Number of external links found on the page")

class HeadingItem(BaseModel):
tag: str = Field(..., description="Heading tag such as h1, h2, h3.")
text: str = Field(..., description="Text content of the heading.")

class TargetKeywords(BaseModel):
primary_keyword: str = Field(..., description="The main keyword the page is optimized for.")
search_intent: str = Field(..., description="Inferred search intent (e.g., informational, commercial, transactional).")
secondary_keyword: List[str] = Field(..., description="A list of supporting, long-tail, or related keywords.")

class AuditResults(BaseModel):
title_tag: str
meta_description: str
primary_heading: str
secondary_headings: List[HeadingItem]
word_count: Optional[int]
content_summary: str
link_counts: LinkCounts
technical_findings: List[str] = Field(default_factory=list, description="List of technical SEO issues found.")
content_opportunities: List[str] = Field(default_factory=list, description="List of immediate content opportunities")

class PageAuditOutput(BaseModel):
audit_results: AuditResults
target_keywords: TargetKeywords

class SerpResult(BaseModel):
rank: int = Field(..., description="The organic search rank (1-10).")
title: str = Field(..., description="The title tag of the search result.")
url: str = Field(..., description="The URL of competitor page.")
snippet: str = Field(..., description="The short description/snippet from the search result.")
content_type: str = Field(..., description="Inferred content format (e.g., blog post, landing page, video, product page.)")

class SerpAnalysis(BaseModel):
keyword_searched: str
top_competitors: List[SerpResult]
common_title_patterns: List[str] = Field(..., description="Common phrases of structures in the top-ranking titles")
dominant_content_format: str = Field(..., description="The most content format (e.g., 'How-to guides', 'Listicles').")

================================================
FILE: .history/schemas_20251024144258.py
================================================
from pydantic import BaseModel, Field
from typing import List, Optional

class LinkCounts(BaseModel):
internal: int = Field(..., description="Number of Internal links found on the page")
external: int = Field(..., description="Number of External links found on the page")

class HeadingItem(BaseModel):
internal: int = Field(..., description="Number of internal links found on the page")
external: int = Field(..., description="Number of external links found on the page")

class HeadingItem(BaseModel):
tag: str = Field(..., description="Heading tag such as h1, h2, h3.")
text: str = Field(..., description="Text content of the heading.")

class TargetKeywords(BaseModel):
primary_keyword: str = Field(..., description="The main keyword the page is optimized for.")
search_intent: str = Field(..., description="Inferred search intent (e.g., informational, commercial, transactional).")
secondary_keyword: List[str] = Field(..., description="A list of supporting, long-tail, or related keywords.")

class AuditResults(BaseModel):
title_tag: str
meta_description: str
primary_heading: str
secondary_headings: List[HeadingItem]
word_count: Optional[int]
content_summary: str
link_counts: LinkCounts
technical_findings: List[str] = Field(default_factory=list, description="List of technical SEO issues found.")
content_opportunities: List[str] = Field(default_factory=list, description="List of immediate content opportunities")

class PageAuditOutput(BaseModel):
audit_results: AuditResults
target_keywords: TargetKeywords

class SerpResult(BaseModel):
rank: int = Field(..., description="The organic search rank (1-10).")
title: str = Field(..., description="The title tag of the search result.")
url: str = Field(..., description="The URL of competitor page.")
snippet: str = Field(..., description="The short description/snippet from the search result.")
content_type: str = Field(..., description="Inferred content format (e.g., blog post, landing page, video, product page.)")

class SerpAnalysis(BaseModel):
keyword_searched: str
top_competitors: List[SerpResult]
common_title_patterns: List[str] = Field(..., description="Common phrases of structures in the top-ranking titles")
dominant_content_format: str = Field(..., description="The most content format (e.g., 'How-to guides', 'Listicles').")
key_themes_and_angles: List[str] = Field(..., description="Specific opportunities ")

================================================
FILE: .history/schemas_20251024144331.py
================================================
from pydantic import BaseModel, Field
from typing import List, Optional

class LinkCounts(BaseModel):
internal: int = Field(..., description="Number of Internal links found on the page")
external: int = Field(..., description="Number of External links found on the page")

class HeadingItem(BaseModel):
internal: int = Field(..., description="Number of internal links found on the page")
external: int = Field(..., description="Number of external links found on the page")

class HeadingItem(BaseModel):
tag: str = Field(..., description="Heading tag such as h1, h2, h3.")
text: str = Field(..., description="Text content of the heading.")

class TargetKeywords(BaseModel):
primary_keyword: str = Field(..., description="The main keyword the page is optimized for.")
search_intent: str = Field(..., description="Inferred search intent (e.g., informational, commercial, transactional).")
secondary_keyword: List[str] = Field(..., description="A list of supporting, long-tail, or related keywords.")

class AuditResults(BaseModel):
title_tag: str
meta_description: str
primary_heading: str
secondary_headings: List[HeadingItem]
word_count: Optional[int]
content_summary: str
link_counts: LinkCounts
technical_findings: List[str] = Field(default_factory=list, description="List of technical SEO issues found.")
content_opportunities: List[str] = Field(default_factory=list, description="List of immediate content opportunities")

class PageAuditOutput(BaseModel):
audit_results: AuditResults
target_keywords: TargetKeywords

class SerpResult(BaseModel):
rank: int = Field(..., description="The organic search rank (1-10).")
title: str = Field(..., description="The title tag of the search result.")
url: str = Field(..., description="The URL of competitor page.")
snippet: str = Field(..., description="The short description/snippet from the search result.")
content_type: str = Field(..., description="Inferred content format (e.g., blog post, landing page, video, product page.)")

class SerpAnalysis(BaseModel):
keyword_searched: str
top_competitors: List[SerpResult]
common_title_patterns: List[str] = Field(..., description="Common phrases of structures in the top-ranking titles")
dominant_content_format: str = Field(..., description="The most content format (e.g., 'How-to guides', 'Listicles').")
key_themes_and_angles: List[str] = Field(..., description="Specific opportunities based on SERP analysis (e.g., '') ")

================================================
FILE: .history/schemas_20251024144356.py
================================================
from pydantic import BaseModel, Field
from typing import List, Optional

class LinkCounts(BaseModel):
internal: int = Field(..., description="Number of Internal links found on the page")
external: int = Field(..., description="Number of External links found on the page")

class HeadingItem(BaseModel):
internal: int = Field(..., description="Number of internal links found on the page")
external: int = Field(..., description="Number of external links found on the page")

class HeadingItem(BaseModel):
tag: str = Field(..., description="Heading tag such as h1, h2, h3.")
text: str = Field(..., description="Text content of the heading.")

class TargetKeywords(BaseModel):
primary_keyword: str = Field(..., description="The main keyword the page is optimized for.")
search_intent: str = Field(..., description="Inferred search intent (e.g., informational, commercial, transactional).")
secondary_keyword: List[str] = Field(..., description="A list of supporting, long-tail, or related keywords.")

class AuditResults(BaseModel):
title_tag: str
meta_description: str
primary_heading: str
secondary_headings: List[HeadingItem]
word_count: Optional[int]
content_summary: str
link_counts: LinkCounts
technical_findings: List[str] = Field(default_factory=list, description="List of technical SEO issues found.")
content_opportunities: List[str] = Field(default_factory=list, description="List of immediate content opportunities")

class PageAuditOutput(BaseModel):
audit_results: AuditResults
target_keywords: TargetKeywords

class SerpResult(BaseModel):
rank: int = Field(..., description="The organic search rank (1-10).")
title: str = Field(..., description="The title tag of the search result.")
url: str = Field(..., description="The URL of competitor page.")
snippet: str = Field(..., description="The short description/snippet from the search result.")
content_type: str = Field(..., description="Inferred content format (e.g., blog post, landing page, video, product page.)")

class SerpAnalysis(BaseModel):
keyword_searched: str
top_competitors: List[SerpResult]
common_title_patterns: List[str] = Field(..., description="Common phrases of structures in the top-ranking titles")
dominant_content_format: str = Field(..., description="The most content format (e.g., 'How-to guides', 'Listicles').")
key_themes_and_angles: List[str] = Field(..., description="Specific opportunities based on SERP analysis (e.g., 'Target missing Q&A section'). ")

================================================
FILE: .history/schemas_20251024144409.py
================================================
from pydantic import BaseModel, Field
from typing import List, Optional

class LinkCounts(BaseModel):
internal: int = Field(..., description="Number of Internal links found on the page")
external: int = Field(..., description="Number of External links found on the page")

class HeadingItem(BaseModel):
internal: int = Field(..., description="Number of internal links found on the page")
external: int = Field(..., description="Number of external links found on the page")

class HeadingItem(BaseModel):
tag: str = Field(..., description="Heading tag such as h1, h2, h3.")
text: str = Field(..., description="Text content of the heading.")

class TargetKeywords(BaseModel):
primary_keyword: str = Field(..., description="The main keyword the page is optimized for.")
search_intent: str = Field(..., description="Inferred search intent (e.g., informational, commercial, transactional).")
secondary_keyword: List[str] = Field(..., description="A list of supporting, long-tail, or related keywords.")

class AuditResults(BaseModel):
title_tag: str
meta_description: str
primary_heading: str
secondary_headings: List[HeadingItem]
word_count: Optional[int]
content_summary: str
link_counts: LinkCounts
technical_findings: List[str] = Field(default_factory=list, description="List of technical SEO issues found.")
content_opportunities: List[str] = Field(default_factory=list, description="List of immediate content opportunities")

class PageAuditOutput(BaseModel):
audit_results: AuditResults
target_keywords: TargetKeywords

class SerpResult(BaseModel):
rank: int = Field(..., description="The organic search rank (1-10).")
title: str = Field(..., description="The title tag of the search result.")
url: str = Field(..., description="The URL of competitor page.")
snippet: str = Field(..., description="The short description/snippet from the search result.")
content_type: str = Field(..., description="Inferred content format (e.g., blog post, landing page, video, product page.)")

class SerpAnalysis(BaseModel):
keyword_searched: str
top_competitors: List[SerpResult]
common_title_patterns: List[str] = Field(..., description="Common phrases of structures in the top-ranking titles")
dominant_content_format: str = Field(..., description="The most content format (e.g., 'How-to guides', 'Listicles').")
key_themes_and_angles: List[str] = Field(..., description="Specific opportunities based on SERP analysis (e.g., 'Target missing Q&A section'). ")

================================================
FILE: .history/schemas_20251024144820.py
================================================
from pydantic import BaseModel, Field
from typing import List, Optional

class LinkCounts(BaseModel):
internal: int = Field(..., description="Number of Internal links found on the page")
external: int = Field(..., description="Number of External links found on the page")

class HeadingItem(BaseModel):
internal: int = Field(..., description="Number of internal links found on the page")
external: int = Field(..., description="Number of external links found on the page")

class HeadingItem(BaseModel):
tag: str = Field(..., description="Heading tag such as h1, h2, h3.")
text: str = Field(..., description="Text content of the heading.")

class TargetKeywords(BaseModel):
primary_keyword: str = Field(..., description="The main keyword the page is optimized for.")
search_intent: str = Field(..., description="Inferred search intent (e.g., informational, commercial, transactional).")
secondary_keyword: List[str] = Field(..., description="A list of supporting, long-tail, or related keywords.")

class AuditResults(BaseModel):
title_tag: str
meta_description: str
primary_heading: str
secondary_headings: List[HeadingItem]
word_count: Optional[int]
content_summary: str
link_counts: LinkCounts
technical_findings: List[str] = Field(default_factory=list, description="List of technical SEO issues found.")
content_opportunities: List[str] = Field(default_factory=list, description="List of immediate content opportunities")

class PageAuditOutput(BaseModel):
audit_results: AuditResults
target_keywords: TargetKeywords

class SerpResult(BaseModel):
rank: int = Field(..., description="The organic search rank (1-10).")
title: str = Field(..., description="The title tag of the search result.")
url: str = Field(..., description="The URL of competitor page.")
snippet: str = Field(..., description="The short description/snippet from the search result.")
content_type: str = Field(..., description="Inferred content format (e.g., blog post, landing page, video, product page.)")

class SerpAnalysis(BaseModel):
keyword_searched: str
top_competitors: List[SerpResult]
common_title_patterns: List[str] = Field(..., description="Common phrases of structures in the top-ranking titles")
dominant_content_format: str = Field(..., description="The most content format (e.g., 'How-to guides', 'Listicles').")
key_themes_and_angles: List[str] = Field(..., description="Specific opportunities based on SERP analysis (e.g., 'Target missing Q&A section'). ")

================================================
FILE: .history/schemas_20251024161321.py
================================================

# schemas.py

from pydantic import BaseModel, Field
from typing import List, Optional

# --- Estruturas Auxiliares para o Page Auditor ---

class LinkCounts(BaseModel):
internal: int = Field(..., description="Number of internal links found on the page.")
external: int = Field(..., description="Number of external links found on the page.")

class HeadingItem(BaseModel):
tag: str = Field(..., description="Heading tag such as h1, h2, h3.")
text: str = Field(..., description="Text content of the heading.")

class TargetKeywords(BaseModel):
primary_keyword: str = Field(..., description="The main keyword the page is optimized for.")
search_intent: str = Field(..., description="Inferred search intent (e.g., informational, commercial, transactional).")
secondary_keywords: List[str] = Field(default_factory=list, description="A list of supporting, long-tail, or related keywords.")

class AuditResults(BaseModel):
title_tag: str
meta_description: str
primary_heading: str
secondary_headings: List[HeadingItem]
word_count: Optional[int]
content_summary: str
link_counts: LinkCounts
technical_findings: List[str] = Field(default_factory=list, description="List of technical SEO issues found.")
content_opportunities: List[str] = Field(default_factory=list, description="List of immediate content opportunities.")

# --- Saída do Page Auditor Agent ---

class PageAuditOutput(BaseModel):
audit_results: AuditResults
target_keywords: TargetKeywords

# --- Estruturas Auxiliares para o SERP Analyst ---

class SerpResult(BaseModel): # Definição da classe SerpResult
rank: int = Field(..., description="The organic search rank (1-10).")
title: str = Field(..., description="The title tag of the search result.")
url: str = Field(..., description="The URL of the competitor page.")
snippet: str = Field(..., description="The short description/snippet from the search result.")
content_type: str = Field(..., description="Inferred content format (e.g., blog post, landing page, video, product page).")

# --- Saída do SERP Analyst Agent ---

class SerpAnalysis(BaseModel):
keyword_searched: str
top_competitors: List[SerpResult] # Usando SerpResult corretamente
common_title_patterns: List[str] = Field(default_factory=list, description="Common phrases or structures in the top-ranking titles.")
dominant_content_format: str = Field(..., description="The most common content format (e.g., 'How-to guides', 'Listicles').")
key_themes_and_angles: List[str] = Field(default_factory=list, description="Key topics, themes, or differentiation angles to cover.")
serp_opportunities: List[str] = Field(default_factory=list, description="Specific opportunities based on SERP analysis.")

================================================
FILE: .history/schemas_20251027165600.py
================================================
from pydantic import BaseModel, Field
from typing import List, Optional

#Page Audictor ---
class LinkCounts(BaseModel):
internal: int = Field(..., description="Number of internal links found on the page.")
external: int = Field(..., description="Number of external links found on the page.")

class HeadingItem(BaseModel):
tag: str = Field(..., description="Heading tag such as h1, h2, h3.")
text: str = Field(..., description="Text content of the heading.")

class TargetKeywords(BaseModel):
primary_keyword: str = Field(..., description="The main keyword the page is optimized for.")
search_intent: str = Field(..., description="Inferred search intent (e.g., informational, commercial, transactional).")
secondary_keywords: List[str] = Field(default_factory=list, description="A list of supporting, long-tail, or related keywords.")

class AuditResults(BaseModel):
title_tag: str
meta_description: str
primary_heading: str
secondary_headings: List[HeadingItem]
word_count: Optional[int]
content_summary: str
link_counts: LinkCounts
technical_findings: List[str] = Field(default_factory=list, description="List of technical SEO issues found.")
content_opportunities: List[str] = Field(default_factory=list, description="List of immediate content opportunities.")

# Output Page Audictor Agent ---

class PageAuditOutput(BaseModel):
audit_results: AuditResults
target_keywords: TargetKeywords

# --- Estruturas Auxiliares para o SERP Analyst ---

class SerpResult(BaseModel): # Definição da classe SerpResult
rank: int = Field(..., description="The organic search rank (1-10).")
title: str = Field(..., description="The title tag of the search result.")
url: str = Field(..., description="The URL of the competitor page.")
snippet: str = Field(..., description="The short description/snippet from the search result.")
content_type: str = Field(..., description="Inferred content format (e.g., blog post, landing page, video, product page).")

# --- Saída do SERP Analyst Agent ---

class SerpAnalysis(BaseModel):
keyword_searched: str
top_competitors: List[SerpResult] # Usando SerpResult corretamente
common_title_patterns: List[str] = Field(default_factory=list, description="Common phrases or structures in the top-ranking titles.")
dominant_content_format: str = Field(..., description="The most common content format (e.g., 'How-to guides', 'Listicles').")
key_themes_and_angles: List[str] = Field(default_factory=list, description="Key topics, themes, or differentiation angles to cover.")
serp_opportunities: List[str] = Field(default_factory=list, description="Specific opportunities based on SERP analysis.")

================================================
FILE: .history/schemas_20251027165638.py
================================================
from pydantic import BaseModel, Field
from typing import List, Optional

#Page Audictor ---
class LinkCounts(BaseModel):
internal: int = Field(..., description="Number of internal links found on the page.")
external: int = Field(..., description="Number of external links found on the page.")

class HeadingItem(BaseModel):
tag: str = Field(..., description="Heading tag such as h1, h2, h3.")
text: str = Field(..., description="Text content of the heading.")

class TargetKeywords(BaseModel):
primary_keyword: str = Field(..., description="The main keyword the page is optimized for.")
search_intent: str = Field(..., description="Inferred search intent (e.g., informational, commercial, transactional).")
secondary_keywords: List[str] = Field(default_factory=list, description="A list of supporting, long-tail, or related keywords.")

class AuditResults(BaseModel):
title_tag: str
meta_description: str
primary_heading: str
secondary_headings: List[HeadingItem]
word_count: Optional[int]
content_summary: str
link_counts: LinkCounts
technical_findings: List[str] = Field(default_factory=list, description="List of technical SEO issues found.")
content_opportunities: List[str] = Field(default_factory=list, description="List of immediate content opportunities.")

# Output Page Auditor Agent ---

class PageAuditOutput(BaseModel):
audit_results: AuditResults
target_keywords: TargetKeywords

# --- Estruturas Auxiliares para o SERP Analyst ---

class SerpResult(BaseModel): # Definição da classe SerpResult
rank: int = Field(..., description="The organic search rank (1-10).")
title: str = Field(..., description="The title tag of the search result.")
url: str = Field(..., description="The URL of the competitor page.")
snippet: str = Field(..., description="The short description/snippet from the search result.")
content_type: str = Field(..., description="Inferred content format (e.g., blog post, landing page, video, product page).")

# --- Saída do SERP Analyst Agent ---

class SerpAnalysis(BaseModel):
keyword_searched: str
top_competitors: List[SerpResult] # Usando SerpResult corretamente
common_title_patterns: List[str] = Field(default_factory=list, description="Common phrases or structures in the top-ranking titles.")
dominant_content_format: str = Field(..., description="The most common content format (e.g., 'How-to guides', 'Listicles').")
key_themes_and_angles: List[str] = Field(default_factory=list, description="Key topics, themes, or differentiation angles to cover.")
serp_opportunities: List[str] = Field(default_factory=list, description="Specific opportunities based on SERP analysis.")

================================================
FILE: .history/schemas_20251027165709.py
================================================
from pydantic import BaseModel, Field
from typing import List, Optional

#Page Auditor ---
class LinkCounts(BaseModel):
internal: int = Field(..., description="Number of internal links found on the page.")
external: int = Field(..., description="Number of external links found on the page.")

class HeadingItem(BaseModel):
tag: str = Field(..., description="Heading tag such as h1, h2, h3.")
text: str = Field(..., description="Text content of the heading.")

class TargetKeywords(BaseModel):
primary_keyword: str = Field(..., description="The main keyword the page is optimized for.")
search_intent: str = Field(..., description="Inferred search intent (e.g., informational, commercial, transactional).")
secondary_keywords: List[str] = Field(default_factory=list, description="A list of supporting, long-tail, or related keywords.")

class AuditResults(BaseModel):
title_tag: str
meta_description: str
primary_heading: str
secondary_headings: List[HeadingItem]
word_count: Optional[int]
content_summary: str
link_counts: LinkCounts
technical_findings: List[str] = Field(default_factory=list, description="List of technical SEO issues found.")
content_opportunities: List[str] = Field(default_factory=list, description="List of immediate content opportunities.")

# Output Page Auditor Agent ---

class PageAuditOutput(BaseModel):
audit_results: AuditResults
target_keywords: TargetKeywords

# --- Auxiliary Structures for SERP Analyst ---

class SerpResult(BaseModel): # Definição da classe SerpResult
rank: int = Field(..., description="The organic search rank (1-10).")
title: str = Field(..., description="The title tag of the search result.")
url: str = Field(..., description="The URL of the competitor page.")
snippet: str = Field(..., description="The short description/snippet from the search result.")
content_type: str = Field(..., description="Inferred content format (e.g., blog post, landing page, video, product page).")

# --- Saída do SERP Analyst Agent ---

class SerpAnalysis(BaseModel):
keyword_searched: str
top_competitors: List[SerpResult] # Usando SerpResult corretamente
common_title_patterns: List[str] = Field(default_factory=list, description="Common phrases or structures in the top-ranking titles.")
dominant_content_format: str = Field(..., description="The most common content format (e.g., 'How-to guides', 'Listicles').")
key_themes_and_angles: List[str] = Field(default_factory=list, description="Key topics, themes, or differentiation angles to cover.")
serp_opportunities: List[str] = Field(default_factory=list, description="Specific opportunities based on SERP analysis.")

================================================
FILE: .history/schemas_20251027171538.py
================================================
from pydantic import BaseModel, Field
from typing import List, Optional

# --- Estruturas Auxiliares para o Page Auditor ---

class LinkCounts(BaseModel):
internal: int = Field(..., description="Number of internal links found on the page.")
external: int = Field(..., description="Number of external links found on the page.")

class HeadingItem(BaseModel):
tag: str = Field(..., description="Heading tag such as h1, h2, h3.")
text: str = Field(..., description="Text content of the heading.")

class TargetKeywords(BaseModel):
primary_keyword: str = Field(..., description="The main keyword the page is optimized for.")
search_intent: str = Field(..., description="Inferred search intent (e.g., informational, commercial, transactional).")
secondary_keywords: List[str] = Field(default_factory=list, description="A list of supporting, long-tail, or related keywords.")

class AuditResults(BaseModel):
title_tag: str
meta_description: str
primary_heading: str
secondary_headings: List[HeadingItem]
word_count: Optional[int]
content_summary: str
link_counts: LinkCounts
technical_findings: List[str] = Field(default_factory=list, description="List of technical SEO issues found.")
content_opportunities: List[str] = Field(default_factory=list, description="List of immediate content opportunities.")

# --- Saída do Page Auditor Agent ---

class PageAuditOutput(BaseModel):
audit_results: AuditResults
target_keywords: TargetKeywords

# --- Estruturas Auxiliares para o SERP Analyst ---

class SerpResult(BaseModel):
rank: int = Field(..., description="The organic search rank (1-10).")
title: str = Field(..., description="The title tag of the search result.")
url: str = Field(..., description="The URL of the competitor page.")
snippet: str = Field(..., description="The short description/snippet from the search result.")
content_type: str = Field(..., description="Inferred content format (e.g., blog post, landing page, video, product page).")

# --- Saída do SERP Analyst Agent ---

class SerpAnalysis(BaseModel):
keyword_searched: str
top_competitors: List[SerpResult]
common_title_patterns: List[str] = Field(default_factory=list, description="Common phrases or structures in the top-ranking titles.")
dominant_content_format: str = Field(..., description="The most common content format (e.g., 'How-to guides', 'Listicles').")
key_themes_and_angles: List[str] = Field(default_factory=list, description="Key topics, themes, or differentiation angles to cover.")
serp_opportunities: List[str] = Field(default_factory=list, description="Specific opportunities based on SERP analysis.")

================================================
FILE: .history/schemas_20251027171605.py
================================================
from pydantic import BaseModel, Field
from typing import List, Optional

# Auxiliary Structures for Page Auditor

class LinkCounts(BaseModel):
internal: int = Field(..., description="Number of internal links found on the page.")
external: int = Field(..., description="Number of external links found on the page.")

class HeadingItem(BaseModel):
tag: str = Field(..., description="Heading tag such as h1, h2, h3.")
text: str = Field(..., description="Text content of the heading.")

class TargetKeywords(BaseModel):
primary_keyword: str = Field(..., description="The main keyword the page is optimized for.")
search_intent: str = Field(..., description="Inferred search intent (e.g., informational, commercial, transactional).")
secondary_keywords: List[str] = Field(default_factory=list, description="A list of supporting, long-tail, or related keywords.")

class AuditResults(BaseModel):
title_tag: str
meta_description: str
primary_heading: str
secondary_headings: List[HeadingItem]
word_count: Optional[int]
content_summary: str
link_counts: LinkCounts
technical_findings: List[str] = Field(default_factory=list, description="List of technical SEO issues found.")
content_opportunities: List[str] = Field(default_factory=list, description="List of immediate content opportunities.")

# Saída do Page Auditor Agent

class PageAuditOutput(BaseModel):
audit_results: AuditResults
target_keywords: TargetKeywords

# --- Estruturas Auxiliares para o SERP Analyst ---

class SerpResult(BaseModel):
rank: int = Field(..., description="The organic search rank (1-10).")
title: str = Field(..., description="The title tag of the search result.")
url: str = Field(..., description="The URL of the competitor page.")
snippet: str = Field(..., description="The short description/snippet from the search result.")
content_type: str = Field(..., description="Inferred content format (e.g., blog post, landing page, video, product page).")

# --- Saída do SERP Analyst Agent ---

class SerpAnalysis(BaseModel):
keyword_searched: str
top_competitors: List[SerpResult]
common_title_patterns: List[str] = Field(default_factory=list, description="Common phrases or structures in the top-ranking titles.")
dominant_content_format: str = Field(..., description="The most common content format (e.g., 'How-to guides', 'Listicles').")
key_themes_and_angles: List[str] = Field(default_factory=list, description="Key topics, themes, or differentiation angles to cover.")
serp_opportunities: List[str] = Field(default_factory=list, description="Specific opportunities based on SERP analysis.")

================================================
FILE: .history/schemas_20251027171622.py
================================================
from pydantic import BaseModel, Field
from typing import List, Optional

# Auxiliary Structures for Page Auditor

class LinkCounts(BaseModel):
internal: int = Field(..., description="Number of internal links found on the page.")
external: int = Field(..., description="Number of external links found on the page.")

class HeadingItem(BaseModel):
tag: str = Field(..., description="Heading tag such as h1, h2, h3.")
text: str = Field(..., description="Text content of the heading.")

class TargetKeywords(BaseModel):
primary_keyword: str = Field(..., description="The main keyword the page is optimized for.")
search_intent: str = Field(..., description="Inferred search intent (e.g., informational, commercial, transactional).")
secondary_keywords: List[str] = Field(default_factory=list, description="A list of supporting, long-tail, or related keywords.")

class AuditResults(BaseModel):
title_tag: str
meta_description: str
primary_heading: str
secondary_headings: List[HeadingItem]
word_count: Optional[int]
content_summary: str
link_counts: LinkCounts
technical_findings: List[str] = Field(default_factory=list, description="List of technical SEO issues found.")
content_opportunities: List[str] = Field(default_factory=list, description="List of immediate content opportunities.")

# Page Auditor Agent Output

class PageAuditOutput(BaseModel):
audit_results: AuditResults
target_keywords: TargetKeywords

# --- Estruturas Auxiliares para o SERP Analyst

class SerpResult(BaseModel):
rank: int = Field(..., description="The organic search rank (1-10).")
title: str = Field(..., description="The title tag of the search result.")
url: str = Field(..., description="The URL of the competitor page.")
snippet: str = Field(..., description="The short description/snippet from the search result.")
content_type: str = Field(..., description="Inferred content format (e.g., blog post, landing page, video, product page).")

# --- Saída do SERP Analyst Agent ---

class SerpAnalysis(BaseModel):
keyword_searched: str
top_competitors: List[SerpResult]
common_title_patterns: List[str] = Field(default_factory=list, description="Common phrases or structures in the top-ranking titles.")
dominant_content_format: str = Field(..., description="The most common content format (e.g., 'How-to guides', 'Listicles').")
key_themes_and_angles: List[str] = Field(default_factory=list, description="Key topics, themes, or differentiation angles to cover.")
serp_opportunities: List[str] = Field(default_factory=list, description="Specific opportunities based on SERP analysis.")

================================================
FILE: .history/schemas_20251027171643.py
================================================
from pydantic import BaseModel, Field
from typing import List, Optional

# Auxiliary Structures for Page Auditor

class LinkCounts(BaseModel):
internal: int = Field(..., description="Number of internal links found on the page.")
external: int = Field(..., description="Number of external links found on the page.")

class HeadingItem(BaseModel):
tag: str = Field(..., description="Heading tag such as h1, h2, h3.")
text: str = Field(..., description="Text content of the heading.")

class TargetKeywords(BaseModel):
primary_keyword: str = Field(..., description="The main keyword the page is optimized for.")
search_intent: str = Field(..., description="Inferred search intent (e.g., informational, commercial, transactional).")
secondary_keywords: List[str] = Field(default_factory=list, description="A list of supporting, long-tail, or related keywords.")

class AuditResults(BaseModel):
title_tag: str
meta_description: str
primary_heading: str
secondary_headings: List[HeadingItem]
word_count: Optional[int]
content_summary: str
link_counts: LinkCounts
technical_findings: List[str] = Field(default_factory=list, description="List of technical SEO issues found.")
content_opportunities: List[str] = Field(default_factory=list, description="List of immediate content opportunities.")

# Page Auditor Agent Output

class PageAuditOutput(BaseModel):
audit_results: AuditResults
target_keywords: TargetKeywords

# Auxiliary Structures for SERP Analyst

class SerpResult(BaseModel):
rank: int = Field(..., description="The organic search rank (1-10).")
title: str = Field(..., description="The title tag of the search result.")
url: str = Field(..., description="The URL of the competitor page.")
snippet: str = Field(..., description="The short description/snippet from the search result.")
content_type: str = Field(..., description="Inferred content format (e.g., blog post, landing page, video, product page).")

# --- Saída do SERP Analyst Agent ---

class SerpAnalysis(BaseModel):
keyword_searched: str
top_competitors: List[SerpResult]
common_title_patterns: List[str] = Field(default_factory=list, description="Common phrases or structures in the top-ranking titles.")
dominant_content_format: str = Field(..., description="The most common content format (e.g., 'How-to guides', 'Listicles').")
key_themes_and_angles: List[str] = Field(default_factory=list, description="Key topics, themes, or differentiation angles to cover.")
serp_opportunities: List[str] = Field(default_factory=list, description="Specific opportunities based on SERP analysis.")

================================================
FILE: .history/schemas_20251027171700.py
================================================
from pydantic import BaseModel, Field
from typing import List, Optional

# Auxiliary Structures for Page Auditor

class LinkCounts(BaseModel):
internal: int = Field(..., description="Number of internal links found on the page.")
external: int = Field(..., description="Number of external links found on the page.")

class HeadingItem(BaseModel):
tag: str = Field(..., description="Heading tag such as h1, h2, h3.")
text: str = Field(..., description="Text content of the heading.")

class TargetKeywords(BaseModel):
primary_keyword: str = Field(..., description="The main keyword the page is optimized for.")
search_intent: str = Field(..., description="Inferred search intent (e.g., informational, commercial, transactional).")
secondary_keywords: List[str] = Field(default_factory=list, description="A list of supporting, long-tail, or related keywords.")

class AuditResults(BaseModel):
title_tag: str
meta_description: str
primary_heading: str
secondary_headings: List[HeadingItem]
word_count: Optional[int]
content_summary: str
link_counts: LinkCounts
technical_findings: List[str] = Field(default_factory=list, description="List of technical SEO issues found.")
content_opportunities: List[str] = Field(default_factory=list, description="List of immediate content opportunities.")

# Page Auditor Agent Output

class PageAuditOutput(BaseModel):
audit_results: AuditResults
target_keywords: TargetKeywords

# Auxiliary Structures for SERP Analyst

class SerpResult(BaseModel):
rank: int = Field(..., description="The organic search rank (1-10).")
title: str = Field(..., description="The title tag of the search result.")
url: str = Field(..., description="The URL of the competitor page.")
snippet: str = Field(..., description="The short description/snippet from the search result.")
content_type: str = Field(..., description="Inferred content format (e.g., blog post, landing page, video, product page).")

# SERP Analyst Agent Output

class SerpAnalysis(BaseModel):
keyword_searched: str
top_competitors: List[SerpResult]
common_title_patterns: List[str] = Field(default_factory=list, description="Common phrases or structures in the top-ranking titles.")
dominant_content_format: str = Field(..., description="The most common content format (e.g., 'How-to guides', 'Listicles').")
key_themes_and_angles: List[str] = Field(default_factory=list, description="Key topics, themes, or differentiation angles to cover.")
serp_opportunities: List[str] = Field(default_factory=list, description="Specific opportunities based on SERP analysis.")

================================================
FILE: .history/schemas_20251027182547.py
================================================

# schemas.py

from pydantic import BaseModel, Field
from typing import List, Optional

# --- ESTRUTURAS AUXILIARES PADRÃO SEO ---

class LinkCounts(BaseModel):
internal: int = Field(..., description="Number of internal links found on the page.")
external: int = Field(..., description="Number of external links found on the page.")

class HeadingItem(BaseModel):
tag: str = Field(..., description="Heading tag such as h1, h2, h3.")
text: str = Field(..., description="Text content of the heading.")

class TargetKeywords(BaseModel):
primary_keyword: str = Field(..., description="The main keyword the page is optimized for.")
search_intent: str = Field(..., description="Inferred search intent (e.g., informational, commercial, transactional).")
secondary_keywords: List[str] = Field(default_factory=list, description="A list of supporting, long-tail, or related keywords.")

class AuditResults(BaseModel):
title_tag: str
meta_description: str
primary_heading: str
secondary_headings: List[HeadingItem]
word_count: Optional[int]
content_summary: str
link_counts: LinkCounts
technical_findings: List[str] = Field(default_factory=list, description="List of technical SEO issues found.")
content_opportunities: List[str] = Field(default_factory=list, description="List of immediate content opportunities.")

# --- SAÍDAS DE AGENTES SEO ---

class PageAuditOutput(BaseModel):
audit_results: AuditResults
target_keywords: TargetKeywords

class SerpResult(BaseModel):
rank: int = Field(..., description="The organic search rank (1-10).")
title: str = Field(..., description="The title tag of the search result.")
url: str = Field(..., description="The URL of the competitor page.")
snippet: str = Field(..., description="The short description/snippet from the search result.")
content_type: str = Field(..., description="Inferred content format (e.g., blog post, landing page, video, product page).")

class SerpAnalysis(BaseModel):
keyword_searched: str
top_competitors: List[SerpResult]
common_title_patterns: List[str] = Field(default_factory=list, description="Common phrases or structures in the top-ranking titles.")
dominant_content_format: str = Field(..., description="The most common content format (e.g., 'How-to guides', 'Listicles').")
key_themes_and_angles: List[str] = Field(default_factory=list, description="Key topics, themes, or differentiation angles to cover.")
serp_opportunities: List[str] = Field(default_factory=list, description="Specific opportunities based on SERP analysis.")

# --- NOVAS ESTRUTURAS CRO/UX (ADICIONADAS) ---

class UsabilityItem(BaseModel):
area: str = Field(..., description="Area of focus (e.g., Clarity, Frictions, Mobile).")
finding: str = Field(..., description="Specific finding or issue related to the area.")

class ConversionOpportunity(BaseModel):
opportunity: str = Field(..., description="Specific, high-impact recommendation (e.g., Test new CTA copy).")
rationale: str = Field(..., description="Justification for the recommendation.")

# --- NOVA SAÍDA DO AGENTE CRO/UX ---

class CROAnalysis(BaseModel):
usability_findings: List[UsabilityItem] = Field(default_factory=list, description="Detailed findings on UX/Usability (simulated).")
conversion_friction_points: List[str] = Field(default_factory=list, description="Points in the funnel where conversion is likely dropping.")
high_impact_cro_opportunities: List[ConversionOpportunity] = Field(default_factory=list, description="Prioritized recommendations for conversion lift.")
inferred_user_journey: str = Field(..., description="The inferred steps a user takes on this page (e.g., Arrive -> Read Benefit -> Click CTA).")

================================================
FILE: .history/.env_20251024154627
================================================

================================================
FILE: .history/.env_20251024154640
================================================

# .env

# Chave API do Google Gemini (sua chave real)

GOOGLE_API_KEY=sua_chave_gemini_aqui

# Chave API do Firecrawl (sua chave real)

FIRECRAWL_API_KEY=sua_chave_firecrawl_aqui

================================================
FILE: .history/.env_20251024155721
================================================

# .env

# Chave API do Google Gemini (sua chave real)

GOOGLE_API_KEY=AIzaSyDbbPTRclMAyS4OD1gqN2c4tdBXqoCTIH0

# Chave API do Firecrawl (sua chave real)

FIRECRAWL_API_KEY=sua_chave_firecrawl_aqui

================================================
FILE: .history/.env_20251024160715
================================================

# .env

# Chave API do Google Gemini (sua chave real)

GOOGLE_API_KEY=AIzaSyDbbPTRclMAyS4OD1gqN2c4tdBXqoCTIH0

# Chave API do Firecrawl (sua chave real)

FIRECRAWL_API_KEY=fc-1dcaea4ea4ca4b948b8db5c5ceeb45c0

================================================
FILE: .history/.env_20251024163334
================================================

# .env

# Chave API do Google Gemini (sua chave real)

GOOGLE_API_KEY=AIzaSyDbbPTRclMAyS4OD1gqN2c4tdBXqoCTIH0

# Chave API do Firecrawl (sua chave real)

FIRECRAWL_API_KEY=fc-a2684ca785e3440c897f1541d067a778

================================================
FILE: .history/.env_20251024172119
================================================

# .env

# Chave API do Google Gemini (sua chave real)

GOOGLE_API_KEY=AIzaSyCVZtxr2SnIkCUP1QzYEzWW6IZaTT6IiKg

# Chave API do Firecrawl (sua chave real)

FIRECRAWL_API_KEY=fc-a2684ca785e3440c897f1541d067a778

================================================
FILE: .history/.env_20251024172701
================================================

# .env

# Chave API do Google Gemini (sua chave real)

#GOOGLE_API_KEY=AIzaSyCVZtxr2SnIkCUP1QzYEzWW6IZaTT6IiKg

================================================
FILE: .history/.env_20251027172524
================================================

# .env

# Chave API do Google Gemini (sua chave real)

GOOGLE_API_KEY=AIzaSyCVZtxr2SnIkCUP1QzYEzWW6IZaTT6IiKg

================================================
FILE: .history/.env_20251027172548
================================================

GOOGLE_API_KEY=AIzaSyCVZtxr2SnIkCUP1QzYEzWW6IZaTT6IiKg

FIRECRAWL_API_KEY=SUA_CHAVE_REAL_DO_FIRECRAWL_AQUI

================================================
FILE: .history/.env_20251027172859
================================================

GOOGLE_API_KEY=AIzaSyCVZtxr2SnIkCUP1QzYEzWW6IZaTT6IiKg

FIRECRAWL_API_KEY=fc-a2684ca785e3440c897f1541d067a778

================================================
FILE: .history/.env_20251027180503
================================================

GOOGLE_API_KEY=AIzaSyCVZtxr2SnIkCUP1QzYEzWW6IZaTT6IiKg

#FIRECRAWL_API_KEY=fc-a2684ca785e3440c897f1541d067a778

================================================
FILE: .history/.gitignore_20251024110235
================================================

================================================
FILE: .history/.gitignore_20251024110436
================================================
**pycache**
\*.pyc
venv/
