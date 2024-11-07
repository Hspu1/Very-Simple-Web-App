from sport_motivation.models.POSTModel import SPostData

from typing import Annotated

from fastapi import Depends


def delete_pattern(
        deleted_data: Annotated[SPostData, Depends()]
) -> dict[str, int | str | SPostData]:
    return {
        "status": 200,
        "feedback": "the data by sport_mtv_id was successfully deleted",
        "deleted_data": deleted_data
    }
