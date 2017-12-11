import datetime


def is_valid(value):
    if not value.isdigit():
        return False

    age = int(value)
    return age in range(0, 141)


def calculate_year(age):
    return datetime.date.today().year + 100 - age


if __name__ == "__main__":
    name = raw_input("Your name: ")
    age = raw_input("How old are you?: ")

    if is_valid(value=age):
        year = calculate_year(age=int(age))
        print("{0} will be 100 years old in the year {1}".format(name, year))
    else:
        print("Put the number from 0 to 140")
