from typing import List, Dict

from langchain.agents.openai_assistant import OpenAIAssistantRunnable
from langchain.chains.llm import LLMChain
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.prompt_values import StringPromptValue
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.runnables import RunnableSequence
from langchain_core.output_parsers.json import SimpleJsonOutputParser
from langchain_core.output_parsers.json import JsonOutputParser
from pydantic import BaseModel

class NameResponseModel(BaseModel):
    names: List

class CulturalSignificanceResponseModel(BaseModel):
    name: str
    cultural_significance: Dict

class SimulationHelper:

    @staticmethod
    def simulate_scene(llm, prompt_template, input_args, response_model):
        prompt = PromptTemplate(
            input_variables=list(input_args.keys()),
            template=prompt_template
        )
        output_parser = JsonOutputParser(pydantic_object=response_model)
        sequence = prompt | llm | output_parser
        runnable_sequence = RunnableSequence(sequence)
        return runnable_sequence.invoke(input=input_args)

    @staticmethod
    def agentized():
        # def add_one(x: int) -> int:
        #     return x + 1
        #
        # def mul_two(x: int) -> int:
        #     return x * 2
        #
        # runnable_1 = RunnableLambda(add_one)
        # runnable_2 = RunnableLambda(mul_two)
        # sequence = runnable_2 | runnable_1
        # # Or equivalently:
        # # sequence = RunnableSequence(first=runnable_1, last=runnable_2)
        # output = sequence.invoke(1)
        # print(output)
        # # await sequence.ainvoke(1)
        #
        # batch = sequence.batch([1, 2, 3])
        # print(batch)
        # # await sequence.abatch([1, 2, 3])
        prompt = PromptTemplate.from_template(
            'In JSON format, give me a list of {topic} and their '
            'corresponding names in French, Spanish and in a '
            'Cat Language.'
        )
        model = ChatOpenAI()
        chain = prompt | model | SimpleJsonOutputParser
        for chunk in chain.stream({'topic': 'colors'}):
            print('-')  # noqa: T201
            print(chunk, sep='', flush=True)  # noqa: T201

    def trigger(self):
        template = "{father} and {mother} just became parents. Could you help naming their son? They live in {city}, " \
                   "{state}. Respond with a list of names in JSON format."
        prompt = PromptTemplate(
            input_variables=["father", "mother", "city", "state"],
            template=template
        )
        prompt_args = {"father": "chirag", "mother": "skye", "state": "California", "city": "Berkeley"}
        model = ChatOpenAI()
        chain = prompt | model | SimpleJsonOutputParser
        for chunk in chain.stream(input=prompt_args):
            print('-')  # noqa: T201
            print(chunk, sep='', flush=True)  # noqa: T201

        llm = ChatOpenAI(model='gpt-4o-mini', temperature=0.7)
        # temp = llm.invoke('what could be the temp right now?')
        # print(temp.content)

        messages = [SystemMessage(content='You are in California Berkeley. Its mid December.'),
                    HumanMessage(content='what could be the temp right now?')]
        # response = llm.invoke(messages)
        # print(response.content)

        # Step 1: Generate a name
        template = "{father} and {mother} just became parents. Could you help naming their son? They live in {city}, " \
                   "{state}. Respond with a list of names in JSON format." #  prompt for response format?
        name_prompt = PromptTemplate(
            input_variables=["father", "mother", "city", "state"],
            template=template
        )
        name_prompt_args = {"father": "chirag", "mother": "skye", "state": "California", "city": "Berkeley"}
        # print(name_prompt.format(**name_prompt_args))
        # prints formatted prompt
        # llm.generate_prompt([name_prompt.format([args])])

        # invokes llm with formatted prompt
        # response = llm.invoke(name_prompt.format(**parents))

        # LLMChain is deprecated
        # chain = LLMChain(llm=llm, prompt=name_prompt)

        # RunnableSequence
        # Build the sequence
        sequence = name_prompt | llm | SimpleJsonOutputParser()

        # Wrap the sequence into RunnableSequence
        runnable_sequence = RunnableSequence(sequence)

        response = runnable_sequence.invoke(input=name_prompt_args)
        print(f"Parents picked names: {response}")

        cultural_prompt = PromptTemplate(
            input_variables=["names"],
            template="You've become a great grandfather, Hooray! "
                     "Your son and his wife have come up with these 10 names {names} for their son. "
                     "Based on cultural significance of the suggestions, "
                     "could you finalize a name.? "
                     "Return the above response with a object of name in JSON format."
        )
        cultural_prompt_args = response

        sequence = cultural_prompt | llm | SimpleJsonOutputParser()

        runnable_sequence = RunnableSequence(sequence)

        response = runnable_sequence.invoke(input=cultural_prompt_args)
        print(f"GrandParent picked name: {response}")

        # name = response["names"][0]
        # print(response["names"])
        #
        # chain = name_prompt | llm | SimpleJsonOutputParser
        # stream = chain.astream(input=name_prompt_args)
        # print(f"stream: {stream}")

        # Step 2: Process the name (e.g., explore cultural significance)
        cultural_prompt = PromptTemplate(
            input_variables=["name"],
            template="What is the cultural significance of the name {name}?"
        )

        # Step 3: Create study questions based on the name's significance
        study_prompt = PromptTemplate(
            input_variables=["name", "cultural_significance"],
            template="Based on the name {name} and its cultural significance, generate 5 exam questions."
        )

        # Initialize the LLM
        llm = ChatOpenAI(temperature=0.7)
