from pydantic import BaseModel
from typing import List, Optional
from schemas.chart_spec import ChartSpec


class SlideSpec(BaseModel):
    title: str
    bullets: List[str] = []
    chart: Optional[ChartSpec] = None


class DeckSpec(BaseModel):
    slides: List[SlideSpec]