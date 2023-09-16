# Question: Given a roman numeral, convert it to an integer.
# Constrain :
# 1 <= s.length <= 15
# s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
# It is guaranteed that s is a valid roman numeral in the range [1, 3999].

def roman_to_int(string:str):
    map_roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D':500, 'M': 1000}
    n = len(string)
    roman_int = 0

    # Forward tracking
    for i in range(n):
        if i < n-1 and map_roman.get(string[i]) < map_roman.get(string[i+1]):
            roman_int -= map_roman.get(string[i])
        else:
            roman_int += map_roman.get(string[i])
    print(roman_int, "Method 1")

    # Back tracking
    roman_int = map_roman.get(string[n-1]) # last value of the string
    # range will start from second last value
    for i in range(n-2, -1, -1):
        if map_roman.get(string[i]) < map_roman.get(string[i+1]):
            roman_int -= map_roman.get(string[i])
        else:
            roman_int += map_roman.get(string[i])
    print(roman_int, "Method 2")

# Question : Given an integer, convert it to a roman numeral.
# Constrains : 1 <= num <= 3999
# I can be placed before V (5) and X (10) to make 4 and 9.
# X can be placed before L (50) and C (100) to make 40 and 90.
# C can be placed before D (500) and M (1000) to make 400 and 900.


def int_to_roman(num: int):
    # Method 1
    int_nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    roman_syms = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']

    i = 0
    roman_number = ''
    while num:
        if num >= int_nums[i]:
            roman_number = roman_number + num//int_nums[i] * roman_syms[i]
            num = num % int_nums[i]
        i += 1
    print(roman_number)

    # Method 2
    roman_numerals = {
        1000: "M",
        900: "CM",
        500: "D",
        400: "CD",
        100: "C",
        90: "XC",
        50: "L",
        40: "XL",
        10: "X",
        9: "IX",
        5: "V",
        4: "IV",
        1: "I"
    }
    roman_number = ''
    for val, sym in roman_numerals.items():
        if num >= val:
            roman_number = roman_number + num//val * sym
            num %= val
    print(roman_number)



if __name__ == "__main__":
    roman_to_int('MMCMV')
    roman_to_int('MMCMDV')
    roman_to_int('MMMCDV')
    int_to_roman(5)
    int_to_roman(2905)
    int_to_roman(3405)