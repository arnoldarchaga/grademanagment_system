# grade_management.py
"""
Student Grade Management System (Skeleton)
Demonstrates OOP with Encapsulation, Inheritance, and basic data structures.
"""

from abc import ABC, abstractmethod

# ========== Global Data Structures ==========

# Dictionary to link student ID -> Student object
STUDENTS = {}

# ========== Classes ==========

class Student:
    """
    Represents a single student with a name, ID, and associated grades.
    Encapsulates student information and a list of Grade objects.
    """
    def __init__(self, name: str, student_id: str):
        self._name = name
        self._student_id = student_id
        self._grades = []  # list of Grade objects

    @property
    def name(self):
        return self._name

    @property
    def student_id(self):
        return self._student_id

    def add_grade(self, grade):
        """
        Add a Grade object to this student's list of grades.
        """
        self._grades.append(grade)

    def calculate_average(self):
        """
        Returns the average score across all the student's grades
        (0.0 if no grades).
        """
        if not self._grades:
            return 0.0
        total = sum(g.score for g in self._grades)
        return total / len(self._grades)

    def get_grades(self):
        """
        Return a copy of the list of all Grade objects for this student.
        """
        return list(self._grades)

    def __str__(self):
        """
        String representation for debugging or simple reports.
        """
        return f"Student(name={self._name}, ID={self._student_id})"


class Grade(ABC):
    """
    Abstract base class for a Grade. Inherits from ABC for demonstration.
    """
    def __init__(self, score: float):
        self.score = score  # Could add validations if needed

    @abstractmethod
    def grade_type(self) -> str:
        """
        Return the type of this grade (e.g., "Exam", "Homework").
        Must be overridden by subclasses.
        """
        pass

    def __str__(self):
        return f"{self.grade_type()} Grade: {self.score}"


class ExamGrade(Grade):
    """
    Represents an exam grade, derived from Grade.
    """
    def grade_type(self):
        return "Exam"


class HomeworkGrade(Grade):
    """
    Represents a homework grade, derived from Grade.
    """
    def grade_type(self):
        return "Homework"

# ========== Manager/Utility Functions ==========

def add_student(name: str, student_id: str):
    """
    Adds a new Student to the global STUDENTS dictionary
    if the student ID is not already taken.
    """
    if student_id in STUDENTS:
        print(f"ERROR: Student ID {student_id} already exists.")
        return

    student = Student(name, student_id)
    STUDENTS[student_id] = student
    print(f"Added student: {student}")

def add_exam_grade(student_id: str, score: float):
    """
    Creates an ExamGrade and attaches it to the specified student.
    """
    if student_id not in STUDENTS:
        print(f"ERROR: Student ID {student_id} not found.")
        return

    grade = ExamGrade(score)
    STUDENTS[student_id].add_grade(grade)
    print(f"Added {grade} to {STUDENTS[student_id].name}")

def add_homework_grade(student_id: str, score: float):
    """
    Creates a HomeworkGrade and attaches it to the specified student.
    """
    if student_id not in STUDENTS:
        print(f"ERROR: Student ID {student_id} not found.")
        return

    grade = HomeworkGrade(score)
    STUDENTS[student_id].add_grade(grade)
    print(f"Added {grade} to {STUDENTS[student_id].name}")

def generate_report():
    """
    Generates a simple report showing each student's
    name, ID, list of grades, and average score.
    """
    print("\n==== Performance Report ====\n")
    for student_id, student in STUDENTS.items():
        avg = student.calculate_average()
        print(f"{student.name} (ID: {student_id})")
        print(f"  Grades:")
        for g in student.get_grades():
            print(f"    {g}")
        print(f"  Average: {avg:.2f}\n")

# ========== main stub ==========

def main():
    """
    Demonstrates usage of the skeleton.
    In real usage, you might parse user input or read from a file.
    """
    # TODO: For final project, integrate your own I/O or menu system.

    # Example usage:
    add_student("Alice", "S001")
    add_student("Bob", "S002")

    add_exam_grade("S001", 90)
    add_homework_grade("S001", 85)
    add_exam_grade("S002", 78)

    # Generate a report
    generate_report()

if __name__ == "__main__":
    main()
