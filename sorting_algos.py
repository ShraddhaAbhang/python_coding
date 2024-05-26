#---------------------SORTING---------------------#

# Binary Search

def binary_search(arr, target):
    # Binary search works on a sorted array by repeatedly dividing the search interval in half.
    # Time complexity: O(log n)
    # Space complexity: O(1)
    # Use case: Efficiently finding an element in a sorted array.

    left, right = 0, len(arr) - 1  # Initialize left and right pointers

    while left <= right:  # Loop until the pointers meet
        mid = (left + right) // 2  # Find the middle element

        if arr[mid] == target:  # Check if the middle element is the target
            return mid  # Target found, return its index
        elif arr[mid] < target:  # If target is greater, ignore left half
            left = mid + 1
        else:  # If target is smaller, ignore right half
            right = mid - 1

    return -1  # Target not found, return -1

def binary_search_main():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    target = 5
    result = binary_search(arr, target)
    if result != -1:
        print(f"Element found at index {result}")
    else:
        print("Element not found")



# Bubble Sort

def bubble_sort(arr):
    # Bubble sort repeatedly swaps adjacent elements if they are in the wrong order.
    # Time complexity: O(n^2)
    # Space complexity: O(1)
    # Use case: Simple implementation, but inefficient for large datasets.

    n = len(arr)  # Get the number of elements in the array

    for i in range(n):  # Traverse through all array elements
        for j in range(0, n-i-1):  # Last i elements are already sorted
            if arr[j] > arr[j+1]:  # Swap if the element found is greater than the next element
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

def bubble_sort_main():
    arr = [64, 34, 25, 12, 22, 11, 90]
    sorted_arr = bubble_sort(arr)
    print("Sorted array is:", sorted_arr)



# Selection Sort

def selection_sort(arr):
    # Selection sort repeatedly finds the minimum element and moves it to the sorted part of the array.
    # Time complexity: O(n^2)
    # Space complexity: O(1)
    # Use case: Simple implementation, performs well on small lists.

    n = len(arr)  # Get the number of elements in the array

    for i in range(n):  # Traverse through all array elements
        min_idx = i  # Assume the current element is the minimum
        for j in range(i+1, n):  # Find the minimum element in remaining unsorted array
            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]  # Swap the found minimum element with the first element

    return arr

def selection_sort_main():
    arr = [64, 25, 12, 22, 11]
    sorted_arr = selection_sort(arr)
    print("Sorted array is:", sorted_arr)



# Insertion Sort

def insertion_sort(arr):
    # Insertion sort builds the sorted array one item at a time.
    # Time complexity: O(n^2)
    # Space complexity: O(1)
    # Use case: Efficient for small or partially sorted arrays.

    n = len(arr)  # Get the number of elements in the array

    for i in range(1, n):  # Traverse through 1 to len(arr)
        key = arr[i]  # Select the current element to be inserted
        j = i - 1

        while j >= 0 and key < arr[j]:  # Move elements of arr[0..i-1], that are greater than key, to one position ahead
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key  # Place the key at after the element just smaller than it

    return arr

def insertion_sort_main():
    arr = [12, 11, 13, 5, 6]
    sorted_arr = insertion_sort(arr)
    print("Sorted array is:", sorted_arr)



# Quicksort

def partition(arr, low, high):
    # Partition function for quicksort
    # Time complexity: O(n)
    # Space complexity: O(1)

    pivot = arr[high]  # Pivot element
    i = low - 1  # Index of smaller element

    for j in range(low, high):  # Traverse through all elements
        if arr[j] <= pivot:  # If current element is smaller than or equal to pivot
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]  # Swap elements

    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # Swap the pivot element with the element at i+1
    return i + 1

def quicksort(arr, low, high):
    # Quicksort is a divide-and-conquer algorithm. It picks an element as pivot and partitions the array around the pivot.
    # Time complexity: O(n log n) on average, O(n^2) in the worst case
    # Space complexity: O(log n)
    # Use case: Efficient for large datasets, widely used in practice.

    if low < high:
        pi = partition(arr, low, high)  # Partitioning index

        quicksort(arr, low, pi - 1)  # Recursively sort elements before partition
        quicksort(arr, pi + 1, high)  # Recursively sort elements after partition

    return arr

def quicksort_main():
    arr = [10, 7, 8, 9, 1, 5]
    sorted_arr = quicksort(arr, 0, len(arr) - 1)
    print("Sorted array is:", sorted_arr)

# Main function to test all algorithms

if __name__ == "__main__":
    print("Binary Search")
    binary_search_main()

    print("\nBubble Sort")
    bubble_sort_main()

    print("\nSelection Sort")
    selection_sort_main()

    print("\nInsertion Sort")
    insertion_sort_main()

    print("\nQuicksort")
    quicksort_main()
