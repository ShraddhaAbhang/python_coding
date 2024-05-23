

##############################################################################################
# Dictionary sorting
##############################################################################################

# lambda approach
# Dictionary to be sorted
my_dict = {'apple': 5, 'banana': 3, 'orange': 7, 'grape': 2}
# Sorting using lambda function
sorted_dict_lambda = dict(sorted(my_dict.items(), key=lambda x: x[1]))
print(sorted_dict_lambda)  # Output: {'grape': 2, 'banana': 3, 'apple': 5, 'orange': 7}


# core approach
# Dictionary to be sorted
my_dict = {'apple': 5, 'banana': 3, 'orange': 7, 'grape': 2}
# Sorting dictionary values manually without specific keywords
sorted_dict_items = []

# Sorting manually
while my_dict:
    min_key = None
    min_value = None
    for key, value in my_dict.items():
        if min_value is None or value < min_value:
            min_key = key
            min_value = value
    sorted_dict_items.append((min_key, min_value))
    del my_dict[min_key]

sorted_dict = {}
for item in sorted_dict_items:
    sorted_dict[item[0]] = item[1]

# instead of above for loop you can use this below line as well
# sorted_dict = dict(sorted_dict_items)
# remember this sorted dict items was a list with tuple in it as each element which made above line possible e.g: [('grape', 2), ('banana', 3), ('apple', 5), ('orange', 7)]

print(sorted_dict)  # Output: {'grape': 2, 'banana': 3, 'apple': 5, 'orange': 7}


##############################################################################################

# for reverse order
# Dictionary to be sorted

# Dictionary to be sorted
my_dict = {'apple': 5, 'banana': 3, 'orange': 7, 'grape': 2}

# Sorting using lambda function in reverse order
reverse_sorted_dict_lambda = dict(sorted(my_dict.items(), key=lambda x: x[1], reverse=True))

print(reverse_sorted_dict_lambda)  # Output: {'orange': 7, 'apple': 5, 'banana': 3, 'grape': 2}


##############################################################################################

# noraml approach
my_dict = {'apple': 5, 'banana': 3, 'orange': 7, 'grape': 2}

# Sorting dictionary values manually without specific keywords in reverse order
sorted_dict_items = []

# Sorting manually
while my_dict:
    max_key = None
    max_value = None
    for key, value in my_dict.items():
        if max_value is None or value > max_value:
            max_key = key
            max_value = value
    sorted_dict_items.append((max_key, max_value))
    del my_dict[max_key]

reverse_sorted_dict = dict(sorted_dict_items)

print(reverse_sorted_dict)  # Output: {'orange': 7, 'apple': 5, 'banana': 3, 'grape': 2}


##############################################################################################

# select first key value from dict
my_dict = {'apple': 5, 'banana': 3, 'orange': 7, 'grape': 2}
first_key, first_value = next(iter(my_dict.items()))
print("First key:", first_key)
print("First value:", first_value)


# normal approach
# Dictionary
my_dict = {'apple': 5, 'banana': 3, 'orange': 7, 'grape': 2}

# Selecting the first key-value pair
first_key = None
first_value = None
for key, value in my_dict.items():
    first_key = key
    first_value = value
    break  # Exit the loop after the first iteration

print("First key:", first_key)
print("First value:", first_value)