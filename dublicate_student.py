import student


class DublicateStudentError(Exception):
    """Inherited class of Exception class."""

    def __init__(self, student: student.StudentPerson, group_title: str, group_year: int):
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

        return f"{self.student} has already been registered in {self.group_title} - {self.group_year}"