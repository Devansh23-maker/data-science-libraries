Day 8: GFG Practice – Core Python Logic & Problem Solving

Today I focused purely on solving GeeksForGeeks (GFG) style problems to strengthen my problem-solving mindset.
This helped me move from “writing code” to actually thinking like an interviewer.

Problems I practiced:

Palindrome checking (string & array)

Frequency counting using dictionary

Removing duplicates from a list

Finding max, min, sum

Even/Odd separation

List rotation

Example (Palindrome Array – GFG):

def isPalinArray(arr):
    for num in arr:
        s = str(num)
        if s != s[::-1]:
            return False
    return True
