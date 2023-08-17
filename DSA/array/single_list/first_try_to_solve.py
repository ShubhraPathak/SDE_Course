# Given a sorted array A consisting of duplicate elements.
# Your task is to remove all the duplicates and
# return the length of the sorted array of distinct elements consisting of all distinct elements present in A.
# Note: You need to update the elements of array A by removing all the duplicates


def remove_duplicates(array):
    # The ask in the question is to return Length of the SORTED ARRAY OF DISTINCT ELEMENTS.
    # Also, the original array needs to be updated with DISTINCT ELEMENTS
    distinct_set = set(array)  # --> set of DISTINCT ELEMENTS
    array_of_distinct_ele = list(distinct_set)  # --> ARRAY OF DISTINCT ELEMENTS
    array_of_distinct_ele.sort()  # --> SORTED ARRAY OF DISTINCT ELEMENTS
    for i in range(len(array_of_distinct_ele)):
        array[i] = array_of_distinct_ele[i]  # --> Updating array A with DISTINCT ELEMENTS
    return len(array_of_distinct_ele)  # --> return the length of sorted array not the updated array.

    # here only set(A) will not work as the unit test module checks the updated array as well.


if __name__ == '__main__':
    array = [21, 3, 2, 12, 11, 21, 23, 4, 54, 32, 67, 89, 45, 24, 21, 54, 36, 43, 21, 26]
    print(remove_duplicates(array))
