from pydantic import BaseModel, Field
from typing import List


class ChartSpec(BaseModel):
    type: str = Field(description="Chart type: bar, column, line")
    title: str
    categories: List[str]
    values: List[float]

    def validate_lengths(self):
        if len(self.categories) != len(self.values):
            raise ValueError("Categories and values must match length.")