def calculate_gross_salary(basic, hra, allowances):
    return basic + hra + allowances

def assign_grade(gross_salary):
    if gross_salary >= 100000:
        return "Grade A"
    elif gross_salary >= 75000:
        return "Grade B"
    elif gross_salary >= 50000:
        return "Grade C"
    elif gross_salary >= 30000:
        return "Grade D"
    else:
        return "Grade E"

def main():
    # Employee details entered here
    name = "Nikhil"
    emp_id = "E032"
    department = "IT"

    basic = 50000
    hra = 20000
    allowances = 10000

    gross_salary = calculate_gross_salary(basic, hra, allowances)
    grade = assign_grade(gross_salary)

    print("----- Salary Report -----")
    print("Name:", name)
    print("Employee ID:", emp_id)
    print("Department:", department)
    print("Basic Salary: Rs.", basic)
    print("HRA: Rs.", hra)
    print("Allowances: Rs.", allowances)
    print("Gross Salary: Rs.", gross_salary)
    print("Grade:", grade)

if __name__ == "__main__":
    main()
