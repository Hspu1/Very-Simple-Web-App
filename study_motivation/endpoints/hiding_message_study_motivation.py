from main_files.motivation_fake_dbs import study_mtv

from main_files.main_patterns.GET_PUT_PATCH_pattern import (
    get_put_patch_pattern)
from study_motivation.patterns.PATCH_study_pattern import patch_pattern

from study_motivation.models.POSTStudyModel import SPostStudy


def hiding_message_study_mtv(mtv_id: int) -> dict[
                        str, int | str | dict | SPostStudy] | dict[str, str]:
    new_data = {
        "study_mtv_id": mtv_id,
        "message": "the message was hidden by the author"
    }

    for study_mtv_data in study_mtv:
        study_mtv_data_id = dict(study_mtv_data).get("study_mtv_id")

        if study_mtv_data_id == mtv_id:
            old_data = study_mtv_data
            study_mtv.remove(study_mtv_data)
            study_mtv.insert(mtv_id - 1, new_data)

            return patch_pattern(old_pattern_data=old_data,
                                 new_pattern_data=new_data)

    return get_put_patch_pattern(correction="study", mtv_id=mtv_id)
