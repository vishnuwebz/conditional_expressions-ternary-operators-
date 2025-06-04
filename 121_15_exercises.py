"""A Conditional Expression (also called a Ternary Operator) is a one-line shorthand for if-else in Python.

Purpose: Quickly assign values or return expressions based on a condition — all in one line.

syntax:

value_if_true if condition else value_if_false

"Umbrella" if raining else "No Umbrella"

"""

# standard vs ternary comparison

# traditional if-else

age = 17
if age >= 18:
    status = "Adult"
else:
    status = "Minor"

# conditional expression (ternary)
status = "Adult" if age >= 18 else "Minor"


print("---------------------------------------------------")

print("ex 1: assign value based on condition")

temp = 36
status = "Fever" if temp > 37 else "Normal"

print(status)

# returns fever only if temp > 27

print("---------------------------------------------------")

print("ex 2: inside a function")

def eligibility(age):
    return "Eligible" if age >= 18 else "Not Eligible"
print(eligibility(20))  # Eligible

# based on age, returns eligibility criteria

print("---------------------------------------------------")

print("ex 3: with input")

# num = int(input("Enter a number: "))
# result = "Even" if num % 2 == 0 else "Odd"

# print(result)

# uses conditional expression to check even/odd
"""
3: with input
Enter a number: 87
Odd
"""
print("---------------------------------------------------")

print("1: check if number is positive or negative")

num = -10
print("Positive" if num > 0 else "Negative")

# uses ternary to classify number

print("---------------------------------------------------")

print("2: return greater number")

a, b = 9, 8

print(a if a > b else b)

# returns the greater of the two


print("---------------------------------------------------")

print("3: check if string is empty")

text = ""
print("Empty" if text == "" else "Not Empty")

# Checks if string has any content

print("---------------------------------------------------")

print("4: Assign default if variable is None")

username = None
print(username if username else "Guest")

# uses default value when None or empty

print("---------------------------------------------------")

print("5: Compare lengths of strings")

s1 = "hi"
s2 = "hello"
print(s1 if len(s1) > len(s2) else s2)

# prints the longer string

print("---------------------------------------------------")

print("6 Check leap year")

year = 2020

print("Leap" if year % 4 == 0 else "Not leap")

# simple leap year rule

print("---------------------------------------------------")

print("7: Adult or Minor")

age = 15

print("Adult" if age >= 18 else "Minor")

# checks age-based category

print("---------------------------------------------------")

print("8: Temperature alert")

temp = 39

print("High Fever" if temp >= 38 else "Normal")
# Determines if temperature is high

print("---------------------------------------------------")

print("9: Boolean flag")

is_logged_in = False

print("Welcome Back!" if is_logged_in else "Please Log In")

# Choose message based on login status

print("---------------------------------------------------")

print("10: Largest of 3(Nested ternary")


a,b,c = 4,9,6
print(a if a > b and a > c else b if b > c else c)

# uses nested ternary to find largest number



print("---------------------------------------------------")

print("11: Check divisibility")

num = 10

print("Divisible by 5" if num % 5 == 0 else "Not Divisible")

# Quick divisible check

print("---------------------------------------------------")

print("12: score grading")

score = 85

print("Pass" if score >= 50 else "Fail")

# Quick grade logic.

print("---------------------------------------------------")

print("13: Category check")

gender = 'M'

print("Male" if gender == "M" else "Female")

# gender shortcut

print("---------------------------------------------------")

print("15: String contains check")

text = "hello world"

print("Found" if "world" in text else "Not Found")

# uses in with ternary

print("---------------------------------------------------")

