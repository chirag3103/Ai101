import argparse

from apps.assistant.assistant_provider import AssistantProvider


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


def main(**kwargs):
    assistant_name = kwargs.get('assistant_type')

    assistant_provider = AssistantProvider(assistant_name)
    placeholder_support(assistant_provider)
    # tech_support(assistant_provider)
    # letter_support(assistant_provider)


def parse_args():
    parser = argparse.ArgumentParser(description='Specify parameters for the assistant.')
    parser.add_argument('--assistant_type', type=str, required=True, help='The name of the assistant to be used')

    return vars(parser.parse_args())


if __name__ == '__main__':
    args = parse_args()
    main(**args)
