# Selection Sort Program

"""
Time Complexity
O(n**2) - n square

Space Complexity
O(1)
"""


# Input list
arr = [64, 25, 12, 22, 11]

n = len(arr)

# Traverse through all array elements
for i in range(n):

    # Assume current index has minimum value
    min_index = i

    # Find minimum element in remaining array
    for j in range(i + 1, n):

        if arr[j] < arr[min_index]:
            min_index = j

    # Swap minimum element with current element
    arr[i], arr[min_index] = arr[min_index], arr[i]

# Print sorted array
print("Sorted Array:")
print(arr)