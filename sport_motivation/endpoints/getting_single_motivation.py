from sport_motivation.models.POSTModel import SPostData
from sport_motivation.models.PUTModel import SPutData

from sport_motivation.patterns.GET_pattern1 import get_pattern1
from sport_motivation.patterns.GET_pattern2 import get_pattern2
from sport_motivation.patterns.GET_pattern3 import get_pattern3


def endpoint_getting_single_motivation(mtv_id: int) -> dict[
                            str, str] | dict | SPostData | SPutData | bool:
    get_delete_pattern2_obj = get_pattern2(pattern_id=mtv_id)
    if mtv_id <= 0:
        return get_pattern1(pattern_id=mtv_id, custom_message="(too small)")

    return get_pattern3(pattern_obj=get_delete_pattern2_obj, pattern_id=mtv_id)
