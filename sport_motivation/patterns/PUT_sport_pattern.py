from sport_motivation.models.POSTSportModel import SPostSport
from sport_motivation.models.PUTSportModel import SPutSport

from main_files.main_patterns.GET_PUT_PATCH_pattern import (
    get_put_patch_pattern)
from main_files.main_patterns.PUT_PATCH_pattern import put_patch_pattern


def put_sport_pattern(
        num: int, pattern_id: int,
        old_pattern_data: dict | SPostSport | SPutSport = None,
        new_pattern_data: dict | SPostSport | SPutSport = None
                ) -> dict[str, int | str | dict | SPostSport | SPutSport]:
    if num:
        return put_patch_pattern(
            custom_message="the new data has successfully "
                           "replaced the old ones",
            old_data=old_pattern_data,
            new_data=new_pattern_data
        )

    return get_put_patch_pattern(correction="sport", mtv_id=pattern_id)
