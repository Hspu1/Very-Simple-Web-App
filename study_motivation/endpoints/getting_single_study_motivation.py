from main_files.main_patterns.GET_pattern import get_pattern

from study_motivation.patterns.GET_study_pattern import get_study_pattern


def getting_single_study_motivation(mtv_id: int):
    # validation
    return get_pattern(
        pattern_id=mtv_id, custom_message="(too small)") if mtv_id <= 0 \
        else get_study_pattern(pattern_id=mtv_id)
