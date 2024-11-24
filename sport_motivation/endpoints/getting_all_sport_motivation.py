from main_files.motivation_fake_dbs import sport_mtv


def getting_all_sport_mtv() -> list | dict[str, str]:
    return sport_mtv if sport_mtv \
        else {
        "info": "there is no data in the database"
    }
