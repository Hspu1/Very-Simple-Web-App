from main_files.motivation_fake_db import sport_mtv

from sport_motivation.models.POSTModel import SPostData
from sport_motivation.models.PUTModel import SPutData


def get_pattern2(pattern_id: int) -> dict | SPostData | SPutData | bool:
    for sport_mtv_data in sport_mtv:
        if int(dict(sport_mtv_data).get("sport_mtv_id")) == pattern_id:
            return sport_mtv_data
    return False
