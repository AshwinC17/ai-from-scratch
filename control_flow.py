# Python Control Flow


# -------------------------
# IF, ELIF, ELSE
# -------------------------

age = 24

if age >= 18:
    print("Adult")
elif age >= 13:
    print("Teenager")
else:
    print("Child")


# -------------------------
# COMPARISON OPERATORS
# -------------------------

a = 10
b = 20

print("a == b:", a == b)
print("a != b:", a != b)
print("a > b:", a > b)
print("a < b:", a < b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)


# -------------------------
# LOGICAL OPERATORS
# -------------------------

age = 24
has_id = True

if age >= 18 and has_id:
    print("Allowed")


temperature = 30

if temperature < 0 or temperature > 35:
    print("Extreme temperature")
else:
    print("Normal temperature")


is_raining = False

if not is_raining:
    print("You can go outside")


# -------------------------
# FOR LOOP
# -------------------------

numbers = [1, 2, 3, 4, 5]

for number in numbers:
    print("Number:", number)


# -------------------------
# RANGE
# -------------------------

for i in range(5):
    print("Value:", i)


for i in range(1, 6):
    print("Value:", i)


# -------------------------
# WHILE LOOP
# -------------------------

count = 1

while count <= 5:
    print("Count:", count)
    count += 1


# -------------------------
# BREAK
# -------------------------

for number in range(1, 10):
    if number == 5:
        break

    print("Break example:", number)


# -------------------------
# CONTINUE
# -------------------------

for number in range(1, 6):
    if number == 3:
        continue

    print("Continue example:", number)


# -------------------------
# NESTED LOOPS
# -------------------------

for i in range(1, 4):
    for j in range(1, 4):
        print("i:", i, "j:", j)