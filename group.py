import dublicate_student
import group_limit
import student


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
        self.index = 0

    def add_student(self, student: student.StudentPerson):
        """Add a student to a group.

        Raises
        ------
        DublicateStudentError
            If student is in group already.
        GroupLimitError
            If add student when quantity of students in group reached `max_students` value.
        """

        if student in self.__students:
            raise dublicate_student.DublicateStudentError(student, self.title, self.year)
        if len(self.__students) >= self.max_students:
            raise group_limit.GroupLimitError(self.max_students)

        self.__students.append(student)

    def remove_student(self, student: student.StudentPerson):
        """Remove a student from a group."""

        if student in self.__students:
            self.__students.remove(student)

    def find_student(self, student_surname):
        """Find a student in a group."""

        for student in self.__students:
            if student_surname in str(student):
                return student
        return None

    def __getitem__(self, item):
        return self.__students[item]

    def __iter__(self):
        return iter(self.__students)

    def __str__(self):
        """Return formatted group's title and list of the students."""

        return f"{self.title} - {self.year}\n{'-' * 15}\n" + "\n".join(map(str, self.__students)) + "\n"