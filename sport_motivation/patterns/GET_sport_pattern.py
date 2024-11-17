from main_files.motivation_fake_dbs import sport_mtv

from main_files.main_patterns.GET_pattern import get_pattern

from sport_motivation.models.POSTSportModel import SPostSport
from sport_motivation.models.PUTSportModel import SPutSport


def get_sport_pattern(pattern_id: int
                       ) -> dict | SPostSport | SPutSport | bool:
    for sport_mtv_data in sport_mtv:
        if (dict(sport_mtv_data).get("sport_mtv_id") == pattern_id
                or list(sport_mtv_data)[0][1] == pattern_id):
            return sport_mtv_data

    return get_pattern(pattern_id=pattern_id, custom_message="(too large)")
