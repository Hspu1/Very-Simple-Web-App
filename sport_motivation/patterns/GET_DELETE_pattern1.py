def get_delete_pattern1(
        pattern_id: int, custom_message: str
                        ):
    # validation
    return {
        "status": "Index Error",
        "feedback": f"The entered sport_mtv_id ({pattern_id}) "                   
                    f"isn`t in the database {custom_message}"
    }
