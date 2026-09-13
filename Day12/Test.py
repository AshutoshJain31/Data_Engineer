# Question 1

invoice_number = "90001234"

invoice_amount = 12500.50

retry_count = 3

is_processed = False

company_codes = ["IN01", "IN02", "DE01"]

# print(type(invoice_number))
# print(type(invoice_amount))
# print(type(retry_count))
# print(type(is_processed))
# print(type(company_codes))

# Question 2

amount = "1500.50"

tax = 250

total = float(amount) + tax

print(total)

# If float is removed, it will give and error becasue string can not be converted into integer.

# Ques 3
#   = this operator is used to assign value to variable. Like a= 10
#   ==  this operator is use to compare the two values. Like a==b will return boolean value True or False.
#   != this operator use to whether value a is not equal to value b. Like a!=b return boolean value True and False.

a = 10
b = 20

print(f"Value of a is {a} is equal to value of b is {b} : {a==b}")
print(f"Value of a is {a} is not equal to value of b is {b} : {a!=b}")

# question 4

# number = int(input("Enter a number: "))

# if number <= 0:
#     print("invalid Amount")
# elif number > 0 and number < 100000:
#     print("Amount is valid")
# else:
#     print("Approval is required for amount greater than 100000")

# Question 5

# invoices = ["INV101", "INV102", "INV103"]
# counter = 1
# for invoice in invoices:
#     print(f"{counter}: Processing  {invoice}")
#     counter += 1

# output for this is
# Processing  INV101
# Processing INV102
# Processing INV103

# Question 6

attempt = 1

# while attempt <= 3:

#     print(f"Attempt {attempt}")

#     attempt += 1

# Output:
# Attempt 1
# Attempt 2
# Attempt 3

# If attempt +=1 is remove then it will goes in infinite loop becasue attempt value always be 1

# Question 7


def validate_amount(amount):
    if amount > 0:
        return f"Amount is valid: {amount}"
    else:
        return f"Amount is invalid: {amount}"


value = int(input("Enter the amount: "))
result = validate_amount(value)

print(result)

# Question 8

# the main difference betweene list and tuple is list mutable and tuple in imutable.we can appen the data in list but we can not append the data in tuple. List is defined with [] and tuple is defined with ().

# A collection of invoice records that will be updated - list
# A fixed set of month names - tuple
# A queue of failed transactions - list
# Coordinates or other fixed configuration values - tuple

# question 9

# failed_invoices = ["INV101", "INV102"]

# failed_invoices.append("INV103")

# failed_invoices.remove("INV101")

# output
# failed_invoices= ["INV102","INV103"]

# question 10

invoice = {
    "invoice_number": "INV101",
    "company_code": "IN01",
    "amount": 45000,
    "status": "Failed",
}

print(invoice["invoice_number"])
invoice["status"] = "Processed"
print(invoice)
invoice["name"] = "Ashutosh Jain"
print(invoice)

try:
    print(invoice["supplier_name"])
except KeyError:
    print("KeyError: 'supplier_name' does not exist in the dictionary.")

# question 11
company_codes = ["IN01", "IN02", "IN01", "DE01", "IN02"]
unique_codes = set(company_codes)

print(unique_codes)

# output will be {"DE01","IN01","IN02"} using set() function it can be in acending order.

# Question 12
records = [
    {
        "invoice_number": "INV101",
        "company_code": "IN01",
        "amount": 45000,
        "status": "Failed",
    },
    {
        "invoice_number": "INV102",
        "company_code": "IN02",
        "amount": 50000,
        "status": "Processed",
    },
]
failed = []
for record in records:
    if record["status"] == "Failed":

        failed.append(record)

print(failed)

# question 13

supplier_name = " saint-gobain india pvt ltd "

print(supplier_name.strip())

# strip(), lower(), upper(), title(), and replace()
# Strip() removes leading and trailing whitespace from a string.
# Lower() converts all characters in a string to lowercase.
# Upper() converts all characters in a string to uppercase.
# Title() capitalizes the first letter of each word in a string.
# Replace() replaces occurrences of a specified substring with another substring in a string.

result = supplier_name.replace("saint-gobain", "Saint-Gobain")

print(result)

result = supplier_name.lower()

print(result)

# question 14

a = "Failed"

result = a.upper()

print(result)


status = "failed"

status.upper()

print(status)

# output is failed

# question 15
import datetime

start_date = "2025-09-01"
end_date = "2026-09-08"

print(
    datetime.datetime.strptime(end_date, "%Y-%m-%d")
    - datetime.datetime.strptime(start_date, "%Y-%m-%d")
)


# this question not understand


# question 16

# with open("invoices.csv", "r", encoding="utf-8") as file:

#     content = file.read()

# Advantage of with open is it automatically close the file after working on that file.It better instade of file.close(). becuse if code fail before open the file and file.close() trigger the it will an error so to avoide that with open we are using.

# question 17 not understand

# Question 18 read the CSV file and print the content of the file in the form of list of dictionary.

import csv

company_codes = ["IN01", "IN02", "DE01"]
error_invoices = []
valid_invoices = []
with open("invoice.csv", "r", encoding="utf-8-sig") as file:
    invoices = csv.DictReader(file)

    for invoice in invoices:
        error = []
        print(invoice)
        if invoice["Invoice number"] == "":
            error.append("Invoice number is missing")
        if int(invoice["Amount"]) < 0:
            error.append("Amount is negative")
        if invoice["company_code"] not in company_codes:
            error.append("Invalid company code")

        if len(error) > 0:
            error_invoices.append({"Invoice": invoice, "Errors": error})
        else:
            valid_invoices.append(invoice)
print("========================================")
print(f"Error Invoices : {error_invoices}")
print(f"Valid Invoices : {valid_invoices}")


with open("error_invoices.csv", "w", newline="") as file:
    write = csv.DictWriter(
        file,
        fieldnames=[
            "Invoice Number",
            "Company code",
            "Amount",
            "Status",
            "Error Message",
        ],
    )
    # write.writerow(
    #     ["Invoice Number", "Company code", "Amount", "Status", "Error Message"]
    # )
    write.writeheader()

    for successinvoice in valid_invoices:
        write.writerow(
            {
                "Invoice Number": invoice["Invoice number"],
                "Company code": invoice["company_code"],
                "Amount": invoice["Amount"],
                "Status": invoice["Status"],
                "Error Message": "",
            }
        )
    # for invoice in error_invoices:
    #     print(invoice)
    #     write.writerow(
    #         [
    #             invoice["Invoice"]["Invoice number"],
    #             invoice["Invoice"]["company_code"],
    #             invoice["Invoice"]["Amount"],
    #             invoice["Invoice"]["Status"],
    #             ",".join(invoice["Errors"]),
    #         ]
    #     )
