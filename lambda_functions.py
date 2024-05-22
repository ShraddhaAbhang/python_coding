

##############################################################################################
# Lambda approaches
##############################################################################################

##############################################################################################
# Example 1: Simple lambda function for addition
##############################################################################################

# Using lambda functions
addition = lambda x, y: x + y  # Lambda function definition for addition
print(addition(3, 5))  # Output: 8

# Equivalent regular function for addition
def addition(x, y):  # Regular function definition for addition
    return x + y
print(addition(3, 5))  # Output: 8


##############################################################################################
# Example 2: Sorting a list of tuples based on the second element
##############################################################################################

# Sorting a list of tuples based on the second element using lambda
pairs = [(3, 'banana'),(1, 'apple'), (2, 'orange')]
pairs.sort(key=lambda x: x[1])  # Lambda function used as sorting key
print(pairs)  # Output: [(1, 'apple'), (3, 'banana'), (2, 'orange')]

# Sorting using a regular function
def sort_by_second_element(pair):  # Regular function to extract the second element
    return pair[1]
pairs = [(1, 'apple'), (3, 'banana'), (2, 'orange')]
pairs.sort(key=sort_by_second_element)  # Sorting based on a regular function
print(pairs)  # Output: [(1, 'apple'), (3, 'banana'), (2, 'orange')]

# Sorting manually (core Python way)
def sort_by_second_element(pair):  # Regular function to extract the second element
    return pair[1]

pairs = [(1, 'apple'), (3, 'banana'), (2, 'orange')]
sorted_pairs = []

# Sorting manually by finding minimum element iteratively
while pairs:
    min_pair = pairs[0]
    for pair in pairs:
        if sort_by_second_element(pair) < sort_by_second_element(min_pair):
            min_pair = pair
    sorted_pairs.append(min_pair)
    pairs.remove(min_pair)

print(sorted_pairs)  # Output: [(1, 'apple'), (3, 'banana'), (2, 'orange')]

##############################################################################################
# Example 3: Filtering even numbers from a list
##############################################################################################

# Filtering even numbers from a list using lambda with filter()
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))  # Lambda function used with filter
print(even_numbers)  # Output: [2, 4, 6, 8, 10]

# Filtering using a regular function with filter()
def is_even(x):  # Regular function to check if a number is even
    return x % 2 == 0
even_numbers = list(filter(is_even, numbers))  # Filter using a regular function
print(even_numbers)  # Output: [2, 4, 6, 8, 10]

# Filtering manually (core Python way)
def is_even(x):  # Regular function to check if a number is even
    return x % 2 == 0
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = []

# Filtering manually by iterating through each element
for num in numbers:
    if is_even(num):
        even_numbers.append(num)
print(even_numbers)  # Output: [2, 4, 6, 8, 10]


##############################################################################################
# Example 4: Mapping each element of a list to its square
##############################################################################################

# Mapping each element of a list to its square using lambda with map()
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squared_numbers = list(map(lambda x: x ** 2, numbers))  # Lambda function used with map
print(squared_numbers)  # Output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Mapping using a regular function with map()
def square(x):  # Regular function to square a number
    return x ** 2
squared_numbers = list(map(square, numbers))  # Map using a regular function
print(squared_numbers)  # Output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Mapping manually (core Python way)
def square(x):  # Regular function to square a number
    return x ** 2
squared_numbers = []

# Mapping manually by iterating through each element
for num in numbers:
    squared_numbers.append(square(num))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
