import calculator as cal
import math , random , datetime , os

print(cal.add(12,4,5,5,5,5))

print(cal.multiply(12,4,5,5,5,5))


print(f"pi value is {math.pi:.3f}")

print(math.sqrt(144))

print(random.randint(1,10))

date=datetime.datetime.now()

print(date)

print(date.date())

print(date.strftime("%A,%d-%m-%Y %H:%M:%S -  %b"))

print(os.getcwd())

print(os.listdir())


if not os.path.exists("test"):
    os.mkdir("test")
    print("Folder created Successfully")
else:
    print("Folder already Exist.")
