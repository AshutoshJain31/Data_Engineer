# # # Read data from the file
# # file = open("Employees.txt","r")

# # # print(file.read())
# # employees=file.readlines()
# # # print(file.readline())

# # # print(file.readlines())

# # for i in employees:
# #     print(i.strip())


# # file.close()

# # # Write Data into file

# # file=open("output.txt","w")

# # file.write("Name\n")
# # file.write("Rahul\n")
# # file.write("Krishna\n")
# # file.write("Rohit\n")

# # file.close()

# # readfile=open("output.txt","r")

# # readData=readfile.readlines()

# # print(readData)

# # appendfile=open("output.txt","a")

# # apenddata=appendfile.write("Rohan\n")
# # appendfile.write("Mohit\n")
# # appendfile.close()
# # readfile1=open("output.txt","r")

# # print(readfile1.readlines())

# skills=["Python","Javascript","React","java","HTML","CSS"]
# file = open("text.txt","a")

# for skill in skills:
#     file.write(f"Skill is : {skill} \n")

# file.close()
# readfile=open("text.txt","r")

# print(readfile.readlines())

# Using the With open 

# with open("Skills.txt","a") as file:
#     file.write(f"Python\n")
#     file.write(f"JavaScript\n")
#     file.write(f"React\n")
#     file.write(f"Java\n")

# with open("Skills.txt","r") as readfile:
#     print(readfile.readlines())

# import csv
# with open("text.txt","r") as file:
#     # reader=csv.reader(file)
#     reader=csv.DictReader(file)
#     next(reader)
#     for row in reader:
#         if row["role"] == "Team Lead" and int(row["experience"]) >= 5:
#             print(f"Name : {row["name"]} => Role : {row["role"]} => Experience : {row["experience"]}")

import csv

with open("text.txt","r") as file:
    reader=csv.DictReader(file)
    count = 0
    for data in reader:
        count+=1
        if data["role"] == "Data Engineer":
            print(f"{data["name"]} and {data["age"]}")

        if int(data["experience"]) >=5:
            print(f" Experience {data["name"]} and {data["age"]}")
print(f"Total Rows {count}")