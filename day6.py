Day 6: Pandas Basics – DataFrames, Columns & Filtering

# 🐼 Pandas Basics – Working with Real Data

Today I started learning Pandas, the most important library for handling real-world datasets in Python.

What I learned:
- Creating a DataFrame
- Accessing columns
- Basic filtering
- Understanding how Pandas connects NumPy and Seaborn

```python
import pandas as pd

data = {
    "name": ["Ami", "Ravi", "Neha", "Karan"],
    "marks": [78, 45, 89, 60],
    "gender": ["F", "M", "F", "M"]
}

df = pd.DataFrame(data)

print(df)
print(df["marks"])
print(df[df["marks"] > 60])
