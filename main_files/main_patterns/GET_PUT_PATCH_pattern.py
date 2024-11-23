def get_put_patch_pattern(correction: str, mtv_id: int,
                          custom_message: str = "") -> dict[str, str]:
    return {
        "status": "Index Error",
        "feedback": f"The entered {correction}_mtv_id ({mtv_id}) "                   
                    f"isn`t in the database{custom_message}"
    }
