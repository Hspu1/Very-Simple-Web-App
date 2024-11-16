from main_files.main_patterns.GET_pattern import get_pattern

from sport_motivation.models.POSTSportModel import SPostSport
from sport_motivation.models.PUTSportModel import SPutSport

from sport_motivation.patterns.GET_sport_pattern import get_sport_pattern


def getting_single_sport_motivation(mtv_id: int) -> dict[
                            str, str] | dict | SPostSport | SPutSport | bool:
    return get_pattern(
        pattern_id=mtv_id, custom_message="(too small)") if mtv_id <= 0 \
        else get_sport_pattern(pattern_id=mtv_id)
