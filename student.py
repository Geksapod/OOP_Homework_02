import person


class StudentPerson(person.Person):
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
