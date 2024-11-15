from sport_motivation.models.POSTModel import SPostData
from sport_motivation.models.PUTModel import SPutData

from sport_motivation.patterns.GET_pattern1 import get_pattern1


def get_pattern3(
        pattern_obj: SPostData | dict | bool, pattern_id: int
                ) -> dict | SPostData | SPutData | bool | dict[str, str]:
    return pattern_obj if pattern_obj \
        else get_pattern1(pattern_id=pattern_id, custom_message="(too large)")
