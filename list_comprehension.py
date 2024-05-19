# Working with tuples

# Create a tuple and print the second element.
t_tupple = (1, 5)
print(t_tupple[1])  # Accessing the second element of the tuple



###################################################################################################
###################################################################################################

# Working with lists

# Create a list and print it.
lst = [2, 5, 8, 6, 4, 3, 1, 9, 7, 5, 2]
print(lst)  # Printing the list



# Convert the list to a set to remove duplicates and print it.
lst = [2, 5, 8, 6, 4, 3, 1, 9, 7, 5, 2]
print(set(lst))  # Converting the list to a set to remove duplicates



# Convert the list to a set, print the set, and then convert it back to a list and print it.
lst = [2, 5, 8, 6, 4, 3, 1, 9, 7, 5, 2]
a = set(lst)  # Converting the list to a set to remove duplicates
print(a)  # Printing the set
print(list(a))  # Converting the set back to a list and printing it



# Convert the list to a set and back to a list in one line, then print the list.
lst = [2, 5, 8, 6, 4, 3, 1, 9, 7, 5, 2]
print(list(set(lst)))  # Removing duplicates by converting to a set and back to a list

###################################################################################################
###################################################################################################

# Working with sets

# animals list
# Create a list of animals with duplicates, convert it to a set to get unique animals, and print the set and its length.
animals = ["cat", "dog", "cat", "elephant", "cat", "lion"]
print(set(animals))  # Converting the list to a set to get unique animals
print(len(set(animals)))  # Printing the number of unique animals


###################################################################################################
###################################################################################################


# Given a list of numbers, remove all odd numbers from the list.
# numbers list
numbers = [1, 1, 2, 3, 5, 8, 12, 20, 32, 5, 9, 11, 52, 90]

# Create an empty list, iterate through the numbers list, append even numbers to the empty list, and print the result.
empty_lst = []
for a in numbers:
    if (a % 2) == 0:  # Checking if the number is even
        empty_lst.append(a)  # Adding even numbers to the new list
print(empty_lst)  # Printing the list of even numbers


###################################################################################################
###################################################################################################


# Counting spaces in a string

# you have a text of a research paper now you need to find the count of spaces in that text
your_text = "You are best you are strong"

# Initialize a counter, iterate through the text, count the spaces, and print the result.
count = 0
for a in your_text:
    if a == " ":  # Checking if the character is a space
        count = count + 1  # Incrementing the counter for each space
print(count)  # Printing the total count of spaces



# Using an inbuilt function to count spaces in the text.
print(your_text.count(" "))  # Using the count() method to count spaces


###################################################################################################
###################################################################################################


# Finding occurrences of a number in a list

# you have a list of numbers and you need to find occurrences of 7:
numbers_list = [1, 7, 2, 3, 7, 8, 5, 7, 78, 45, 3, 23, 88, 7, 9]



# Initialize a counter, iterate through the list, count the occurrences of 7, and print the result.
count = 0
for a in numbers_list:
    if a == 7:  # Checking if the number is 7
        count = count + 1  # Incrementing the counter for each 7
print(count)  # Printing the total count of 7s



# Using a for loop to count 7s, considering 7 in 78 as well by converting the list to a string.
str_num = ''.join(map(str, numbers_list))  # Converting the list to a string
count = 0
for a in str_num:
    if a == '7':  # Checking if the character is '7'
        count = count + 1  # Incrementing the counter for each '7'
print(count)  # Printing the total count of '7's



# Using an inbuilt function to count occurrences of 7 in the string representation of the list.
numbers_list = [1, 7, 2, 3, 7, 8, 5, 7, 78, 45, 3, 23, 88, 7, 9]
str_num = ''.join(map(str, numbers_list))  # Converting the list to a string
print(str_num.count("7"))  # Using the count() method to count '7's
