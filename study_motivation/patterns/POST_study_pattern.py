from main_files.motivation_fake_dbs import study_mtv

from study_motivation.models.POSTStudyModel import SPostStudy

from typing import Annotated

from fastapi import Depends


def post_study_pattern(
        pattern_post_data: Annotated[SPostStudy, Depends()]
):
    # validation
    study_mtv.append(pattern_post_data)
    return pattern_post_data
