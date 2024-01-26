from datetime import date


def calculate_age(birth_year = 2000):
    todays_date = date.today()
    present_year = todays_date.year
    age = present_year - birth_year
    return age


print(calculate_age(2000))
