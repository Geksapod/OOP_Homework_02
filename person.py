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