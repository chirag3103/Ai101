def get_tech_assistant_config(model_name):
    return {
        "name": "tech_buddy",
        "model_name": model_name,  # ModelProvider?
        "system_content_version": 1,
        "user_content_version": 1,
    }


def get_writing_assistant_config(model_name):
    return {
        "name": "writing_buddy",
        "model_name": model_name,  # ModelProvider?
        "system_content_version": 1,
        "user_content_version": 1,
    }
