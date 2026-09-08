import csv

# with open("Employee.csv", "w", newline="") as file:
#     fieldname = ["Name", "Role", "Experience", "Salary"]
#     data = csv.DictWriter(file, fieldname)
#     data.writeheader()
#     data.writerows(
#         [
#             {
#                 "Name": "Rahul",
#                 "Role": "Software Engineer",
#                 "Experience": 5,
#                 "Salary": "12000",
#             },
#             {
#                 "Name": "Ashutosh",
#                 "Role": "Engineer",
#                 "Experience": 3,
#                 "Salary": "80000",
#             },
#         ]
#     )
#     print(data)
#     # for row in data:
#     #     print(f"Name : {row["Name"]}")
#     #     print(f"Name : {row["Name"]}")


def incremen(name, salary):
    if int(salary) >= 70000:
        return ("Bonus for", name, "is", int(salary) * 0.10)
    else:
        return ("Bonus for", name, "is", int(salary) * 0.05)


with open("Employee.csv", "r") as file:
    employeeData = csv.DictReader(file)

    # for employee in employeeData:
    #     print(f"Name :{employee["Name"]}")
    #     print(f"Experience : {employee["Experience"]}")
    #     print(f"Role : {employee["Role"]}")
    #     print(f"Salary : {employee["Salary"]}")
    #     print("----------------------")

    # Experience Employee
    # for employee in employeeData:
    #     if int(employee["Experience"]) >= 5:
    #         print(f"{employee["Name"]} - {employee["Role"]} - {employee['Experience']}")

    # Developer Role Employee
    # for employee in employeeData:
    #     if "Engineer" in employee["Role"]:
    #         print(f"{employee["Name"]} - {employee["Role"]} - {employee['Experience']}")

    # Incremented Salary

    for employee in employeeData:
        name = employee["Name"]
        salary = employee["Salary"]
        result = incremen(name, salary)
        print(result)
