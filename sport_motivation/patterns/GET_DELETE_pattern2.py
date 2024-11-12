from main_files.motivation_fake_db import sport_mtv


def get_delete_pattern2(pattern_id: int):
    # validation
    for sport_mtv_data in sport_mtv:
        if int(dict(sport_mtv_data).get("sport_mtv_id")) == pattern_id:
            return sport_mtv_data
    return False
