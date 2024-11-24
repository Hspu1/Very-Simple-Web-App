from main_files.motivation_fake_dbs import study_mtv

from main_files.responses.GET_POST_PUT_PATCH_response import (
    get_post_put_patch_response)
from main_files.responses.PUT_PATCH_response import put_patch_response

from study_motivation.models.PATCHStudyModel import SPatchStudy
from study_motivation.models.POSTStudyModel import SPostStudy

from typing import Annotated

from fastapi import Depends


def hiding_message_study_mtv(study_mtv_id: Annotated[SPatchStudy, Depends()]
                ) -> dict[str, str | dict | SPostStudy]:
    int_study_mtv_id = list(study_mtv_id)[0][1]

    new_data = {
        "study_mtv_id": int_study_mtv_id,
        "message": "the message was hidden by the author"
    }

    for study_mtv_data in study_mtv:
        study_mtv_data_id = dict(study_mtv_data).get("study_mtv_id")

        if study_mtv_data_id == int_study_mtv_id:
            old_data = study_mtv_data
            study_mtv.remove(study_mtv_data)
            study_mtv.insert(int_study_mtv_id - 1, new_data)

            return put_patch_response(
                custom_message="The message has been successfully hidden",
                old_data=old_data, new_data=new_data)

    return get_post_put_patch_response(correction="study",
                                       mtv_id=int_study_mtv_id,
                                       custom_message="isn`t in the database")
