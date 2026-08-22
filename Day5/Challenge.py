employees = [
    {"name": "Ashutosh", "role": "RPA Engineer", "experience": 5},
    {"name": "Rahul", "role": "Data Engineer", "experience": 3},
    {"name": "Mansi", "role": "Data Engineer", "experience": 6},
    {"name": "Amit", "role": "Software Engineer", "experience": 4}
]
# display all employee
def display_employee(employees):
    for i in employees:
        print(f"{i["name"]} => {i["role"]} => {i["experience"]}")

display_employee(employees)

# Display employee where role is Data Engineer

def find_data_engineer(emp):
    for i in emp:
        if(i["role"] == "Data Engineer"):
            print(i["name"])

find_data_engineer(employees)

# Find Experience Employee

def experience_employee(emp,minexp=5):
    for i in emp:
        if(i["experience"]>=minexp):
            print(f"experience person: {i["name"]}")

experience_employee(employees)
experience_employee(employees,4)

# Count of data engineer where role is data engineer

def count_data_engineer(emp):
    result = 0
    for i in emp:
        if(i["role"] == "Data Engineer"):
            print(i["name"])
            result = result +1
    return result

final_result =count_data_engineer(employees)
print(final_result)