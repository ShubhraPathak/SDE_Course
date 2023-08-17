
def can_complete_circuit(A, B):
    start_index = 0
    tank_fuel = 0
    way_back = 0
    i = 0
    while i < len(A):
        tank_fuel += A[i] - B[i]  # if B[i] is greater we can not reach to next station
        i += 1
        if tank_fuel < 0:
            start_index = i
            way_back += tank_fuel
            tank_fuel = 0

    return start_index if way_back + tank_fuel >= 0 else -1


def majority_element(array):
    d = len(array) / 2
    b_ = []
    for i in array:
        if i not in b_:
            count_i = array.count(i)
            if count_i > d:
                return i


if __name__ == '__main__':
    A = [1,3, 4, 2]
    B = [4, 2, 3, 1, 1]
    val = can_complete_circuit(A, B)
    print(val)
    array = [1,2,3,4,2,2,3,2,4,2,2,2]
    print("majority element is:", majority_element(array))
