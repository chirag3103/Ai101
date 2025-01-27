from langchain_openai.chat_models import ChatOpenAI
from langchain_core.runnables import RunnableSequence


class ExamAssistant:
    def __init__(self, exam, prompt_template):
        # Create a RunnableSequence
        self.runnable_sequence = RunnableSequence(
            prompt_template | ChatOpenAI(temperature=0)  # Chain the prompt and LLM
        )
        self.pending_exams = [exam]

    def add_exam(self, exam):
        self.pending_exams.append(exam)

    def interact(self):
        print("Exam Day!")
        for exam in self.pending_exams:
            print(f"Scheduled for test: {exam.get('name')}")

            # # Use LLM to evaluate the exam
            # llm_output = self.runnable_sequence.invoke({"exam": exam})
            # print(f"LLM Exam Validation: {llm_output.content}")

            for student in exam.get('students'):
                if student.prepared():
                    return f"{student.name} passed the exam on his own!"
                print(f"{student.name} needs help from their parents")
                mother = student.child.mother
                father = student.child.father
                if student.child.ask_parent(mother):
                    return f"{student.name} passed the exam with help from Mother: {mother.name}."
                elif student.child.ask_parent(father):
                    return f"{student.name} passed the exam with help from Father: {father.name}."
                return f"{student.name} failed the exam."
