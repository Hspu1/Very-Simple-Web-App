from pydantic import BaseModel, Field


class SGetStudy(BaseModel):
    study_mtv_id: int = Field(ge=1)
