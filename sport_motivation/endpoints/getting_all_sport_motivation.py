from main_files.motivation_fake_dbs import sport_mtv


def getting_all_sport_mtv() -> list | str:
    return sport_mtv if sport_mtv else f"there is no data in the database"
