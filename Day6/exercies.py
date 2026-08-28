# Exercies one
name="Ashutosh Jain"

print(f"First Character {name[0]}")
print(f"last Character {name[-1]}")
print(f"First 8 Character {name[0:8]}")
print(f"Last 4 Character {name[-4:]}")
print(f"length of string string is {len(name)}")


# Exercies 2
text =" Python is very Powerfull  "

print(text.upper())
print(text.lower())
print(text.strip())
print(text.replace("Powerfull","usefull"))

# Exercies 3

data = "Ashutosh|RPA Engineer|5"

print(data.split("|"))

# Exercies 4

skills = ["Python", "SQL", "Power BI", "Git"]

for i in skills:
    print(i)

print(",".join(skills))
email = "  ASHUTOSH@GMAIL.COM  "

print(email.strip().lower())