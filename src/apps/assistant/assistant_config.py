def get_placeholder_assistant_config(model_name):
    return {
        "name": "placeholder",  # directory name under /content/prompts/v1 (regardless of version)
        "model_name": model_name,
        "system_content_version": 1,
        "user_content_version": 1,
    }


def get_tech_assistant_config(model_name):
    return {
        "name": "tech",
        "model_name": model_name,  # ModelProvider?
        "system_content_version": 1,
        "user_content_version": 1,
    }


def get_writing_assistant_config(model_name):
    return {
        "name": "writing",
        "model_name": model_name,
        "system_content_version": 1,
        "user_content_version": 1,
    }
