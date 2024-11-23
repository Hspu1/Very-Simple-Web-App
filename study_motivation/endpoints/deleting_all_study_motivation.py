from main_files.motivation_fake_dbs import study_mtv


def deleting_all_study_mtv() -> str:
    study_mtv.clear()
    return f"all data has been successfully deleted"
