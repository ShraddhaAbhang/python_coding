# NOTE: Run this in a Interactive window for simplicity.

# Print numbers from 1 to 10 using a for loop.
for a in range(1, 11):
    print(a)

# Print numbers from 1 to 10 with an interval of 2 (e.g., 2, 4, 6).
# Start the range from 0 with a step of 2, but skip the first element (0).
for a in range(0, 11, 2):
    if a == 0:  # Skip the first element which is 0.
        continue
    print(a)

# Print numbers from 1 to 10 with an interval of 2 (e.g., 2, 4, 6).
# This method uses a counter variable to achieve the interval of 2.
counter = 0
for a in range(1, 10):
    if counter == 1:
        counter = 0  # Reset the counter after printing the next number.
        print(a+1)  # Print the next number in the sequence.
    elif a == 1:  # Print the first number in the sequence.
        print(a+1)
    else:
        counter += 1  # Increment the counter to control the interval.
