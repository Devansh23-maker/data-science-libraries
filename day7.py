import pandas as pd

data = {
    "name": ["Ami", "Ravi", "Neha", "Karan", "Aman", "Pooja"],
    "marks": [78, 45, 89, 60, 72, 55],
    "gender": ["F", "M", "F", "M", "M", "F"]
}

df = pd.DataFrame(data)

# View data
print(df)

# Basic statistics
print("Average Marks:", df["marks"].mean())
print("Maximum Marks:", df["marks"].max())
print("Minimum Marks:", df["marks"].min())

# Filtering
print(df[df["marks"] > 60])

# Grouping
print(df.groupby("gender")["marks"].mean())

# Sorting
print(df.sort_values(by="marks", ascending=False))

# Adding new column
df["result"] = df["marks"].apply(lambda x: "Pass" if x >= 60 else "Fail")
print(df)

🔹 What I learned today:

DataFrame is the heart of Pandas

mean(), max(), min() give instant insights

df[condition] filters rows

groupby() helps in category-wise analysis

sort_values() orders data

New columns can be created using logic

Pandas alone is enough to perform real data analysis

🎯 Outcome:
Now I understand that Pandas is not just a helper library.
It is a complete data analysis engine by itself.
Visualization is optional, but understanding data is mandatory.
