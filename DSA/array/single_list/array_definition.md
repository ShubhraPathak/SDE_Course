# **Array or List**

Before we start to discuss Arrays, let us revise few points about memory allocation
in RAM.

--> For most of the programming languages an integer is stored in RAM with
4 bytes memory allocation (1 byte = 8 bits)

--> An array/list is stored in **contiguous memory location** with 4 bytes memory space each.

#### Example: stock price stored in an array from day1 to day n

stock_price = [298, 305, 320, 421, 311, 210]

memory allocation will look something like this in a stack---

| **Memory Stack** | **Stock Price value** | **Index** |
|------------------|-----------------------|-----------| 
| 0*00500          | 298                   | index 0   |
| 0*00504          | 305                   | index 1   |
| 0*00508          | 320                   | index 2   |
| 0*0050A          | 421                   | index 3   |
| 0*0050F          | 311                   | index 4   |
| 0*0050K          | 210                   | index 5   |

#### Note: When array stock_price is assigned, it will point to 0th memory location. ie stock_price -> stock_price[0]

## How we can access the value and how it works under hood?

### Case 1: Find price on day 3? Lookup by Index.

    simply pass the index value=>  stock_price[2] = 320
    
        Internal process
        stock_price[0] -> 0*00500
        stock_price[2] -> 0*00500 + 2 * size of integer -----> for int the size is 4 bytes
        stock_price[2] -> 0*00500 + 2 *4 = 0*00508
        price value at memory location 0*00508 --> 320.

    Lookup by Index, time complexity -> O(1)

### Case 2: Find index of 421 ? Lookup by value.

    A Simple for loop till we find the value at nth index.
    
    for i in range(len(stock_price)):
        if stock_price[i] == 421:
            return i
    
    Time complexity for Lookup by value in worst case -> O(n)

### Case 3: Print all stock price. Traversing through the list of length n.

    Array Traversal -> O(n)

### Case 4: list.insert new price at a given index.

    stock_price.insert(1, 201)
    The above memory stack will be changed to below table after insertion:
        

| **Memory Stack** | **Stock Price value** | **Index** |
|------------------|-----------------------|-----------| 
| 0*00500          | 298                   | index 0   |
| 0*00504          | 201                   | index 1   |
| 0*00508          | 305                   | index 1   |
| 0*0050A          | 320                   | index 2   |
| 0*0050F          | 421                   | index 3   |
| 0*0050K          | 311                   | index 4   |
| 0*0050P          | 210                   | index 5   |
    Post insertion, all other values shifts by 1 and their respective memory location changes.
    This says that Insert function has time complexity of -> O(n)

### Case 5: list.delete element at index 1.

    Similar to .insert function, .delete function also shifts the element by -1 and changes their prev memory location.
    Time complexity -> O(n)


### Note:
In Python List is implemented as DYNAMIC ARRAY. In java/cpp/c# etc we have STATIC and Dyanamic btoh.
[Detailed Explanation on array type](Array_Type.md)

### Important:
We can store all type of data in Python list (mixed data in one list, similar is not possible in other programming languages), also it is a difference between List and Tuple.


List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.


## Practice few questions:
question 1 --> A = [21, 32, 34, 54,88,67,89,97,100,32,41,521,37,67,97,88,20,202]
1. from list A find index of 67.
2. from list A find length of the list.
3. From list A find 9th element
4. From list A find max and min elements
5. from list A delete x element.
6. From list A find 2nd largest number.
7. From list A find element from 2nd to 5th and 5th to 12th index.
8. Find all numbers at odd and even index.

[Solutions](list_questionary.py)

Question 2--> 

Given two integer arrays A and B of size N. There are N gas stations along a circular route, where the amount of gas at station i is A[i].
You have a car with an unlimited gas tank and it costs B[i] of gas to travel from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.
Return the minimum starting gas station's index if you can travel around the circuit once, otherwise return -1.
You can only travel in one direction. i to i+1, i+2, ... n-1, 0, 1, 2.. Completing the circuit means starting at i and ending up at i again.

[Solution 2](list_solution2.py)

Question 3 -->

Given an array of size N, find the majority element. The majority element is the element that appears more than floor(N/2) times.
You may assume that the array is non-empty and the majority element always exist in the array.

    Example Input
    A = [2, 1, 2]
    Example Output
    2
    Example Explanation
    2 occurs 2 times which is greater than 3/2.

[Solution 3](list_solution2.py)

[Groot Groot check me](MaxMod.py)

[*Try yourself*](https://www.interviewbit.com/problems/remove-duplicates-from-sorted-array/)



