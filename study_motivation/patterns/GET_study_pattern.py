from main_files.motivation_fake_dbs import study_mtv

from main_files.main_patterns.GET_pattern import get_pattern

from study_motivation.models.POSTStudyModel import SPostStudy


def get_study_pattern(pattern_id: int) -> dict | SPostStudy | dict[str, str]:
    for study_mtv_data in study_mtv:
        if (dict(study_mtv_data).get("study_mtv_id") == pattern_id
                or list(study_mtv_data)[0][1] == pattern_id):
            return study_mtv_data

    return get_pattern(pattern_id=pattern_id, custom_message="(too large)")
