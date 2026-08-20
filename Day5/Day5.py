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
