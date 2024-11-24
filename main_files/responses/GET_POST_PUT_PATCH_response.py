def get_post_put_patch_response(correction: str, mtv_id: int,
                               custom_message: str = "") -> dict[str, str]:
    return {
        "problem": "Index Error",
        "info": f"The entered {correction}_mtv_id ({mtv_id}) {custom_message}"
    }
