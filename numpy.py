import numpy as np

a = np.array([10, 20, 30, 40, 50])

print("Original:", a)
print("Add 5:", a + 5)
print("Multiply by 2:", a * 2)
print("Greater than 25:", a[a > 25])
print("Even numbers:", a[a % 2 == 0])
