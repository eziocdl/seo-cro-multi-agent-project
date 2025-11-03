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


 





