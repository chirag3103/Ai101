# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import asyncio

from apps.writing_buddy.writing_buddy import WritingBuddy
from apps.shared.model import LLMs
# from apps.lor_writing.generate import Generate
from apps.tech_buddy.tech_buddy import TechBuddy


def get_model_info():
    mod = LLMs.get_model_info('gpt-4o-mini')
    print(f'Model Params, {mod}')


def letter_support():
    # Split into specific vs generalized writing (both won't be possible in one, will it?)
    writing_buddy = WritingBuddy()
    writing_buddy.generate_response()


def tech_support():
    # Use a breakpoint in the code line below to debug your script.
    tech_buddy = TechBuddy()
    tech_buddy.generate_response()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Define the project root
    tech_support()
