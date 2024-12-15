# This is a sample Python script.
from src.apps.assistant.assistant_provider import AssistantProvider


def letter_support():
    # Split into specific vs generalized writing (both won't be possible in one, will it?)
    writing_buddy = assistant_provider.get_tech_assistant()
    writing_buddy.generate_response()


def tech_support(assistant_prov):
    # Use a breakpoint in the code line below to debug your script.
    tech_buddy = assistant_prov.get_tech_assistant()
    tech_buddy.generate_response()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Define the project root
    assistant_provider = AssistantProvider()
    tech_support(assistant_provider)
