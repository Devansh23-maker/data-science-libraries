#  Data Science Libraries Journey

Day 2 & 3 Progress Update 

Today I worked on strengthening my Python fundamentals and started exploring NumPy.

## 🔹 Python Practice
- Reversing numbers and strings
- Palindrome checking (number & array based)
- List operations:
  - Finding max & min
  - Removing duplicates
  - List rotation
  - Even/Odd separation
- Dictionary & Set revision

## 🔹 Interview Question Solved
**Check if all elements in an array are Palindrome**
```python
def isPalinArray(arr):
    for num in arr:
        s = str(num)
        if s != s[::-1]:
            return False
    return True
