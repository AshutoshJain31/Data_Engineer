try:
    number= int(input("Please enter the number"))
    print("Entered Number Is ",number )
except ValueError:
    print("Enter Valid Number")
except TypeError:
    print("Entered date Data type does not correct")
except KeyError:
    print("Key not found")


try:
    num1=int(input("Please enter the first number : "))
    num2=int(input("Please enter the second number : "))
    operation = input("Please enter the operation add,substract,multiply,division")

    if(operation == "add"):
        print(num1+num2)
    elif(operation == "substract"):
        print(num1-num2)
    elif(operation == "multiply"):
        print(num1 * num2)
    else:
        print(num1/num2)
except ValueError:
    print("Please enter the correct value")
except ZeroDivisionError:
    print("number can not ne devide by zero")

data=[10,20,"abf",43,"dcd"]
count =0
for i in data:
    try:
        value = int(i)
        print(f"Valid Integer {i}")
    except :
        print(f"Invalid Integer {i}")
        count +=1
print(f"Total Invalid data is {count}")