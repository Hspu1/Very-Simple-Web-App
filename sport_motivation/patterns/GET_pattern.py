from sport_motivation.models.POSTModel import SPostData
from sport_motivation.patterns.GET_DELETE_pattern1 import get_delete_pattern1


def get_pattern(pattern_obj: SPostData | dict | bool, pattern_id: int):
    # validation
    return pattern_obj if pattern_obj else get_delete_pattern1(
                    pattern_id=pattern_id, custom_message="(too large)")
