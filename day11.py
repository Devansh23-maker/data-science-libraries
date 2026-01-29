🎉🎨 Seaborn Completed + IPL Dataset Project!

Day 11 – Another huge milestone achieved! I’ve completed Seaborn and also applied it on a real-world IPL dataset 🏏📊

This helped me understand how data visualization works in actual sports analytics, not just in sample examples.

What I did with the IPL dataset:
🏏 Analyzed team performances
📈 Visualized runs, wickets & match trends
🔥 Used bar plots, heatmaps & count plots
🎯 Compared players & teams visually
🧠 Gained insights from real match data

What I learned in Seaborn:
✅ Distribution plots
✅ Categorical plots
✅ Heatmaps
✅ Pair plots
✅ Styling & themes
✅ Working directly with Pandas DataFrames

Progress Tracker:
NumPy ✅
Pandas ✅
Matplotlib ✅
Seaborn ✅

Learning + Real Data = Real Skill 💯

From coding to cricket analytics… this journey just got even more exciting! 🏏🚀

Some highlights of the code -->

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# we use warnings so that even after running code it shows output sometimes but it diaplays some warnings to remove that we display this!
import warnings
warnings.filterwarnings("ignore")

df = pd.read_csv( 'IPL.csv')

df.head()

print(f"your rows are {df.shape[0]} and your columns are {df.shape[1]}")

match_wins = df['match_winner'].value_counts()
match_wins

#SeabornCompleted
#IPLDataAnalysis
#DataScience
#Python
#Seaborn
#DataVisualization
#LearningInPublic
#GitHubDaily
#Consistency
