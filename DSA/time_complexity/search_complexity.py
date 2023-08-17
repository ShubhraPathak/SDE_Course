A = [5, 3, 42, 124, 56, 43, 57, 8, 95, 31, 2, 34, 15, 6, 55]  # find index of 31


# linear search
def linear_search(a, target):
    for i in range(len(a)):
        if a[i] == target:
            return i
    return 'index not found'


def binary_search(a, target):
    """
    In a binary search, however, cut down your search to half as soon as you find the middle of a sorted list.
    The middle element is looked at to check if it is greater than or less than the value to be searched.
    Accordingly, a search is done to either half of the given list
    :param a:
    :param target:
    :return:
    """
    a.sort()  # sort if not already sorted (it will change the index of target, drawback) requires a sorted list only
    low = 0
    high = len(a)
    print(low, high, a)

    # Repeat until the pointers low and high meet each other
    while low <= high:

        mid = low + (high - low) // 2

        if a[mid] == target:
            return mid

        elif a[mid] < target:
            low = mid + 1

        else:
            high = mid - 1

    return -1


if __name__ == '__main__':
    ans = linear_search(A, target=31)
    print(ans)

    bin_search = binary_search(A, target=31)
    print(bin_search)

