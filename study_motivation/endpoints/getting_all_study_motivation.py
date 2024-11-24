from main_files.motivation_fake_dbs import study_mtv


def getting_all_study_mtv() -> list | dict[str, str]:
    return study_mtv if study_mtv \
        else {
        "info": "there is no data in the database"
    }
