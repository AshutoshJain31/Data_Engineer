class Employee:
    def __init__(self,name,role,experience,salary):
        self.name=name
        self.role=role
        self.experience=experience
        self.salary=salary

    def display_employee(self):
        print(f"name of employee is : {self.name}")
        print(f"Role of employee is : {self.role}")
        print(f"Experience of employee is : {self.experience}")
        print(f"Salary of Employee is : {self.salary}")

    def bonus(self):
        bonussalary = self.salary * 0.10
        return f"Annual 10 % bonus is {bonussalary}"

    def increment_salary(self,percentage):
        currentsalary = self.salary + (self.salary * (percentage/100))
        return currentsalary

employee1 = Employee("Vijay","Software engineer",5,23000)
employee2=Employee("Rohit","Team Lead",9,50000)
employee3=Employee("Vanita","Delivery Manager",12,120000)

employees=[employee1,employee2,employee3]

for emp in employees:
    emp.display_employee()
    print(emp.bonus())
    print(emp.increment_salary(20))

# employee1.name="Ashutosh"
# employee1.role="Software Engineer"
# employee1.experience=5

# employee1.display_employee()
# employee2.display_employee()
# print("Increment Salary is ",employee1.increment_salary(10))
# print(employee1.bonus())
print(employee2.bonus())
# print(employee1.name)
# print(employee1.role)
# print(employee1.experience)


# print(employee2.name)
# print(employee2.role)
# print(employee2.experience)