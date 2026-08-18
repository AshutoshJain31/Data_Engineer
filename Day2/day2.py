# name=input("Enter Your name: ")
# age = int(input("Enter your Age : "))
# role= input("Enter your role : ")
# print(f"Hello my name is {name}, I am {age} years old and I work as a {role}.")


# Task 2 Arithmatic Operation 

a=20
b=7

# print("The sum of",a,"and",b,"is",a+b)
# print("The difference of",a,"and",b,"is",a-b)
# print("The product of",a,"and",b,"is",a*b)
# print("The quotient of",a,"and",b,"is",a/b)
# print("The floor division of",a,"and",b,"is",a//b)
# print("The remainder of",a,"and",b,"is",a%b)
# print("The power of",a,"and",b,"is",a**b)

# Task 3 Comparison Operators

age = 27
required_age = 18

# print("Is age greater than required age?",age>required_age)
# print(f"Is age is less that requied age? {age<required_age}")
# print(f"If age is equal to required age? {age==required_age}")
# print(f"If age is not equal to required age? {age!=required_age}")
# print(f"If age is greated than or equal to required age? {age>=required_age}")
# print(f"If age is less than or equal to required age? {age<=required_age}")


#Task 4 Logical Operators

age = 27
experience = 18

# print(f"is age is grate the 18 {age>=18 and experience >=18 } ")
# print(f"is age is grate the 18 {age<=18 or experience >18 } ")
# print(f"is age is grate the 18 {not age<=18 } ")

minimum_experience = 5
minimum_age = 18

# print(f"Is employee eligible for the job?{minimum_experience>3 and minimum_age>16}")

#Task 5 If Else Statement

My_Age = 8

if (My_Age>=18):
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

Experience =int(input("Enter your experience in years: "))

if (Experience<3):
    print("You are at biginner level.")
elif(Experience>=3 and Experience<=5):
    print("You are at intermediate level.")
else:
    print("You are at expert level.")


# Task 6
salary=int(input("Enter your salary: "))

if (salary>=120000):
    print("Salary Cetegory : High")
else:
    print("Salary Cetegory : Low")

print(f"excepted salary as per 20% increment is {salary+(salary*0.20)}")