from pydantic import BaseModel, Field


class SPutSport(BaseModel):
    sport_mtv_id: int = Field(ge=1)
    message: str = "your sport motivation"
