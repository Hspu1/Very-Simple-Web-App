from main_files.motivation_fake_dbs import sport_mtv

from pydantic import BaseModel, Field


class SPutSport(BaseModel):
    sport_mtv_id: int = Field(ge=int(dict(sport_mtv[0]).get("sport_mtv_id")))
    message: str = "your sport motivation"
