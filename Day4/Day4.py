# Tuple

employee_info=("Ashutosh",27,"Software Engineer",5,"Mumbai")

# print(type(employee_info))
# print(employee_info)
# print(employee_info[0])
# print(employee_info[1])
# print(employee_info[-1])
# employee_info[0]="Vijay"
# print(employee_info)

# print(f"First 3 employee details: {employee_info[0:3]}")
# print(f"Last 2 values are {employee_info[-2:]}")
# print(f"The value at index 2 is {employee_info[2]}")
# print(f"The Length of tuple is {len(employee_info)}")


# Sets
employees={"Ashutosh","Vijay","Amit","Rahul","Rohan","Vijay"}

# print(employees)

# print(type(employees))

# print(len(employees))

# print("Vijay" in employees)

# employees.add("Mansi")
# print(employees)

# print("Mansi" in employees)

# Union , Intersection , Difference

set1={"Ashutosh","Vijay","Vanita","Mohan"}
set2={"Rohit","Vijay","Rahul","Mohan"}

# print(set1.union(set2))
# print(set1.intersection(set2))
# print(set1.difference(set2))

# print(set1 | set2)
# print(set1 & set2)
# print(set1 - set2)

# Dictionary

employee_details={"name": "Ashutosh Jain","age": 27,"Role":"Software Engineer","Experience":5}

employee_details["Country"]="India";

employee_details["Experience"]=9;

employee_details["salary"]=123;

print(type(employee_details))

print(employee_details)

print(employee_details["name"])

print(employee_details["salary"])

print(employee_details.get("dob"))

print(employee_details.keys())
print(employee_details.values())
print(employee_details.items())


for value in employee_details.values():
    print(value)

for key,value in employee_details.items():
    print(f"{key} : {value} ")