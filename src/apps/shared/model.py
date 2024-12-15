from enum import Enum


class Models(Enum):
    GPT_4o_MINI = {
        "name": "gpt-4o-mini",
        "description": "A lightweight GPT-4 variant optimized for quick responses.",
        "max_tokens": 4096,
        "usage": "Ideal for small to medium-sized tasks.",
    }
    GPT_4 = {
        "name": "gpt-4",
        "description": "The full GPT-4 model with extensive capabilities.",
        "max_tokens": 8192,
        "usage": "Best for complex and detailed queries.",
    }
    GPT_3_5_TURBO = {
        "name": "gpt-3.5-turbo",
        "description": "A cost-effective, high-performance variant of GPT-3.5.",
        "max_tokens": 4096,
        "usage": "Suitable for large-scale, cost-sensitive applications.",
    }

    @classmethod
    def get_model_info(cls, model_name):
        """Fetch detailed information for a given model name."""
        for model in cls:
            if model.value["name"] == model_name:
                return model.value
        return None
