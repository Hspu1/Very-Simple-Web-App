from sport_motivation.main_files.motivation_fake_db import sport_mtv


def endpoint_deleting_all_motivation() -> str:
    sport_mtv.clear()
    return f"the data was successfully deleted"
