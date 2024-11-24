from pydantic import BaseModel, Field


class SGetSport(BaseModel):
    sport_mtv_id: int = Field(ge=1)
