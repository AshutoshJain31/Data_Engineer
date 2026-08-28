# String Manipulation

name="Ashutosh"

for i in name:
    print(f"Index {i}")

print(len(name))

print(name[::3])

print(name[:-1])

# Built in method for string manipulation

text ="Ashutosh Jain"

print(text.upper())
print(f"Lower case text : {text.lower()}")
print(f"trim spaces text : {text.strip()}")
print(f"Replace text text : {text.replace("Jain","Bulanakr")}")
print(f"Name start with a : {text.startswith("A")}")
print(f"Name end with Jain : {text.endswith("Jain")}")

# Split

print(text.split())

language="python,Java,Jabascript,React,NodeJS"

print(language.split(","))

skills=["Communication","Writing","Reading"]

print(",".join(skills))


for i in skills:
    print(i)

# Skill Joining
print("-> ".join(skills))

split_text=text.split();
print(split_text)

print(f"first name : {split_text[0]}")
print(f"Last name : {split_text[1]}")


# find 

string1="Ashutosh Jain Ashutosh"

print(string1.find("jain"))

print(string1.count("Ashutosh"))

print(string1.startswith("A"))

print(string1.endswith("Jain"))

print(string1.isalpha())

print(string1.isdigit())

print(string1.find("Jain"))
print(string1.count("Ashutosh"))

value = "a123"

if(value.isdigit()):
    print("valid")
else:
    print("Invalid")

    
    