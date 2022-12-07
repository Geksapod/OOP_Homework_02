class Person:
    """Describe a person"""

    def __init__(self, surname: str, name: str, father_name: str, birth_date: dict):
        """Initialisation of person's attributes"""
        self.surname = surname
        self.name = name
        self.father_name = father_name
        self.birth_date = birth_date

    def __str__(self):
        """Return formatted person's name"""
        return f"{self.surname} {self.name}. {self.father_name}."


class StudentPerson(Person):
    """Describe a student"""

    def __init__(self, surname: str, name: str, father_name: str, birth_date: dict, status="student"):
        """Initialisation of student's attributes"""
        super().__init__(surname, name, father_name, birth_date)
        self.status = status

    def __str__(self):
        """Return formatted student's name"""
        return f"{self.surname} {self.name[0]}. {self.father_name[0]}."


class Group:
    """Describe a group"""

    def __init__(self, title: str, year: int):
        """Initialisation of group's attributes"""
        self.title = title
        self.year = year
        self.students = []

    def add_student(self, student: StudentPerson):
        """Add a student to a group"""
        if student not in self.students:
            self.students.append(student)

    def remove_student(self, student: StudentPerson):
        """Remove a student from a group"""
        if student in self.students:
            self.students.remove(student)

    def find_student(self, student_surname):
        """Find a student in a group"""
        for student in self.students:
            if student_surname in str(student):
                return True
        return None

    def __str__(self):
        """Return formatted group's title"""
        return f"{self.title} - {self.year}\n{'-' * 15}\n" + "\n".join(map(str, self.students)) + "\n"


if __name__ == "__main__":
    student_1 = StudentPerson("Petrenko", "Petro", "Petrovych", {"year": 1990, "mounth": 1, "date": 11})
    student_2 = StudentPerson("Vasylenko", "Vasylyna", "Vasylivna", {"year": 1990, "mounth": 2, "date": 12})
    student_3 = StudentPerson("Andrienko", "Andriy", "Andrievych", {"year": 1990, "mounth": 3, "date": 13})
    student_4 = StudentPerson("Kuzmenko", "Maria", "Petrovnf", {"year": 1990, "mounth": 4, "date": 14})
    student_5 = StudentPerson("Stetsenko", "Stephan", "Andrievych", {"year": 1990, "mounth": 5, "date": 20})
    student_6 = StudentPerson("Shevchenko", "Ivan", "Oleksievych", {"year": 1991, "mounth": 11, "date": 5})
    student_7 = StudentPerson("Sergienko", "Olga", "Sergievna", {"year": 1990, "mounth": 9, "date": 21})
    student_8 = StudentPerson("Petrenko", "Victor", "Andrievych", {"year": 1990, "mounth": 8, "date": 22})
    student_9 = StudentPerson("Ivanenko", "Hanna", "Ivanivna", {"year": 1990, "mounth": 7, "date": 23})
    student_10 = StudentPerson("Bondarenko", "Mykola", "Mykolayovych", {"year": 1990, "mounth": 6, "date": 24})

    group_1 = Group("Python", 2022)
    group_1.add_student(student_1)
    group_1.add_student(student_2)
    group_1.add_student(student_3)
    group_1.add_student(student_4)
    group_1.add_student(student_5)
    group_1.add_student(student_6)
    group_1.add_student(student_7)
    group_1.add_student(student_8)
    group_1.add_student(student_9)
    group_1.add_student(student_10)
    group_1.remove_student(student_5)
    group_1.add_student(student_5)

    print(group_1)






