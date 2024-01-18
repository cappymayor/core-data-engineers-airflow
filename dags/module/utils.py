from datetime import datetime


def customer_age(birth_year):
    def calculate_age(birth_year, current_year):
        current_year = datetime.now().year
        age = current_year - birth_year
        return age

    try:
        birth_year = int(birth_year)
        current_year = datetime.now().year
        if birth_year > current_year:
            raise ValueError("Birth year cannot be in the future.")

        age = calculate_age(birth_year, current_year)
        return age
    except ValueError:
        return "Invalid input. Please enter a valid birth year."
