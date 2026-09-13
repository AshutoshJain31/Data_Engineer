import pandas as pd

employee_data = pd.DataFrame(
    {
        "Name": ["Ashutosh", "Rahul", "Vijay", "Mansi", "Amit"],
        "Role": [
            "RPA Engineer",
            "Data Engineer",
            "Developer",
            "Team Lead",
            "data Analyst",
        ],
        "Experience": [5, 3, 4, 7, 2],
        "Salary": [70000, 545454, 544554, 54545, 42323],
        "Department": ["Automatio", "Data", "IT", "Automation", "Data"],
    }
)

# print(employee_data)

# print(f"first 3 rows : {employee_data.head(3)}")

# print(f"Last 3 rows : {employee_data.tail (2)}")


print(employee_data.shape)

print(employee_data.columns)

print(employee_data.info())

# print(employee_data.describe())

print(employee_data["Salary"])

print(employee_data.iloc[0, :])

print(f"max salary {max(employee_data['Salary'])}")
print(f"max salary {min(employee_data['Salary'])}")
print(f"max salary {employee_data['Salary'].mean(numeric_only=True)}")

print(employee_data[employee_data['Salary']>60000])
