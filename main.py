import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s %(name)-12s %(levelname)-8s %(message)s")

console = logging.StreamHandler()
console.setLevel(logging.WARNING)
console.setFormatter(formatter)

filehandler = logging.FileHandler("logger.log")
filehandler.setLevel(logging.INFO)
filehandler.setFormatter(formatter)

logger.addHandler(console)
logger.addHandler(filehandler)


class Person:
    """Class describes a person."""

    def __init__(self, surname: str, name: str, father_name: str, birth_date: dict):
        """Initialisation of person's attributes.

        Parameters
        ----------
        surname: str
            Surname of a person.
        name: str
            Name of a person.
        father_name: str
            Father's name of a person.
        birth_date: dict of {str: int}
            Birth date of a person.
        """

        self.surname = surname
        self.name = name
        self.father_name = father_name
        self.birth_date = birth_date

    def __str__(self):
        """Return formatted person's name."""

        return f"{self.surname} {self.name}. {self.father_name}."


class StudentPerson(Person):
    """Inherited class of class Person, describes a student."""

    def __init__(self, surname: str, name: str, father_name: str, birth_date: dict, status: str = "student"):
        """Initialisation of student's attributes.

        Parameters
        ----------
        surname: str
            Surname of a student.
        name: str
            Name of a student.
        father_name: str
            Father's name of a student.
        birth_date: dict of {str: int}
            Birth date of a student.
        status: str, default "student"
            Status of a student.
        """

        super().__init__(surname, name, father_name, birth_date)
        self.status = status

    def __str__(self):
        """Return formatted student's name."""

        return f"{self.surname} {self.name[0]}. {self.father_name[0]}."


class GroupLimitError(Exception):
    """Inherited class of Exception class."""

    def __init__(self, max_limit: int):
        """Initialisation of GroupLimitError's attributes.

        Parameters
        ----------
        max_limit: int
            Maximum limit of students in group.
        """

        self.max_limit = max_limit

    def __str__(self):
        """ Return formatted message of GroupLimitError."""

        return f"The group has got {self.max_limit} students already"


class DublicateStudentError(Exception):
    """Inherited class of Exception class."""

    def __init__(self, student: StudentPerson, group_title: str, group_year: int):
        """Initialisation of DublicateStudentError's attributes

        Parameters
        ----------
        student: StudentPerson
            Student that studies in a group.
        group_title: str
            Title of a group.
        group_year: int
            Year of a group.
        """

        self.student = student
        self.group_title = group_title
        self.group_year = group_year

    def __str__(self):
        """ Return formatted message of DublicateStudentError"""

        return f"{self.student} has been registered in {self.group_title} - {self.group_year}"


class Group:
    """Class describes a group"""

    def __init__(self, title: str, year: int, max_students: int = 10):
        """Initialisation of group's attributes

        Parameters
        ----------
        title: str
            Title of a group.
        year: int
            Year of a group.
        max_students: int, default 10
            Maximum limit of students in group.

        Raises
        ------
        TypeError
            If `max_students` is not integer
        ValueError
            If `max_students` is negative or equal to zero.
        """

        if not isinstance(max_students, int):
            raise TypeError("max_students argument is not integer")
        if max_students <= 0:
            raise ValueError("max_students argument can not be negative or equal to zero")

        self.title = title
        self.year = year
        self.max_students = max_students
        self.__students = []

    def add_student(self, student: StudentPerson):
        """Add a student to a group.

        Raises
        ------
        DublicateStudentError
            If student is in group already.
        GroupLimitError
            If add student when quantity of students in group reached `max_students` value.
        """

        if student in self.__students:
            raise DublicateStudentError(student, self.title, self.year)
        if len(self.__students) >= self.max_students:
            raise GroupLimitError(self.max_students)

        self.__students.append(student)

    def remove_student(self, student: StudentPerson):
        """Remove a student from a group."""

        if student in self.__students:
            self.__students.remove(student)

    def find_student(self, student_surname):
        """Find a student in a group."""

        for student in self.__students:
            if student_surname in str(student):
                return student
        return None

    def __str__(self):
        """Return formatted group's title and list of the students."""

        return f"{self.title} - {self.year}\n{'-' * 15}\n" + "\n".join(map(str, self.__students)) + "\n"


if __name__ == "__main__":

    logger.info("Started logging")

    try:
        student_1 = StudentPerson("Petrenko", "Petro", "Petrovych", {"year": 1990, "month": 1, "date": 11})
        student_2 = StudentPerson("Vasylenko", "Vasylyna", "Vasylivna", {"year": 1990, "month": 2, "date": 12})
        student_3 = StudentPerson("Andrienko", "Andriy", "Andrievych", {"year": 1990, "month": 3, "date": 13})
        student_4 = StudentPerson("Kuzmenko", "Maria", "Petrivna", {"year": 1990, "month": 4, "date": 14})
        student_5 = StudentPerson("Stetsenko", "Stephan", "Andrievych", {"year": 1990, "month": 5, "date": 20})
        student_6 = StudentPerson("Shevchenko", "Ivan", "Oleksievych", {"year": 1991, "month": 11, "date": 5})
        student_7 = StudentPerson("Sergienko", "Olga", "Sergievna", {"year": 1990, "month": 9, "date": 21})
        student_8 = StudentPerson("Petrenko", "Victor", "Andrievych", {"year": 1990, "month": 8, "date": 22})
        student_9 = StudentPerson("Ivanenko", "Hanna", "Ivanivna", {"year": 1990, "month": 7, "date": 23})
        student_10 = StudentPerson("Bondarenko", "Mykola", "Mykolayovych", {"year": 1990, "month": 6, "date": 24})
        student_11 = StudentPerson("Bondarenko", "Mykola", "Vasyliovych", {"year": 1992, "month": 1, "date": 10})

        group_1 = Group("Python", 2022)

        logger.warning("Started logging to console and log")

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
        group_1.add_student(student_5)
        group_1.add_student(student_11)


    except Exception as error:
        print(error)

    logger.info("Finished logging")

    print(group_1, "\n")
    print(group_1.find_student("Stetsenko"))







