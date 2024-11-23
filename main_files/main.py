from sport_motivation.endpoints.getting_all_sport_motivation import (
    getting_all_sport_mtv)
from sport_motivation.endpoints.getting_single_sport_motivation import (
    getting_single_sport_mtv)
from sport_motivation.endpoints.adding_single_sport_motivation import (
    adding_single_sport_mtv)
from sport_motivation.endpoints.changing_sport_motivation import (
    changing_sport_mtv)
from sport_motivation.endpoints.deleting_all_sport_motivation import (
    deleting_all_sport_mtv)

from sport_motivation.models.POSTSportModel import SPostSport
from sport_motivation.models.PUTSportModel import SPutSport

from study_motivation.endpoints.getting_all_study_motivation import (
    getting_all_study_mtv)
from study_motivation.endpoints.getting_single_study_motivation import (
    getting_single_study_mtv)
from study_motivation.endpoints.adding_single_study_motivation import (
    adding_single_study_mtv)
from study_motivation.endpoints.hiding_message_study_motivation import (
    hiding_message_study_mtv)
from study_motivation.endpoints.deleting_all_study_motivation import (
    deleting_all_study_mtv)

from study_motivation.models.POSTStudyModel import SPostStudy

from typing import Annotated

from fastapi import FastAPI, Depends

app = FastAPI(
    title="Motivation"
)


@app.get(tags=["sport_motivation"], path="/getting_all_sport_motivation")
def getting_all_sport_motivation() -> dict[str, int | list | str]:

    return {
        "status": 200,
        "all_data": getting_all_sport_mtv()
    }


@app.get(tags=["sport_motivation"],
         path="/getting_sport_motivation{sport_mtv_id}")
def getting_sport_motivation(sport_mtv_id: int) -> dict[
                                str, str] | dict | SPostSport | SPutSport:
    return {
        "status": 200,
        "data": getting_single_sport_mtv(mtv_id=sport_mtv_id)
    }


@app.post(tags=["sport_motivation"], path="/adding_sport_motivation")
def adding_sport_motivation(post_data: Annotated[SPostSport, Depends()]
                           ) -> dict[str, int | SPostSport | str]:
    return {
        "status": 200,
        "entered_data":
            adding_single_sport_mtv(endpoint_post_data=post_data)
    }


@app.put(tags=["sport_motivation"], path="/changing_sport_motivation")
def changing_sport_motivation(
        put_data: Annotated[SPutSport, Depends()]
) -> dict[str, int | str | dict | SPostSport | SPutSport]:

    return changing_sport_mtv(endpoint_put_data=put_data)


@app.delete(tags=["sport_motivation"], path="/deleting_all_sport_motivation")
def deleting_all_sport_motivation() -> dict[str, int | str]:

    return {
        "status": 200,
        "feedback": deleting_all_sport_mtv()
    }



@app.get(tags=["study_motivation"], path="/getting_all_study_motivation")
def getting_all_study_motivation() -> dict[str, int | list | str]:

    return {
        "status": 200,
        "all_data": getting_all_study_mtv()
    }


@app.get(tags=["study_motivation"],
         path="/getting_study_motivation{study_mtv_id}")
def getting_study_motivation(study_mtv_id: int) -> dict[
                            str, int | dict[str, str] | dict | SPostStudy]:
    return {
        "status": 200,
        "data": getting_single_study_mtv(mtv_id=study_mtv_id)
    }


@app.post(tags=["study_motivation"], path="/adding_study_motivation")
def adding_study_motivation(post_data: Annotated[SPostStudy, Depends()]
                            ) -> dict[str, int | SPostStudy | str]:
    return {
        "status": 200,
        "entered_data":
            adding_single_study_mtv(endpoint_post_data=post_data)
    }


@app.patch(tags=["study_motivation"], path="/hiding_message_study_motivation")
def hiding_message_study_motivation(study_mtv_id: int) -> dict[
                        str, int | str | dict | SPostStudy] | dict[str, str]:

    return hiding_message_study_mtv(mtv_id=study_mtv_id)


@app.delete(tags=["study_motivation"], path="/deleting_all_study_motivation")
def deleting_all_study_motivation() -> dict[str, int | str]:

    return {
        "status": 200,
        "feedback": deleting_all_study_mtv()
    }
