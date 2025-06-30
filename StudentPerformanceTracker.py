# Student Performance Tracker : 

# Dataset: Create a DataFrame manually with student names, marks in 3 subjects, 
# total marks, and grades.

# Practice:

# Calculate total marks using iteration or column sum.

# Create a categorical Series for Grade (A/B/C) based on total marks.

# Append new students, then remove one.

# Print top 3 students using head().

import pandas as pd

Record = {
    "student" : ["Ali","Taaha","Hani","basit","Usman","Qadir","Mustafa"],
    "Math Marks" : [91,92,93,94,95,96,97],
    "English Marks" : [81,82,83,84,85,86,87],
    "Science Marks" : [71,72,73,74,75,76,77],
}

df = pd.DataFrame(Record,index=["Student 1","Student 2","Student 3","Student 4","Student 5","Student 6","Student 7"])

df["Total Marks"] = df["Math Marks"] + df["English Marks"] + df["Science Marks"]

def AssignGrade(total):
    if(total >= 255):
        return 'A'
    elif total >= 240:
        return 'B'
    else:
        return 'C'
    
grades = df["Total Marks"].apply(AssignGrade)
df["Grade"] = pd.Categorical(grades,categories=["A","B","C"],ordered=True)
print(df)
    
# we need to add new student (Royam)
newStudent ={
    "student" : ["Royam"],
    "Math Marks" : [98],
    "English Marks" : [88],
    "Science Marks" : [78]
}
df1 = pd.DataFrame(newStudent,index=["Student 8"])
df1["Total Marks"] = df1["Math Marks"] + df1["English Marks"] + df1["Science Marks"]
    
grades = df1["Total Marks"].apply(AssignGrade)
df1["Grade"] = pd.Categorical(grades,categories=["A","B","C"],ordered=True)

resdf = pd.concat([df,df1])
print("\n")
print("Updated Record : \n")
print(resdf)


resdf.drop(index=["Student 3"],inplace=True)
print("\n")
print("Updated Record : \n")
print(resdf)

print("\n")
top_students = df.sort_values(by="Total Marks",ascending=False).head(3)
print("Top 3 Students \n",top_students)