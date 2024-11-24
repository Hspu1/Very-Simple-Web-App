from main_files.motivation_fake_dbs import sport_mtv

from main_files.responses.GET_POST_PUT_PATCH_response import (
    get_post_put_patch_response)

from sport_motivation.models.POSTSportModel import SPostSport

from typing import Annotated

from fastapi import Depends


def adding_single_sport_mtv(
        endpoint_post_data: Annotated[SPostSport, Depends()]
) -> dict[str, str | SPostSport]:
    entered_sport_mtv_id = list(endpoint_post_data)[0][1]

    if (not sport_mtv and entered_sport_mtv_id == 1
            or len(sport_mtv) + 1 == entered_sport_mtv_id):
        sport_mtv.append(endpoint_post_data)
        return {
            "info": "the data has been successfully added to the database",
            "entered_data": endpoint_post_data
        }

    return get_post_put_patch_response(correction="sport",
                                       mtv_id=entered_sport_mtv_id,
                                       custom_message="is already in the database")
