# Dictionary

# Create a dictionary with student names and their marks, then print Sa's marks.
marks_dict = {"sa": 100, "sh": 100}
print(marks_dict["sa"])  # Accessing the value associated with the key 'sa'

# Create the dictionary again and print all the keys in the dictionary.
marks_dict = {"sa": 100, "sh": 100}
print(marks_dict.keys())  # Retrieving all the keys from the dictionary 

# Create the dictionary again and print all the values in the dictionary.
marks_dict = {"sa": 100, "sh": 100}
print(marks_dict.values())  # Retrieving all the values from the dictionary

# Iterate through the dictionary and print each value followed by its key.
for i in marks_dict:
    print(marks_dict[i])  # Printing the value associated with the current key
    print(i)  # Printing the current key

### Inserting into a dictionary

# Iterate through the dictionary and print each key-value pair.
for key, value in marks_dict.items():
    print(key, value)  # Printing the current key and its associated value

# Create a dictionary with favorite fruits and their prices, then add a new fruit.
fav_fruits = {"mango": 450, "apple": 250, "banana": 40, "kiwi": 200, "orange": 120}
fav_fruits["stawberry"] = 400  # Adding a new key-value pair to the dictionary
print(fav_fruits)

## Inserting/updating multiple key-value pairs into the existing dictionary

# Update the dictionary by changing the price of apple and adding new fruits.
fav_fruits = {'mango': 450, 'apple': 250, 'banana': 40, 'kiwi': 200, 'orange': 120, 'stawberry': 400}
fav_fruits.update({'apple': 150, 'watermelon': 100, 'pipeapple': 80})  # Updating and adding key-value pairs
print(fav_fruits)

##

# Get the price of mango from the dictionary.
fav_fruits = {'mango': 450, 'apple': 250, 'banana': 40, 'kiwi': 200, 'orange': 120, 'stawberry': 400}
print(fav_fruits.get('mango'))  # Using the get() method to retrieve the value associated with the key 'mango'

##

# Remove apple from the dictionary using pop() and print the updated dictionary.
fav_fruits = {'mango': 450, 'apple': 250, 'banana': 40, 'kiwi': 200, 'orange': 120, 'stawberry': 400}
a = fav_fruits.pop('apple')  # Removing the key 'apple' and storing its value in variable 'a'
print(fav_fruits)  # Printing the updated dictionary after removal

##

# Remove the last inserted key-value pair using popitem() and print the updated dictionary.
fav_fruits = {'mango': 450, 'apple': 250, 'banana': 40, 'kiwi': 200, 'orange': 120, 'stawberry': 400}
a = fav_fruits.popitem()  # Removing the last inserted key-value pair and storing it in variable 'a'
print(fav_fruits)  # Printing the updated dictionary after removal

##

# Delete the entry for 'orange' from the dictionary.
fav_fruits = {'mango': 450, 'apple': 250, 'banana': 40, 'kiwi': 200, 'orange': 120, 'stawberry': 400}
del fav_fruits['orange']  # Deleting the key 'orange' from the dictionary
print(fav_fruits)  # Printing the updated dictionary after deletion

##

# Clear all entries from the dictionary.
fav_fruits = {'mango': 450, 'apple': 250, 'banana': 40, 'kiwi': 200, 'orange': 120, 'stawberry': 400}
fav_fruits.clear()  # Removing all key-value pairs from the dictionary
print(fav_fruits)  # Printing the empty dictionary

##

# Check if 'kiwi' exists in the dictionary and print the result.
fav_fruits = {'mango': 450, 'apple': 250, 'banana': 40, 'kiwi': 200, 'orange': 120, 'stawberry': 400}
if "kiwi" in fav_fruits:
    print("Kiwi exists in the given dictionary.")  # Message if 'kiwi' is a key in the dictionary
else:
    print("Kiwi does not exist in the given dictionary.")  # Message if 'kiwi' is not a key in the dictionary

##

# Merge two dictionaries.
dic_1 = {'mango': 450, 'apple': 250}
dict_2 = {'banana': 40, 'kiwi': 200, 'orange': 120, 'stawberry': 400}
dict_2.update(dic_1)  # Merging dic_1 into dict_2
print(dict_2)  # Printing the updated dictionary after merging

##

# Create a dictionary comprehension that maps numbers from 0 to 29 to their cubes.
a = {x: x**3 for x in range(30)}  # Dictionary comprehension to generate a dictionary of cubes
print(a)  # Printing the resulting dictionary
