"""Class for the language program"""


class ProgrammingLanguage:

    def __init__(self, name, typing, reflection, year):
        """Defining variables for class operation"""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Returns a string/statement"""
        return f"{self.name}, {self.typing} typing, reflection={self.reflection}, First appeared in {self.year}"

    def is_dynamic(self):
        """Test if program is Dynamic"""
        return self.typing == "Dynamic"

