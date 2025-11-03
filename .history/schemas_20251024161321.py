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