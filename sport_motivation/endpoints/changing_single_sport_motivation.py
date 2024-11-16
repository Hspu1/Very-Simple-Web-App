from sport_motivation.models.POSTSportModel import SPostSport
from sport_motivation.models.PUTSportModel import SPutSport

from sport_motivation.patterns.PUT_sport_pattern import put_sport_pattern
from main_files.motivation_fake_dbs import sport_mtv

from typing import Annotated

from fastapi import Depends


def changing_single_sport_motivation(
        endpoint_put_data: Annotated[SPutSport, Depends()]
) -> dict[str, int | str | dict | SPostSport | SPutSport]:
    entered_mtv_sport_id = list(endpoint_put_data)[0][1]

    for sport_mtv_data in sport_mtv:
        if dict(sport_mtv_data).get("sport_mtv_id") == entered_mtv_sport_id:
            old_data = sport_mtv_data
            sport_mtv.remove(sport_mtv_data)
            sport_mtv.insert(entered_mtv_sport_id - 1, endpoint_put_data)

            return put_sport_pattern(num=1, pattern_id=entered_mtv_sport_id,
                                     old_pattern_data=old_data,
                                     new_pattern_data=endpoint_put_data)

    return put_sport_pattern(num=0, pattern_id=entered_mtv_sport_id)
