from sport_motivation.models.POSTModel import SPostData
from sport_motivation.main_files.motivation_fake_db import sport_mtv

from typing import Annotated

from fastapi import Depends


def post_pattern(
        pattern_post_data: Annotated[SPostData, Depends()]
) -> SPostData:
    sport_mtv.append(pattern_post_data)
    return pattern_post_data
