from apps.assistant.assistant_config import get_tech_assistant_config, get_writing_assistant_config, \
    get_placeholder_assistant_config
from apps.assistant.base_open_ai_assistant import BaseOpenAiAssistant


class AssistantProvider(BaseOpenAiAssistant):

    def __init__(self, assistant):
        self.validate_assistant_type(assistant)

    @staticmethod
    def validate_assistant_type(assistant):
        if assistant not in ['placeholder', 'tech', 'writing', 'life_simulation']:
            raise ValueError(f"Assistant '{assistant}' is not supported.")

    @staticmethod
    def get_placeholder_assistant(model_name="gpt-4o-mini"):
        assistant_config = get_placeholder_assistant_config(model_name)
        return BaseOpenAiAssistant(assistant_config)

    @staticmethod
    def get_tech_assistant(model_name="gpt-4o-mini"):
        assistant_config = get_tech_assistant_config(model_name)
        return BaseOpenAiAssistant(assistant_config)

    @staticmethod
    def get_writing_assistant(model_name="gpt-4o-mini"):
        assistant_config = get_writing_assistant_config(model_name)
        return BaseOpenAiAssistant(assistant_config)
