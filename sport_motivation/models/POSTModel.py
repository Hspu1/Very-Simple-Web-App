from pydantic import BaseModel, Field


class SPostData(BaseModel):
    sport_mtv_id: int = Field(ge=1)
    message: str = "your motivation"
