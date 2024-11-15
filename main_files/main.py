from sport_motivation.endpoints.getting_all_motivation import (
    endpoint_getting_all_motivation)
from sport_motivation.endpoints.getting_single_motivation import (
    endpoint_getting_single_motivation)
from sport_motivation.endpoints.adding_single_motivation import (
    endpoint_adding_single_motivation)
from sport_motivation.endpoints.changing_single_motivation import (
    endpoint_changing_single_motivation)
from sport_motivation.endpoints.deleting_all_motivation import (
    endpoint_deleting_all_motivation)

from sport_motivation.models.POSTModel import SPostData
from sport_motivation.models.PUTModel import SPutData

from typing import Annotated

from fastapi import FastAPI, Depends

app = FastAPI(
    title="Motivation"
)


@app.get(tags=["sport_motivation"], path="/getting_all_motivation_data")
def getting_all_motivation_data() -> dict[str, int | list | str]:
    return {
        "status": 200,
        "all_data": endpoint_getting_all_motivation()
    }


@app.get(tags=["sport_motivation"],
         path="/getting_motivation_data{sport_mtv_id}")
def getting_motivation_data(sport_mtv_id: int) -> dict[
                            str, str] | dict | SPostData | SPutData | bool:
    return endpoint_getting_single_motivation(mtv_id=sport_mtv_id)


@app.post(tags=["sport_motivation"], path="/adding_motivation_data")
def adding_motivation_data(post_data: Annotated[SPostData, Depends()]
                           ) -> dict[str, int | (SPostData | str)]:
    return {
        "status": 200,
        "entered_data":
            endpoint_adding_single_motivation(endpoint_post_data=post_data)
    }


@app.put(tags=["sport_motivation"], path="/changing_motivation_data")
def changing_motivation_data(
        put_data: Annotated[SPutData, Depends()]
):
    # validation# validation# validation# validation# validation# validation# validation# validation
    return endpoint_changing_single_motivation(endpoint_put_data=put_data)


@app.delete(tags=["sport_motivation"], path="/deleting_all_motivation_data")
def deleting_all_motivation_data() -> dict[str, int | str]:
    return {
        "status": 200,
        "feedback": endpoint_deleting_all_motivation()
    }
