name=input("Enter Your name: ")
age = int(input("Enter your Age : "))
experience= int(input("Enter your experience in years: "))
salary=int(input("Enter your salary: "))

if(age>=18 and experience>=5):
    print(f"Hello {name} you are eligible for the job.")
    print(f"current salary is {salary}")
    print("Incremented Amount is ",salary * 0.20)
    print("Total Salary after increment is ",salary + salary*0.20)
    print(f"Hello {name}, you are eligible for the job. your incremented salary will be 20% that is {salary + salary*0.20}")
else:
    print(f"Hello{name}, Sorry you are not eligible for the job.")