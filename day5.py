🔥 Day’s GitHub Update – NumPy Completion Sprint! 🔥

Today was all about wrapping up NumPy and strengthening the core concepts.
I focused on revision + hands-on practice so that nothing remains half-baked.

📌 What I covered today:

Array creation & reshaping

Indexing and slicing

Broadcasting

Axis operations (axis=0, axis=1)

Mean, Sum, Max, Min on matrices

Boolean masking

Mini problem solving (Marks matrix analysis)

Histogram concepts (bins)

Transition from Seaborn to Plotly for visualization

MOST IMP -> 

NumPy Mini Project Completed 🧩🔥  

Built a Sudoku Validator using NumPy.  
Used matrix operations and axis-based summation to validate Sudoku rows.

What I learned today:
- How to apply np.sum() with axis
- How to validate matrix-based rules
- How NumPy can be used in real-world logical problems
- Transitioning from practice problems to mini projects

This marks the completion of my NumPy core revision.  
Next focus: Pandas + Real Dataset Analysis.

s = np.array([
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],

    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9]
])

valid = True
for i in b:
    if i != 45:
        valid = False
        break

if valid:
    print("SUDOKU IS VALID!")
else:
    print("INVALID SUDOKU!")
