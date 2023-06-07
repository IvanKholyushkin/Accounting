from prettytable import PrettyTable, DOUBLE_BORDER

salary_table = PrettyTable()

salary_table.field_names = ["id", "First name", "Last name", "Position", "Salary '$'"]
salary_table.add_row([1, "Robert", "Nichols", "Speech-Language Pathologist", 2100])
salary_table.add_row([2, "James", "Garcia", "Bus Driver", 1450])
salary_table.add_row([3, "Justin", "Casey", "Insurance Agent", 3210])
salary_table.add_row([4, "Jimmie", "Gonzalez", "Respiratory Therapist", 1870])
salary_table.add_row([5, "Gary", "Arnold", "Historian", 4440])
salary_table.add_row([6, "Rafael", "Cobb", "Occupational Therapist", 6500])
salary_table.add_row([7, "Roland", "Pittman", "Telemarketer", 3430])


def employees(table=salary_table):
    table.set_style(DOUBLE_BORDER)
    return table.get_string(fields=["id", "First name", "Last name"])

def salary(table=salary_table):
    table.set_style(DOUBLE_BORDER)
    return table.get_string(fields=["Position", "Salary '$'"])


if __name__ == "__main__":
    salary_table.set_style(DOUBLE_BORDER)
    print(salary_table.get_string())




