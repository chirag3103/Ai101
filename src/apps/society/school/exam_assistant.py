from abc import ABC
from apps.society.agent.base_agent import BaseAgent


class ExamAssistant(BaseAgent, ABC):
    def __init__(self, exam, llm_chain, output_parser=None):
        super().__init__(llm_chain=llm_chain, output_parser=output_parser)
        self.pending_exams = [exam]

    def add_exam(self, exam):
        self.pending_exams.append(exam)

    def interact(self):
        print("Exam Day!")
        for exam in self.pending_exams:
            print(f"Scheduled for test: {exam.get('name')}")
            for student in exam.get('students'):
                # Prompt for taking an exam
                if student.prepared():
                    return f"{student.name} passes the exam on his own!"

                print(f"{student.name} needs helps from his parents")
                # Ask parents when not prepared
                mother = student.child.mother
                father = student.child.father
                if student.child.ask_parent(mother):
                    return f"{student.name} passes the exam with help from Mother: {mother.name}."
                elif student.child.ask_parent(father):
                    return f"{student.name} passes the exam with help from Father: {father.name}."
                return f"{student.name} fails the exam."
