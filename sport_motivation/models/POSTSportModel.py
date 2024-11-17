from pydantic import BaseModel, Field


class SPostSport(BaseModel):
    sport_mtv_id: int = Field(ge=1)
    message: str = "your sport motivation"
