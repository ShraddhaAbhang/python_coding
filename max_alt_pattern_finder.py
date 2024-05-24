
# Find the length of the longest alternating pattern in the sequence:

# Given the list [1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1], 
# Determine the length of the longest subsequence where each element alternates between 1 and 0.
# Input list a = [1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1]  

# Approach 1:- Best Approach

max_length = 1  # Initialize the maximum length of the alternating pattern
current_length = 1  # Initialize the current length of the alternating pattern

for i in range(1, len(a)):
    cur_ele = a[i]  # Current element
    pre_ele = a[i-1]  # Previous element
    if pre_ele != cur_ele:
        # If the current element is different from the previous one, it's alternating
        current_length += 1  # Increment the current alternating pattern length
        max_length = max(max_length, current_length)  # Update the maximum length if the current is longer
    else:
        # If the current element is the same as the previous one, reset the current length
        current_length = 1

print("The length of the longest alternating pattern is:", max_length)


#######################################################################################################################

# Approach 2

a = [1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1]  # Input list
b = [True]  # Initialize list b to store alternating pattern comparison results

for i in range(1, len(a)):
    # Iterate through the list starting from the second element (index 1)
    cur_ele = a[i]  # Current element
    print(cur_ele)
    pre_ele = a[i-1]  # Previous element
    comparison = pre_ele != cur_ele  # Check if the current element is different from the previous element
    if comparison == True:
        # If the elements are alternating, append True to list b
        b.append(comparison)
        cure_len = len(b)  # Calculate the current length of the alternating pattern
        print("current length", cure_len) 
    else:
        # If the elements are not alternating, print the current list b and its length
        print("list_b", b)
        cure_len = len(b)
        print("current length", cure_len)
        # Reset list b to start a new alternating pattern
        b = [True]
        print("---------")

print(cur_ele)  # Print the last element in the list
print(b)  # Print the final list b

