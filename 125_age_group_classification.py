# 4 age group classification

age = 65

group = (
    "Child" if age < 13 else
    "Teen" if age < 20 else
    "Adult" if age < 60 else
    "Senior"
)

print(group) # Senior

# uses multiple ternary operators to classify age.

