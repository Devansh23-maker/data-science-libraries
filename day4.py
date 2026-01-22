import numpy as np

marks = np.array([
    [60, 70, 80],
    [40, 55, 65],
    [90, 85, 88],
    [30, 45, 50]
])

print("Shape:", marks.shape)

# Student-wise average
print("Student averages:", np.mean(marks, axis=1))

# Subject-wise average
print("Subject averages:", np.mean(marks, axis=0))

# Students who scored more than 70 in Math
print("Top in Math:", marks[marks[:,0] > 70])
