def data(name):
    print("RPA Programming")
    print("Welcome to team")
    print(f"Welcome {name}")
for i in range(4):
    data("Ashutosh")

def details(name,experience):
    if(experience>5):
        print(f'{name} has experience person')
    else:
        print(f'{name} need more experience')

details("Ashutosh",5)

def increment(salary,increment):
    return salary+(salary * increment/100)

result= increment(30000,20)

print(f"Incremented salary is {result}")

# Check Even of odd

def check_even(num):
    if(num%2 == 0):
        print(f"{num} is Even.")
    else:
        print(f"{num} is Odd.")

userNumber= int(input("Enter Number : "))

check_even(userNumber)

# calculate the price

def calculate(price,quentity):
    return price * quentity


for i in range(3):
    price=int(input("Enter the price : "))
    quentity=int(input("Enter the quentity : "))
    # result = calculate(price,quentity)
    print(f"{i} : result for {price} and {quentity} is {result}")


def printDetails(name,age,experience):
    print(f"name is {name}")
    print(f"Age is {age}")
    print(f"experience is {experience}")


printDetails(name="Ashutosh",age=23,experience=4)

# Args

def function23(*num):
    total=0
    for i in num:
        total = total +i
    return total

result = function23(10,34,34,3,43,3)

print(result)

def details(**detail):
    for key,value in detail.items():
        print(f"{key} : {value}")


details(name="Ashutosh Jain",Age=32,Experience=5,Role="Senior Software Enineer")
details(name="Rahul",Age=32)