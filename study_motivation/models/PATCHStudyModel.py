from pydantic import BaseModel, Field


class SPatchStudy(BaseModel):
    study_mtv_id: int = Field(ge=1)
