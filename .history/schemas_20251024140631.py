from pydantic import BaseModel, Field
from typing import List, Optional

class LinkCounts(BaseModel):
  internal: int = Field(..., description="Number of Internal links found on the page")
  external: int = Field(..., description="Number of External links found on the page")

class HeadingItem(BaseModel):
  internal: int = Field(..., description="Number of internal links found on the page")
  external: int = Field(..., description="Number of external links found on the page")

class HeadingItem(BaseModel);


