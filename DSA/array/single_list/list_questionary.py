def find_by_index(array: list, index: int):
    return array[index]  # Time Complexity of O(1)


def find_length_of_array(array: list):
    return len(array)  # Time Complexity of this in-build method is O(1)


def find_by_value(array: list, value: int):
    for i in range(len(array)):
        if array[i] == value:
            return i  # Time complexity O(n)

    # can also be written as:
    # return [i for i in range(len(array)) if array[i]==value]


def find_max_and_min(array: list):
    # we have 2 ways to obtain the max and min values. Here I've coded one method, second you need to try by yourself.
    return max(array), min(array)


def delete_element_by_value(array: list, value: int):
    return array.remove(value)


def find_second_largest_element(array: list):
    # there are multiple ways to obtain result, here in the question the value of second-largest element is asked
    # so in one way we can traverse through the array and find out and another way is to sort the list and find the
    # value of second-largest element.
    # please note that if the list contains Duplicates in such cases making a set is advisable.
    array.sort()
    return array[-2]


def find_sub_array_between_given_index(array: list, index_1: int, index_2: int):
    array_result = []
    for i in range(index_1, index_2 + 1):
        array_result.append(array[i])
    return array_result

    # there is one more way to achieve this:
    # return array[start_index:stop_index+1]


def find_all_even_and_odd_index_elem(array: list):
    all_even_index = array[::2]
    all_odd_index = array[1::2]
    return all_even_index, all_odd_index


if __name__ == '__main__':
    A = [21, 32, 34, 54, 88, 67, 89, 97, 100, 32, 41, 521, 37, 67, 97, 88, 20, 202]
    print(find_by_index(A, 6))
    print(find_length_of_array(A))
    print(find_by_value(A, 100))
    print(find_max_and_min(A))
    print(delete_element_by_value(A, 89))
    print(find_second_largest_element(A))
    print(find_sub_array_between_given_index(A, 3, 8))
    print(find_all_even_and_odd_index_elem(A))
