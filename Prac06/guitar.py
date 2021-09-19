"""Class for Guitars"""


CURRENT_YEAR = 2021
VINTAGE_AGE = 50


class Guitar:
    """Guitar class storing guitar info"""
    def __init__(self, name="", year=0, cost=0):
        """Initialise a Guitar."""
        self.name = name
        self.year = year
        self.cost = cost
    
    def __str__(self):
        """Return a string/statement"""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"
    
    def get_age(self):
        """Getting the age of the guitar based on the current year"""
        return CURRENT_YEAR - self.year
    
    def is_vintage(self):
        """Returning a statement if the age of the guitar is greater then predetermined restriction"""
        return self.get_age() >= CURRENT_YEAR
    
    
