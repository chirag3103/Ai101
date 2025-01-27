import json

from langchain.agents.openai_assistant import OpenAIAssistantRunnable
from langchain.chains.llm import LLMChain
from langchain_core.output_parsers import SimpleJsonOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence
from langchain_openai import ChatOpenAI

from apps.society.family.child import Child
from apps.society.family.parent import Parent
from apps.society.school.exam_assistant import ExamAssistant
from apps.society.school.student import Student
from apps.society.school.teacher import Teacher
from apps.society.self.person import Person
# from langchain_community.chains.openapi import SimpleSequentialChain

from apps.society.workflow_manager import SimulationHelper, NameResponseModel, CulturalSignificanceResponseModel


class LifeCycle:

    def __init__(self) -> None:
        super().__init__()
        self.general_purpose_llm = ChatOpenAI(model='gpt-4o-mini', temperature=0.7)
        self.simulation_helper = SimulationHelper()

    def simulate_life_cycle(self):
        grand_father = Person("Rufus", 84)
        grand_father.birth()

        boy = Person("Alex", 24)
        boy.birth()

        print(f"Boy {boy}")

        girl = Person("Sarah", 30)
        girl.birth()

        print(f"Girl {girl}")

        father = Parent(boy)
        mother = Parent(girl)

        print(f"{father} and {mother} are going to have a son. What will they name him?")

        chosen_name = self.simulate_name_giving_ceremony(father.name, mother.name, grand_father)

        child = Child(chosen_name.get("name"), 1, father, mother)
        child.birth()

        print(f"OMG! {child.name} is already 3. Time flies!"
              f"{child.mother.name} and {child.father.name} are now in search for a school in the neighborhood.")

        # a prompt that helps to research schools and finalizing one
        school_name = "Berkeley Elementary School"

        print(f"They decided to enroll {child.name} in {school_name}.")
        student = Student(child)
        # student.complete_take_home() #  Uncomment of un helped success

        # what does he go by now? new names etc
        teacher = Teacher("Mr. Reed", 50, student)
        teacher.birth()
        print(f"Teacher {teacher.name} now teaches student {student.name}")

        exam = teacher.create_exam('Sample Test')

        prompt_template = PromptTemplate(
            input_variables=["exam"],
            template="You are an exam evaluator. Review this exam: {exam} and provide detailed feedback."
        )

        # Use ExamAssistant
        exam_assistant = ExamAssistant(exam, prompt_template)
        print(f"ExamAssistant created for exam: {exam.get('name')}")

        # # Create multi-step chain
        # multi_step_chain = create_multi_step_chain(self)

        # # Simulate parent guidance
        # self.simulate_parent_kid_test_prep_guidance(multi_step_chain, father.name, child.name)

        # Simulating exam interaction
        result = exam_assistant.interact()
        print(result)


    @staticmethod
    def simulate_parent_kid_test_prep_guidance(multi_step_chain, parent_name, child_name):
        # Run the chain
        result = multi_step_chain.run({"parent_name": parent_name, "child_name": child_name})
        print(result)

    ## Helper methods
    # Sample OUTPUT 1:
    # Parents suggested names: {'names': ['Aiden', 'Kai', 'Milo', 'Jasper', 'Soren', 'Liam', 'Orion', 'Ezra', 'Finn', 'Asher', 'Zane', 'Theo', 'Nolan', 'Ronan', 'Kiran']}
    # GrandParent picked name: {'name': 'Orion'}
    # Sample OUTPUT 2:
    # Parents suggested names: {'names': ['Eli', 'Jasper', 'Finn', 'Leo', 'Milo', 'Asher', 'Theo', 'Zane', 'River', 'Kai', 'Luca', 'Orion', 'Silas', 'Dashiell', 'Emmett']}
    # GrandParent picked name: {'suggestedName': 'Asher', 'culturalSignificance': {'origin': 'Hebrew', 'meaning': 'happy, blessed', 'popularity': 'widely used in various cultures'}}
    def simulate_name_giving_ceremony(self, father_name, mother_name, grandparent):
        # Step 1: Generate a name
        # name_prompt_template = {
        #     "father": father_name,
        #     "mother": mother_name,
        #     "state": "California",
        #     "city": "Berkeley",
        #     "prompt": "Could you help naming their son? Respond with a list of names in JSON format.",
        #     "response_format": {"names": ["<name1>", "<name2>", "..."]}
        # }
        name_prompt_template = ("{father} and {mother} just became parents! "
                                "Could you help naming their son? "
                                "They live in {city}, {state}. "
                                "Respond with a list of names in JSON format."
                                "Output format: {{\"names\": [\"<name1>\", \"<name2>\", \"...\"]}}")
        name_prompt_args = {"father": father_name, "mother": mother_name, "state": "California", "city": "Berkeley"}
        response = self.simulation_helper.simulate_scene(self.general_purpose_llm, name_prompt_template, name_prompt_args, NameResponseModel)
        print(f"The following have been submitted for review to his grand_parent: {response}")

        # Step 2: Cultural significance
        # cultural_prompt_template = {
        #     "grandparent_name": grandparent_name,
        #     "names": response,
        #     "prompt": "Based on cultural significance of the suggestions, could you finalize a name? Return the above response with an object of name in JSON format.",
        #     "response_format": {"name": "<name>",
        #                         "cultural_significance": {"origin": "<origin>", "meaning": "<meaning>",
        #                                                   "popularity": "<popularity>"}}
        # }
        cultural_prompt_template = ("{grandparent_name} just became a great grandfather! "
                                    "His son and wife have come up with these 10 names {names} for their son. "
                                    "Based on cultural significance of the suggestions, could you finalize a name? "
                                    "Return the above response with an object of name in JSON format. "
                                    "Output format: {{\"name\": \"<name>\", \"cultural_significance\": {{\"origin\": \"<origin>\", \"meaning\": \"<meaning>\", \"popularity\": \"<popularity>\"}}}}")
        cultural_prompt_args = {"grandparent_name": grandparent.name, **response}
        response = self.simulation_helper.simulate_scene(self.general_purpose_llm, cultural_prompt_template, cultural_prompt_args, CulturalSignificanceResponseModel)
        # Transform the cultural response into a string; add another link in the chain
        print(f"GrandParent is heart felt and chosen the following to be name of the heir: {response.get('name')}. "
              f"Here's the cultural significance: {response.get('cultural_significance')}")
        return response


    # SAMPLE OUTPUT 1:
    # [Message(id='msg_qSWhR97sLVnl4nMauN40o7fB',
    #     assistant_id='asst_7D5pVgEd2xrMmCyzlucdKh3J',
    #     attachments=[], completed_at=None,
    #     content=[
    #         TextContentBlock(
    #             text= Text(
    #                 annotations=[],
    #                 value='\\(10 - 4^{2.7}\\) results in approximately -32.2243.'), <--
    #             type='text')],
    #     created_at=1734418094, incomplete_at=None, incomplete_details=None, metadata={},
    #     object='thread.message', role='assistant',
    #     run_id='run_5hr8YMbcCFODK5Nns6Yvaadf',
    #     status=None,
    #     thread_id='thread_tznfVsHguZjPwo229obPxAnP')]
    @staticmethod
    def simulate_math_tutoring(question = "What's 10 - 4 raised to the 2.7"):
        interpreter_assistant = OpenAIAssistantRunnable.create_assistant(
            name="langchain assistant",
            instructions="You are a personal math tutor. "
                         "Write and run code to answer math questions.",
            tools=[{"type": "code_interpreter"}],
            model="gpt-4-1106-preview"
        )
        output_array = interpreter_assistant.invoke({"content": question})
        content = output_array[0].content
        print(f"Result: {content[0].text.value}")