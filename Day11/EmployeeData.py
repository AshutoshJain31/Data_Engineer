import csv


def highest_Salary():
    temp = 0
    for emp in employees:
        if(int(emp["Salary"]) > temp):
            temp = int(emp["Salary"])
            emp_name = emp["Name"]
    return temp,emp_name

def lowest_Salary():
    temp = 1000000000000000000
    print(f"Temp is {temp}")
    for emp in employees:
        if(int(emp["Salary"]) < temp):
            temp = int(emp["Salary"])
    return temp

def average_Salary():
    total_salary = 0
    for emp in employees:
        total_salary += int(emp["Salary"])
    average = total_salary / len(employees)
    return average

def experience_employee():
    for emp in employees:
        if int(emp["Experience"]) >= 5:
            temp = emp["Name"]
    return temp

with open("Employee.csv", "r") as file:
    employees = list(csv.DictReader(file))

    highest_salary = highest_Salary()
    lowest_salary = lowest_Salary()
    average_salary = average_Salary()
    experienced_employee = experience_employee()
    
    total_employee = len(employees)
    print(f"Count of total employee is {total_employee}")
    print(f"Highest salary is {highest_salary[0]} and employee name is {highest_salary[1]}")
    print(f"Lowest salary is {lowest_salary}")
    print(f"Average salary is {average_salary}")
    print(f"Experienced employee is {experienced_employee}")
