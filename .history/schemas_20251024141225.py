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




