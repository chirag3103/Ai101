from abc import ABC

from langchain.agents import Agent


class BaseAgent(Agent, ABC):

    @staticmethod
    def interact():
        #
        pass

    @property
    def llm_prefix(self):
        return "Base Agent LLM Prefix"

    @property
    def observation_prefix(self):
        return "Base Agent Observation Prefix"

    def _get_default_output_parser(self):
        # Provide a simple parser or default behavior
        return lambda x: x

    @property
    def create_prompt(self):
        # Return a default prompt creation mechanism
        return lambda: "Base Agent Default Prompt"
