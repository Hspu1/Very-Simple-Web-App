from sport_motivation.models.POSTSportModel import SPostSport
from main_files.motivation_fake_dbs import sport_mtv

from typing import Annotated

from fastapi import Depends


def post_sport_pattern(
        pattern_post_data: Annotated[SPostSport, Depends()]
) -> SPostSport:
    sport_mtv.append(pattern_post_data)
    return pattern_post_data
