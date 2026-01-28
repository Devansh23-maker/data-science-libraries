🎉🚀 Matplotlib Completed – Visualization Level Up!

Day 10 – Big win today! I’ve successfully completed Matplotlib and now my Data Science journey feels truly visual 📊✨

From simple line graphs to meaningful data stories, Matplotlib taught me how powerful visualization really is. Watching raw numbers transform into insights is such a satisfying feeling!

What I learned:
✅ Line plots
✅ Bar charts
✅ Scatter plots
✅ Histograms
✅ Titles, labels & legends
✅ Grid & styling
✅ Plot customization
✅ Subplots
✅ Better understanding of plt.show()

Progress so far:
NumPy ✅ Completed
Pandas ✅ Completed
Matplotlib ✅ Completed
Seaborn 🔥 Starting Next

Now data is not just numbers… it’s a story waiting to be told 📖📈

Next stop → Seaborn
Ready to make my visualizations more beautiful and professional!

Consistency > Motivation 💪

#MatplotlibCompleted
#Python
#DataVisualization
#DataScienceJourney
#LearningInPublic
#GFGPractice
#GitHubDaily
#Consistency

Now the code (final practice examples after completing Matplotlib):

import matplotlib.pyplot as plt
import numpy as np

# Data
x = np.arange(1, 6)
y = [5, 10, 15, 20, 25]

# 1. Line Plot
plt.figure(figsize=(6,4))
plt.plot(x, y, marker='o')
plt.title("Line Plot Example")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.show()


# 2. Bar Plot
plt.figure(figsize=(6,4))
plt.bar(x, y)
plt.title("Bar Plot Example")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()


# 3. Scatter Plot
plt.figure(figsize=(6,4))
plt.scatter(x, y)
plt.title("Scatter Plot Example")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()


# 4. Histogram
data = [12, 15, 20, 20, 25, 25, 25, 30, 35, 40]
plt.figure(figsize=(6,4))
plt.hist(data, bins=5)
plt.title("Histogram Example")
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.show()


# 5. Subplots (Multiple graphs together)
plt.figure(figsize=(10,4))

plt.subplot(1,2,1)
plt.plot(x, y)
plt.title("Line Plot")

plt.subplot(1,2,2)
plt.bar(x, y)
plt.title("Bar Plot")

plt.tight_layout()
plt.show()
