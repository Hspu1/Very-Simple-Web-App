from main_files.main_patterns.GET_pattern import get_pattern
from main_files.motivation_fake_dbs import study_mtv


def get_study_pattern(pattern_id: int):
    for study_mtv_data in study_mtv:
        if int(dict(study_mtv_data).get("study_mtv_id")) == pattern_id:
            return study_mtv_data

    return get_pattern(pattern_id=pattern_id, custom_message="(too large)")
