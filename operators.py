# NOTE: Run this in a Interactive window for simplicity.

# Python Arithmetic Operators (+, -, *, /, %, **, //)

# Print all even numbers from 1 to 10.
for a in range(1,11):
    if (a % 2) == 0:
        print(a)

# Print all odd numbers from 1 to 10.
for a in range(1,11):
    if (a % 2) != 0:
        print(a)

# Multiply two numbers and print the result.
a = 1
b = 10
c = a * b
print(c)

# Divide two numbers and print the result.
a = 10
b = 2
c = a / b
print(c)

# Subtract two numbers and print the result.
a = 10
b = 2
c = a - b
print(c)


# Python Comparison Operators (==, !=, >, <,  >=,  <=)

# Check if two numbers are not equal.
a = 5
b = 3
print(a != b)

# Check if one number is greater than or equal to another.
a = 5
b = 3
print(a >= b)

# Check if one number is less than another.
a = 5
b = 3
print(a < b)


# Python Logical Operators (and, or, not)

# Check if a number is greater than 3 and less than 10.
a = 5
print(a > 3 and a < 10)     # Returns True if both statements are true

# Check if a number is greater than 3 or less than 4.
a = 5
print(a > 3 or a < 4)       # Returns True if one of the statements is true

# Reverse the result of a logical expression.
a = 5
print(not(a > 3 and a < 10))    # Reverse the result, returns False if the result is true
