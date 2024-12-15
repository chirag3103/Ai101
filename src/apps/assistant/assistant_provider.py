from src.apps.assistant.base_open_ai_assistant import BaseOpenAiAssistant


class AssistantProvider(BaseOpenAiAssistant):

    def __init__(self, model_name="gpt-4o-mini"):
        buddy_config = self.get_tech_assistant(model_name)
        super().__init__(buddy_config)

    @staticmethod
    def get_tech_assistant(model_name="gpt-4o-mini"):
        return {
            "name": "tech_buddy",
            "model_name": model_name,  # ModelProvider?
            "system_content_version": 1,
            "user_content_version": 1,
        }

    @staticmethod
    def get_writing_assistant(model_name="gpt-4o-mini"):
        return {
            "name": "writing_buddy",
            "model_name": model_name,  # ModelProvider?
            "system_content_version": 1,
            "user_content_version": 1,
        }
