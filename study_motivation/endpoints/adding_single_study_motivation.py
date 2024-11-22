from main_files.motivation_fake_dbs import study_mtv

from main_files.main_patterns.POST_pattern import post_pattern
from study_motivation.patterns.POST_study_pattern import post_study_pattern

from study_motivation.models.POSTStudyModel import SPostStudy

from typing import Annotated

from fastapi import Depends


def adding_single_study_mtv(
        endpoint_post_data: Annotated[SPostStudy, Depends()]
) -> SPostStudy | str:
    entered_study_mtv_id = list(endpoint_post_data)[0][1]

    return post_study_pattern(pattern_post_data=endpoint_post_data) \
        if (not study_mtv and entered_study_mtv_id == 1
            or len(study_mtv) + 1 == entered_study_mtv_id) \
        else post_pattern(mtv_id=entered_study_mtv_id)
