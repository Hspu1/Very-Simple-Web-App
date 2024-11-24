from main_files.motivation_fake_dbs import sport_mtv

from main_files.patterns.GET_POST_PUT_PATCH_pattern import (
    get_post_put_patch_pattern)
from main_files.patterns.PUT_PATCH_pattern import put_patch_pattern

from sport_motivation.models.POSTSportModel import SPostSport
from sport_motivation.models.PUTSportModel import SPutSport

from typing import Annotated

from fastapi import Depends


def changing_sport_mtv(endpoint_put_data: Annotated[SPutSport, Depends()]
) -> dict[str, str | dict | SPostSport | SPutSport]:
    entered_mtv_sport_id = list(endpoint_put_data)[0][1]

    for sport_mtv_data in sport_mtv:
        if dict(sport_mtv_data).get("sport_mtv_id") == entered_mtv_sport_id:
            old_data = sport_mtv_data
            sport_mtv.remove(sport_mtv_data)
            sport_mtv.insert(entered_mtv_sport_id - 1, endpoint_put_data)

            return put_patch_pattern(
                custom_message="the new data has successfully "
                               "replaced the old ones",
                old_data=old_data,
                new_data=endpoint_put_data
            )

    return get_post_put_patch_pattern(correction="sport",
                                      mtv_id=entered_mtv_sport_id,
                                      custom_message="isn`t in the database")
