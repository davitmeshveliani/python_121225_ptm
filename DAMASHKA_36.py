
"""
This module defines the hierarchy for Person, Student, and Teacher classes.
"""
class Person:
    """A base class representing a person."""

    def __init__(self, name):
        """Initialize the person with a name."""
        self.name = name

    def introduce(self):
        """Return a basic greeting string."""
        return f"Hello, my name is {self.name}."

class Student(Person):
    """A class representing a student, inheriting from Person."""
    def __init__(self, name, course):
        """Initialize the student with a name and a course number."""
        super().__init__(name)
        self.course = course

    def introduce(self):
        """Return the parent greeting plus the student's course."""
        parent_intro = super().introduce()
        return f"{parent_intro}\nI'm on course {self.course}."

class Teacher(Person):
    """A class representing a teacher, inheriting from Person."""
    def __init__(self, name, subject):
        """Initialize the teacher with a name and a subject."""
        super().__init__(name)
        self.subject = subject

    def introduce(self):
        """Return a specific greeting for a professor including their subject."""
        return f"Hello, I am professor {self.name}.\nMy subject is {self.subject}"


student = Student("Alice", 2)
teacher = Teacher("Bob", "Mathematics")

people = [student, teacher]

# for person in people:  ~  это только для моей проверки.
#     print(person.introduce())