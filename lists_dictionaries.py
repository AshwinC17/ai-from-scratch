# Lists and Dictionaries

# LISTS
numbers = [10, 20, 30, 40, 50]
print("Numbers:", numbers)

# Access first element
print("First element:", numbers[0])

# Access last element
print("Last element:", numbers[-1])


# Slicing
print("First three:", numbers[:3])

print("From third:", numbers[2:])

print("Reversed:", numbers[::-1])


# Add element
numbers.append(60)
print("After append:", numbers)


# Remove element
numbers.remove(20)
print("After remove:", numbers)


# -------------------------

# DICTIONARIES

student = {
    "name": "Ashwin",
    "age": 24,
    "skills": ["Python", "Java", "C++"]
}

print("\nStudent name:", student["name"])

print("Student age:", student["age"])

print("Student skills:", student["skills"])


# Add new key
student["learning"] = "Artificial Intelligence"

print("Learning:", student["learning"])

print("\nStudent details:")
print(student)