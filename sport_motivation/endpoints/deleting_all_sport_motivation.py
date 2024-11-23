from main_files.motivation_fake_dbs import sport_mtv


def deleting_all_sport_mtv() -> str:
    sport_mtv.clear()
    return f"all data has been successfully deleted"
