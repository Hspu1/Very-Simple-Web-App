from pydantic import BaseModel, Field


class SPostStudy(BaseModel):
    study_mtv_id: int = Field(ge=1)
    message: str = "your study motivation"
