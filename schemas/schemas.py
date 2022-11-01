from typing import Optional

from pydantic import BaseModel


class Country(BaseModel):
    countries: list[str]

    class Config:
        schema_extra = {
            "example": {
                "countries": ["turkey", "india", "australia"],
            }
        }


class University(BaseModel):
    country: Optional[str] = None
    web_pages: list[str] = []
    name: Optional[str] = None
    alpha_two_code: Optional[str] = None
    domains: list[str] = []
