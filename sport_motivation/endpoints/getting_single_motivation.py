from sport_motivation.main_files.motivation_fake_db import sport_mtv
from sport_motivation.patterns.GET_pattern import get_pattern
from sport_motivation.patterns.GET_DELETE_pattern1 import get_delete_pattern1
from sport_motivation.patterns.GET_DELETE_pattern2 import get_delete_pattern2


def endpoint_getting_single_motivation(mtv_id: int):
    # validation
    get_delete_pattern2_obj = get_delete_pattern2(pattern_id=mtv_id)
    if mtv_id <= 0:
        return get_delete_pattern1(pattern_id=mtv_id,
                                            custom_message="(too small)")

    return get_pattern(pattern_obj=get_delete_pattern2_obj, pattern_id=mtv_id)
