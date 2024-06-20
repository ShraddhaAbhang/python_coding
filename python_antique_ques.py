# Q1) What does this print?

# Unpack the list [1, 2, 3, 4, 5, 6] and assign the first value to a dummy variable (___), 
# and the next three values to a, b, and c respectively.
___, a, b, c = [1, 2, 3, 4, 5, 6]
print(a, b, c)  # Output: 2 3 4

# -------------------------------------------------------------------------------- #

def testing():
    # Print a message and return a tuple (1000, 1001)
    print('hello!!')
    return 1000, 1001

# Call the testing function and unpack its return values into a and b.
a, b =  testing()
print(b)  # Output: 1001

# -------------------------------------------------------------------------------- #

def addition(a, b):
    # Calculate the sum of a and b and return it.
    sum =  a + b
    return sum

# Call the addition function with arguments 5 and 10, store the result in res.
res = addition(5,10)
print(res)  # Output: 15

# -------------------------------------------------------------------------------- #

def string():
    # Return a predefined string.
    str = "Hi, my name is Shraddha Abhang"
    return str

# Call the string function, store the result in res.
res = string()
print(res)  # Output: Hi, my name is Shraddha Abhang

# -------------------------------------------------------------------------------- #

def fun(name, surname):
    # Print the name and surname.
    print(name, surname)

# Call the fun function with arguments "Shraddha" and "Abhang".
fun("Shraddha", "Abhang")  # Output: Shraddha Abhang

# -------------------------------------------------------------------------------- #

def fun(name = "Shraddha"):
    # Print the name (default is "Shraddha" if not provided).
    print(name)

# Call the fun function with argument "Sahil".
fun("Sahil")  # Output: Sahil

# -------------------------------------------------------------------------------- #

def substraction(a, b):
    # Calculate the difference of a and b and return it.
    sub =  a - b
    return sub

# Call the substraction function with arguments 5 and 10, store the result in res.
res = substraction(5,10)
print(res)  # Output: -5

# -------------------------------------------------------------------------------- #

def main(a, b):
    # Use the addition function to calculate the sum of a and b.
    add = addition(a, b)
    # Use the substraction function to calculate the difference of a and b.
    sub = substraction(a, b)
    # Return both the sum and the difference.
    return add, sub

# Call the main function with arguments 50 and 15, unpack the results into add and sub.
add, sub = main(50,15)
print(sub)  # Output: 35
