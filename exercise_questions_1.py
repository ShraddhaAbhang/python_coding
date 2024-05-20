"""
Task: Given a string of animal names, find the most popular animal. If the most popular animal is in the forbidden list,
ignore it and select the next most popular animal.

animals_string = "unicorn dog monkey unicorn lion elephant dog unicorn tiger elephant elephant monkey elephant elephant"
forbidden = "elephant"
"""

###################################################################################################

# Approach 1: Using dictionary for counting and sorting

# Initialize the animals string and the forbidden animal
animals_string = "unicorn dog monkey unicorn lion elephant dog unicorn tiger elephant elephant monkey elephant elephant"
forbidden = "elephant"

# Split the string into a list of animals
animals_list = animals_string.split()  # Converting the string into a list of animals

# Count the occurrences of each animal
animal_counts = {}
for animal in animals_list:
    if animal not in forbidden:  # Excluding the forbidden animal
        animal_counts[animal] = animal_counts.get(animal, 0) + 1  # Counting each animal

# Sort the animals by their counts in descending order
sorted_animals = sorted(animal_counts.items(), key=lambda x: x[1], reverse=True)  # Sorting animals by count

# Find the most popular animal that is not in the forbidden list
most_popular = None
for animal, count in sorted_animals:
    if animal != forbidden:
        most_popular = animal  # Selecting the most popular non-forbidden animal
        break

# Print the result
print("The most popular animal (excluding '{}') is: {}".format(forbidden, most_popular))


###################################################################################################

# Approach 2: Using while loop to remove forbidden animal

# Initialize the animals string and the forbidden animal
animals_string = "unicorn dog monkey unicorn lion elephant dog unicorn tiger elephant elephant monkey elephant elephant"
forbidden = "elephant"

# Split the string into a list of animals
animals_list = animals_string.split()  # Converting the string into a list of animals

# Remove forbidden animal from the list
while forbidden in animals_list:
    animals_list.remove(forbidden)  # Removing all instances of the forbidden animal

# Count occurrences of each animal
animal_counts = {}
for animal in animals_list:
    if animal in animal_counts:
        animal_counts[animal] += 1  # Incrementing the count for each animal
    else:
        animal_counts[animal] = 1  # Initializing the count for new animals

# Find the most popular animal
most_popular = None
for animal, count in animal_counts.items():
    if most_popular is None or count > animal_counts.get(most_popular, 0):
        most_popular = animal  # Selecting the most popular animal

# Print the result
print("The most popular animal (excluding '{}') is: {}".format(forbidden, most_popular))


###################################################################################################

# Approach 3: Using list comprehension and max function

# Initialize the animals string and the forbidden animal
animals_string = "unicorn dog monkey unicorn lion elephant dog unicorn tiger elephant elephant monkey elephant elephant"
forbidden = "elephant"

# Split the string into a list of animals and remove the forbidden animal using list comprehension
animals_list = animals_string.split()
animals_list = [animal for animal in animals_list if animal != forbidden]  # Removing forbidden animals

# Find the most popular animal using max function and set to count occurrences
most_popular = max(set(animals_list), key=animals_list.count)  # Finding the most frequent animal

# Print the result
print("The most popular animal (excluding '{}') is: {}".format(forbidden, most_popular))
print(f"The most popular animal (excluding '{forbidden}') is: {most_popular}")
