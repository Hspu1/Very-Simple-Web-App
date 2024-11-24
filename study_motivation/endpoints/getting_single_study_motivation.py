from main_files.motivation_fake_dbs import study_mtv

from main_files.patterns.GET_POST_PUT_PATCH_pattern import (
    get_post_put_patch_pattern)

from study_motivation.models.GETStudyModel import SGetStudy
from study_motivation.models.POSTStudyModel import SPostStudy
from study_motivation.models.PATCHStudyModel import SPatchStudy

from typing import Annotated

from fastapi import Depends


def getting_single_study_mtv(study_mtv_id: Annotated[SGetStudy, Depends()]
                             ) -> dict | SPostStudy | SPatchStudy:
    int_study_mtv_id = list(study_mtv_id)[0][1]

    for study_mtv_data in study_mtv:
        if (dict(study_mtv_data).get("study_mtv_id") == int_study_mtv_id
                or list(study_mtv_data)[0][1] == int_study_mtv_id):
            return study_mtv_data

    return get_post_put_patch_pattern(correction="study",
                                      mtv_id=int_study_mtv_id,
                                      custom_message="isn`t in the database")
