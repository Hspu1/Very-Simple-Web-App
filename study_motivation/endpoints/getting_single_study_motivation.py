from main_files.main_patterns.GET_PUT_PATCH_pattern import (
    get_put_patch_pattern)
from study_motivation.patterns.GET_study_pattern import get_study_pattern

from study_motivation.models.POSTStudyModel import SPostStudy


def getting_single_study_mtv(mtv_id: int) -> dict[
                                str, str] | dict | SPostStudy:
    return get_put_patch_pattern(correction="study", mtv_id=mtv_id,
                                 custom_message=" (too small)") \
        if mtv_id <= 0 \
        else get_study_pattern(pattern_id=mtv_id)
