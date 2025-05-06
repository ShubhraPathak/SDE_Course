import sys
# given an unsorted array a = [12, 321, 2, -1, 0, -4, 60, 18, 564]
# find 3 largest number from the array a.
# note- Do not use build in methods or sort the array or manipulate it by adding or removing the array.

# By using build in methods-
def find_3_largest_elemnt(A):
    first_largest = max(A)
    A.remove(first_largest)
    second_largest = max(A) if A else 0
    A.remove(second_largest) if A and second_largest else A
    third_largest = max(A) if A else 0
    return [first_largest, second_largest, third_largest]

# Implementing it without using build in methods
def find_3_largest_element_without_buildin(A):
    # intialize first, second, third
    # iterate through each element of the array
    # if (i > first) {third = second, second = first, first = x}
    # if (i > second and i != first) {third = second, second = x}
    # if (i > third and i != second) {third = i}
    if len(A) < 3:
        return "invalid input"
    first = second = third = -sys.maxsize
    for i in range(0, len(A)):
        if (A[i] > first):
            third = second
            second = first
            first = A[i]
        elif (A[i] > second):
            third = second
            second = A[i]
        elif (A[i] > third):
            third = A[i]
        
    return [first, second, third]


if __name__ == "__main__":
    A = [1,23,-9,0,99,87,61,-89,198]
    print(find_3_largest_elemnt(A))
    A = [1,23,-9,0,99,87,61,-89,198]
    print(find_3_largest_element_without_buildin(A))