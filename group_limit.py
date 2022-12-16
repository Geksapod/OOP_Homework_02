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