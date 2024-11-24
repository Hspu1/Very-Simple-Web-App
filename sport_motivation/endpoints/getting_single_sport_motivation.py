from main_files.motivation_fake_dbs import sport_mtv

from main_files.responses.GET_POST_PUT_PATCH_response import (
    get_post_put_patch_response)

from sport_motivation.models.GETSportModel import SGetSport
from sport_motivation.models.POSTSportModel import SPostSport
from sport_motivation.models.PUTSportModel import SPutSport

from typing import Annotated

from fastapi import Depends


def getting_single_sport_mtv(sport_mtv_id: Annotated[SGetSport, Depends()]
                             ) -> dict | SPostSport | SPutSport:
    int_sport_mtv_id = list(sport_mtv_id)[0][1]

    for sport_mtv_data in sport_mtv:
        if (dict(sport_mtv_data).get("sport_mtv_id") == int_sport_mtv_id
                or list(sport_mtv_data)[0][1] == int_sport_mtv_id):
            return sport_mtv_data

    return get_post_put_patch_response(correction="sport",
                                       mtv_id=int_sport_mtv_id,
                                       custom_message="isn`t in the database")
