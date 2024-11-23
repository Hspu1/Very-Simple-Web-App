from study_motivation.models.POSTStudyModel import SPostStudy

from main_files.main_patterns.PUT_PATCH_pattern import put_patch_pattern


def patch_pattern(
        old_pattern_data: dict | SPostStudy,
        new_pattern_data: dict | SPostStudy
                ) -> dict[str, int | str | dict | SPostStudy]:

    return put_patch_pattern(
        custom_message="The message has been successfully hidden",
        old_data=old_pattern_data,
        new_data=new_pattern_data
    )
