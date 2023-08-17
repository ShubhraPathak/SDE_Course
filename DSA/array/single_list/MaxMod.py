# Given an array A of size N, Groot wants you to pick 2 indices i and j such that
# 1 <= i, j <= N
# A[i] % A[j] is maximum among all possible pairs of (i, j).
# Help Groot in finding the maximum value of A[i] % A[j] for some i, j.

# Note: Array can have duplicates as well.

def max_mod(array):
    # Duplicates are handled.
    if not array:  # Handle empty list
        return
    set_of_array = list(set(array))  # By creating a set we are only considering distinct value

    max_of_array = max(set_of_array)
    set_of_array.remove(max_of_array)
    # If the array only consist of duplicates in such case the set_of_array will be of length 1
    # Post deletion of max value from the array it will become a empty list. Handling that corner case.
    if set_of_array:
        second_max = max(set_of_array)
    else:
        second_max = 0
    return second_max % max_of_array


if __name__ == '__main__':
    print(max_mod([1, 2, 3, 1, 21, 31, 22, 41, 11]))
    print(max_mod([5, 5, 5, 5, 5, 5, 5]))
    print(max_mod(
        [78, 54, 21, 2345, 543212, 121, 232, 1, 34, 1, 3, 2, 11223, 22, 33, 1, 3, 344, 1, 3, 4, 2, 2, 34, 45, 5, 4, 2]))
    print(max_mod([]))
