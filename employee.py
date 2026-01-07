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
    name = input("Employee Name: ")
    emp_id = input("Employee ID: ")
    department = input("Department: ")

    basic = float(input("Basic Salary: "))
    hra = float(input("HRA: "))
    allowances = float(input("Allowances: "))

    gross_salary = calculate_gross_salary(basic, hra, allowances)
    grade = assign_grade(gross_salary)

    print("\n----- Salary Report -----")
    print("Name:", name)
    print("Employee ID:", emp_id)
    print("Department:", department)
    print("Gross Salary: ₹", gross_salary)
    print("Grade:", grade)

if __name__ == "__main__":
    main()
