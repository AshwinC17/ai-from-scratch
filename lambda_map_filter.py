# Lambda, map, filter and zip


numbers = [1, 2, 3, 4, 5]


# -------------------------
# LAMBDA
# -------------------------

square = lambda x: x * x

print("Square of 5:", square(5))


# -------------------------
# MAP
# -------------------------

squares = list(
    map(lambda x: x * x, numbers)
)

print("Squares:", squares)


# -------------------------
# FILTER
# -------------------------

even_numbers = list(
    filter(lambda x: x % 2 == 0, numbers)
)

print("Even numbers:", even_numbers)


# -------------------------
# ZIP
# -------------------------

names = ["Alice", "Bob", "Charlie"]

scores = [90, 85, 95]

data = list(zip(names, scores))

print("Student scores:", data)


# -------------------------
# LIST COMPREHENSION
# -------------------------

cubes = [x ** 3 for x in numbers]

print("Cubes:", cubes)