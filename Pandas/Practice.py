import pandas as pd

Userdetails = pd.DataFrame(
    {
        "Name": ["Ashutosh", "Vijay", "Vanita", "Mansi"],
        "Age": [27, 58, 47, 27],
        "Skill": ["Python", "JavaScript", "React", "Automation Anywhere"],
    }
)

singleUser = pd.Series(
    [12, 3, 2, 3, 3, 3], index=["one", "two", "Three", "four", "Five", "six"]
)
print(Userdetails)
print(singleUser.head(3))
print(singleUser.index)