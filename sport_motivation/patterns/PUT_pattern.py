from sport_motivation.models.POSTModel import SPostData
from sport_motivation.models.PUTModel import SPutData


def put_pattern(num: int, pattern_id: int, old_pattern_data=None,
                new_pattern_data=None
                    ) -> dict[str, int | str | dict | SPostData | SPutData]:
    if num:
        return {
            "status": 200,
            "feedback": "the new data has successfully replaced the old ones",
            "old_data": old_pattern_data,
            "new_data": new_pattern_data
        }

    return {
        "status": "unable to change a message",
        "feedback": f"sport_mtv_id ({pattern_id}) "
                    f"isn`t in the database"
    }
