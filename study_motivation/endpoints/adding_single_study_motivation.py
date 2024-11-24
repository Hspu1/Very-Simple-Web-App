from main_files.motivation_fake_dbs import study_mtv

from main_files.responses.GET_POST_PUT_PATCH_response import (
    get_post_put_patch_response)

from study_motivation.models.POSTStudyModel import SPostStudy

from typing import Annotated

from fastapi import Depends


def adding_single_study_mtv(
        endpoint_post_data: Annotated[SPostStudy, Depends()]
) -> dict[str, str | SPostStudy]:
    entered_study_mtv_id = list(endpoint_post_data)[0][1]

    if (not study_mtv and entered_study_mtv_id == 1
            or len(study_mtv) + 1 == entered_study_mtv_id):
        study_mtv.append(endpoint_post_data)
        return {
            "info": "the data has been successfully added to the database",
            "entered_data": endpoint_post_data
        }

    return get_post_put_patch_response(correction="study",
                                       mtv_id=entered_study_mtv_id,
                                       custom_message="is already in the database")
