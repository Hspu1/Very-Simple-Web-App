from sport_motivation.models.POSTSportModel import SPostSport
from sport_motivation.models.PUTSportModel import SPutSport
from study_motivation.models.POSTStudyModel import SPostStudy


def put_patch_response(
        custom_message: str,
        old_data: dict | SPostSport | SPutSport | SPostStudy,
        new_data: dict | SPostSport | SPutSport | SPostStudy
                    ) -> dict[
                str, str | dict | SPostSport | SPutSport | SPostStudy]:
    return {
            "info": custom_message,
            "old_data": old_data,
            "new_data": new_data
        }
