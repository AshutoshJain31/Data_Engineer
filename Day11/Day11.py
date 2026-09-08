numbers=[2,4,5,6,343,142,54,53,323]
names=["Ashutosh","Vijay","Vanita"]
square=[num * num for num in numbers]

# for num in numbers:
#     square.append(num * num)

print(square)

uppername=[name.upper() for name in names]

print(uppername)

even=[num for num in numbers if num%2 == 0  ]

print(even)

employees=[{"name":"Ashutosh","role": "Software Engineer","experience":12},{"name":"Vijay","role": "Senior Software Engineer","experience":4}]

experience=[employee for employee in employees if employee["experience"]>=5]
print(experience)