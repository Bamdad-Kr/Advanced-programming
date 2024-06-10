class Student:
    def __init__(self, student_id, physics, language, math):
        self.student_id = student_id
        self.physics = physics
        self.language = language
        self.math = math

    def calculate_average(self):
        total_credits = 2 + 3 + 2 
        total_score = self.physics * 2 + self.math * 3 + self.language * 2
        return total_score / total_credits


class University:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def expel_students_below_average(self, threshold=10):
        self.students = [student for student in self.students if student.calculate_average() >= threshold]


def input_students(num_students):
    university = University()
    for _ in range(num_students):
        student_id = input("Enter student ID: ")
        physics = float(input("Enter Physics score (out of 20): "))
        language = float(input("Enter Language score (out of 20): "))
        math = float(input("Enter Math score (out of 20): "))
        student = Student(student_id, physics, language, math)
        university.add_student(student)
    return university


def main():
    num_students = 100
    university = input_students(num_students)
    university.expel_students_below_average()
    
    for student in university.students:
        print(f"Student ID: {student.student_id}, Average: {student.calculate_average():.2f}")

if __name__ == "__main__":
    main()
