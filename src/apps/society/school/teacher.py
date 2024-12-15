from apps.society.self.person import Person


class Teacher(Person):
    def __init__(self, name, age, assigned_student):
        super().__init__(name, age)
        self.students = [assigned_student]
        self.attendance = 0.0

    def mark_attendance(self, present_students):
        """
        Mark attendance for the teacher's students based on the provided list of present_students.
        """
        if not self.students:
            raise ValueError("No students are assigned to this teacher.")

        total_present = 0
        for student in self.students:
            if student in present_students:
                student.mark_present()
                total_present += 1
            else:
                student.mark_absent()

        self.attendance = total_present / len(self.students) * 100
        print(f"Attendance updated to {self.attendance:.2f}%.")

    def give_class(self, present_students):
        """
        Conduct a class, marking attendance and then teaching the subject.
        """
        self.mark_attendance(present_students)
        self.teach()

    def create_exam(self, name):
        """
        Create an exam for students. This could include random questions or other logic.
        """
        exam = {
            "name": name,
            "teacher": self,
            "students": self.students,
            "questions": "What is yellow?"
        }
        print(f"Teacher {self.name} is creating an exam {exam} for {len(self.students)} students.")
        return exam

    def teach(self):
        """
        Basic teaching logic. Override for specific subjects or styles.
        """
        print(f"Teacher {self.name} is teaching the class.")

    def assign_student(self, new_student):
        """
        Assign a new student to this teacher.
        """
        self.students.append(new_student)
        print(f"Student {new_student.name} has been assigned to teacher {self.name}.")
