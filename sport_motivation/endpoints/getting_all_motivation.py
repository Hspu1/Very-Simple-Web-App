from sport_motivation.main_files.motivation_fake_db import sport_mtv


def endpoint_getting_all_motivation() -> list | str:
    return sport_mtv if sport_mtv \
        else f"no data (sport_mtv = {sport_mtv})"
