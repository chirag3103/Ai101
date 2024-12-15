from rich.console import Console
from rich.markdown import Markdown
from openai import OpenAI

from apps.shared.abstract_buddy import AbstractBuddy
from apps.shared.model import LLMs
from apps.shared.utils import read_markdown, write_markdown


class TechBuddy(AbstractBuddy):
    def __init__(self, model_name="gpt-4o-mini"):
        self.console = Console()
        self.client = OpenAI()
        self.model_info = LLMs.get_model_info(model_name)
        if not self.model_info:
            raise ValueError(f"Model '{model_name}' is not supported.")

    def sample_llm(self, system_content, user_content):
        chat_completion = self.client.chat.completions.create(
            messages=[
                {"role": "system", "content": system_content},
                {"role": "user", "content": user_content},
            ],
            model=self.model_info["name"],  # Use model name dynamically
            max_tokens=self.model_info["max_tokens"] - 500,  # Reserve tokens for system/user
        )
        return chat_completion.choices[0].message

    def generate_response(self):
        # Load content
        system_content = read_markdown("apps/tech_buddy/v1/prompts/system.md")
        user_content = read_markdown("apps/tech_buddy/v1/prompts/user.md")

        # Generate response
        # response = "# Welcome to Rich!"
        response = self.sample_llm(system_content=system_content, user_content=user_content).content.strip()

        # Print formatted output
        print("\nGenerated Output:\n")
        mark_down = Markdown(response)
        self.console.print(mark_down)
        # self.print_formatted_output(response)

        # Save to a Markdown file
        output_file = write_markdown(file_path="apps/tech_buddy/response.md", write_content=response)
        print(f"\nResponse saved to {output_file}")
