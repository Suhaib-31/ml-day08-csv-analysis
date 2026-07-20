import pandas as pd

print("===== CSV Data Analysis =====\n")

# Load Dataset
df = pd.read_csv("students.csv")

# Show Dataset
print("Dataset:")
print(df)

# Basic Information
print("\nDataset Info:")
print(df.info())

# Shape
print("\nShape:")
print(df.shape)

# Statistical Summary
print("\nSummary:")
print(df.describe())

# Average Marks
print("\nAverage Marks:")
print(df["Marks"].mean())

# Highest Marks
print("\nHighest Marks:")
print(df["Marks"].max())

# Lowest Marks
print("\nLowest Marks:")
print(df["Marks"].min())

# Top Student
top_student = df[df["Marks"] == df["Marks"].max()]

print("\nTop Student:")
print(top_student)

# Students from Lahore
print("\nStudents from Lahore:")
print(df[df["City"] == "Lahore"])

# Sort by Marks
print("\nSorted by Marks:")
print(df.sort_values(by="Marks", ascending=False))