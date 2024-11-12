from sport_motivation.patterns.DELETE_pattern import delete_pattern
from sport_motivation.patterns.GET_DELETE_pattern1 import get_delete_pattern1
from sport_motivation.patterns.GET_DELETE_pattern2 import get_delete_pattern2
from main_files.motivation_fake_db import sport_mtv


def endpoint_deleting_single_motivation(mtv_id: int):
    # validation
    get_delete_pattern2_obj = deleted_data = (
                            get_delete_pattern2(pattern_id=mtv_id))

    if mtv_id <= 0:
        return get_delete_pattern1(pattern_id=mtv_id,
                                   custom_message="(too small)")
    try:
        sport_mtv[mtv_id - 1]

    except IndexError:
        if get_delete_pattern2_obj:
            sport_mtv.remove(get_delete_pattern2_obj)
            return delete_pattern(deleted_data=deleted_data)

        return get_delete_pattern1(pattern_id=mtv_id,
                                            custom_message="(too large)")

    else:
        if get_delete_pattern2_obj:
            sport_mtv.remove(get_delete_pattern2_obj)
            return delete_pattern(deleted_data=deleted_data)

    return get_delete_pattern1(pattern_id=mtv_id,
                                            custom_message="(too large)")
