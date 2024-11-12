from sport_motivation.models.PUTModel import SPutData
from sport_motivation.patterns.PUT_pattern import put_pattern
from main_files.motivation_fake_db import sport_mtv

from typing import Annotated

from fastapi import Depends


def endpoint_changing_single_motivation(
        endpoint_put_data: Annotated[SPutData, Depends()]):
    # validation    e
    entered_mtv_sport_id = list(endpoint_put_data)[0][1]

    for sport_mtv_data in sport_mtv:
        if dict(sport_mtv_data).get("sport_mtv_id") == entered_mtv_sport_id:
            old_data = sport_mtv_data
            sport_mtv.remove(sport_mtv_data)
            sport_mtv.insert(entered_mtv_sport_id - 1, endpoint_put_data)

            return put_pattern(num=1, pattern_id=entered_mtv_sport_id,
                               old_pattern_data=old_data,
                               new_pattern_data=endpoint_put_data)

    return put_pattern(num=0, pattern_id=entered_mtv_sport_id)
