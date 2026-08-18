# # List Task 1

# names=["Ashutosh","Rohit","Saurabh","Ankit","Rakesh"]

# print(names)
# print(names[0])
# print(names[1])
# print(names[2])
# print(names[-1])

# names[1]="Rahul"
# names[-2]="Vijay"

# names.append("Rohit")
# names.append("karan")
# names.append("Mansi")

# names.insert(2,"Mohit")
# names.insert(4,"Shriyan")
# print(names)
# names.remove("Rakesh")
# names.pop(3)
# print(names)

# print("Total items in the list",len(names))

# print(f"Total items in the list {len(names)}")

# name_list=["Ashutosh","Piyush","Rahul","Rohit","Arpit","Aniket"]
# search_employee=input("Enter the Employee Name")
# print("Rahul" in name_list)

# print("Rohan" in name_list)

# if(search_employee in name_list):
#     print("Employee Found")
# else:
#     print("Employee Not Found")

# List Slicing

#First 3 Employee
# print(name_list[0:3]) 

#Employee from Index 2 to 4
# print(name_list[2:5])

#Last 2 employee
# print(name_list[-2:])

# If we want to go backword then we need to define the step name_list(start,end,step)
# print(name_list[-2:0:-1])

#All Employee Except first employee
# print(name_list[1:])

# List Sorting 

#.sort() function sort the original list and return it 
# name_list.sort()
# print("sort list using the .sort() : ",name_list)

# sorted function sort the list and create the new list and print it 
# print("The Sorted List using the Sorted function ",sorted(name_list))

numbers_list=[43,54,13,1,42,654]

#  sorted function sort the list and create the new list and print it 
# print(sorted(numbers_list))

# .sort() function sort the original list and return it 
# numbers_list.sort(reverse=True)
# print(numbers_list)


# num_list=[34,43,43,4,545,65,53]

# print(num_list)

# ascending Order
# num_list.sort()
# print(num_list)

# decending Order
# num_list.sort(reverse=True)

# print(num_list)

# print(num_list.count(43))

# print(num_list.index(43))


# name_list=["Ashutosh","Piyush","Rahul","Rohit","Arpit","Aniket"]


# for employee in name_list:
#     print(employee)

# for employee in name_list:
#     if(employee == "Ashutosh"):
#         print(f"employee {employee} present in name_list")

# for employee in name_list:
#     if employee.startswith("A"):
#         print(f"Employee start with A : {employee}")

# Range
# for i in range(5):
#     print(i)

# range(start,end)
# for i in range(2,10):
#     print(i)

# range(start,end,step)

# for i in range(2,22,2):
#     print(i)

# for i in range(1,11):
#     print(f"table of 17 is {17} X {i}: {17*i}")


# Task 12

# print number from one to 10
# for i in range(1,11):
#     print(i)

# Print even number from 2 to 20
# for i in range(2,21,2):
#     print(i)

# print number from 10 to 1
# for i in range(10,0,-1):
     # print(i)


#printing the table 

# num1 = int(input("Please enter the number for creating the table: "))

# for i in range(1,11):
#     print(f"The table of{num1} is {num1} X {i} = {num1 * i}")


#Day3 Challange
employees = ["Ashutosh", "Rahul", "Amit", "Priya", "Karan", "Aniket"]

total_employee=len(employees)

print("total employee count",total_employee)

for employee in employees:
    print("Employee in list",employee)

for employee in employees:
    if(employee.startswith("A")):
        print("Employee name start with A :",employee)

print("Ashutosh exist in employees list","Ashutosh" in employees)

print("Sort Employee List",sorted(employees))

print("First 3 Employee",employees[:3])

print("Last 2 Employee",employees[-2:])