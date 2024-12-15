from abc import ABC

from rich.console import Console
from rich.markdown import Markdown
from openai import OpenAI

from src.apps.content.content_provider import ContentProvider
from src.apps.shared.model import Models
from src.apps.shared.utils import write_markdown


class BaseOpenAiAssistant(ABC):
    def __init__(self, buddy_config):
        self.client = OpenAI()
        self.console = Console()
        self.validate_buddy_config(buddy_config)
        self.model_info = Models.get_model_info(buddy_config['model_name'])
        self.content_provider = ContentProvider(buddy_config)
        self.buddy_type = buddy_config['name']

    @staticmethod
    def validate_buddy_config(config):
        if not config['model_name']:
            raise ValueError(f"Model '{config['model_name']}' is not supported.")

    def sample_llm(self, system_content, user_content):
        chat_completion = self.client.chat.completions.create(
            messages=[
                {"role": "system", "content": system_content},
                {"role": "user", "content": user_content},
            ],
            model=self.model_info["name"],
            max_tokens=self.model_info["max_tokens"] - 500,
        )
        return chat_completion.choices[0].message

    def generate_response(self):
        # Load content
        user_content, system_content = self.content_provider.get_contents()

        # Generate response
        response = self.sample_llm(system_content=system_content, user_content=user_content).content.strip()

        # Print formatted output
        print("\nGenerated Output:\n")
        mark_down = Markdown(response)
        self.console.print(mark_down)

        # Save to a Markdown file
        output_file = write_markdown(file_path=f"apps/{self.buddy_type}_response.md", write_content=response)
        print(f"\nResponse saved to {output_file}")
