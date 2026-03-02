# tools/layout_engine.py

from enum import Enum


class SlideType(str, Enum):
    TITLE_ONLY = "title_only"
    BULLET = "bullet"
    CHART = "chart"
    MIXED = "mixed"

def detect_slide_type(slide_spec):
    has_bullets = bool(slide_spec.bullets)
    has_chart = slide_spec.chart is not None

    if has_chart and has_bullets:
        return SlideType.MIXED
    elif has_chart:
        return SlideType.CHART
    elif has_bullets:
        return SlideType.BULLET
    else:
        return SlideType.TITLE_ONLY

def choose_layout(prs, slide_type: SlideType):
    if slide_type == SlideType.CHART:
        return prs.slide_layouts[5]  # Title Only

    if slide_type == SlideType.BULLET:
        return prs.slide_layouts[1]  # Title + Content

    if slide_type == SlideType.MIXED:
        return prs.slide_layouts[3]  # Two Content

    return prs.slide_layouts[5]  # default safe