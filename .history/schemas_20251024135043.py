from pydantic import BaseModel, Field
from typing import List, Optional


#-- Estruturas auxiliares para o Page Auditor ---
class LinkCounts(BaseModel);
  internal: int = Field(..., description="Number of Internal links found on the ")