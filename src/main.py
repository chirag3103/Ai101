import argparse

from apps.assistant.assistant_provider import AssistantProvider
from apps.society.life_cycle import LifeCycle
from apps.society.workflow_manager import SimulationHelper


def placeholder_support(assistant_prov):
    placeholder_assistant = assistant_prov.get_placeholder_assistant()
    placeholder_assistant.generate_response()


def letter_support(assistant_prov):
    # Split into specific vs generalized writing (both won't be possible in one, will it?)
    writing_assistant = assistant_prov.get_writing_assistant()
    writing_assistant.generate_response()


def tech_support(assistant_prov):
    tech_assistant = assistant_prov.get_tech_assistant()
    tech_assistant.generate_response()


def life_cycle_support(assistant_prov):
    life_cycle = LifeCycle()
    life_cycle.simulate_life_cycle()


def main(**kwargs):
    assistant_type = kwargs.get('assistant_type')

    assistant_provider = AssistantProvider(assistant_type)

    # Mapping of assistant types to their corresponding support functions
    support_functions = {
        'placeholder': placeholder_support,
        'letter': letter_support,
        'tech': tech_support,
        'life_simulation': life_cycle_support
    }

    # Get the appropriate support function based on the assistant type
    support_function = support_functions.get(assistant_type)

    if support_function:
        support_function(assistant_provider)
    else:
        print(f"Unknown assistant type: {assistant_type}")


def parse_args():
    parser = argparse.ArgumentParser(description='Specify parameters for the assistant.')
    parser.add_argument('--assistant_type', type=str, required=True, help='The type of assistant to be used')

    return vars(parser.parse_args())


if __name__ == '__main__':
    args = parse_args()
    main(**args)
