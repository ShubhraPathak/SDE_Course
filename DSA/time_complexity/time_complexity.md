# **Time Complexity:** How many steps a program is taking to provide the final output.
### Let us assume an array of length and we want to find nth element. there are 2 ways we can achieve it-
1. iterate though each element of the list and find nth element. we can obtain it by a simple 'for' loop.
        
        A = [4,9,12,21,43,67,98] # find 67
        for i in range(len(A)):
            if A[i] == 67: # in 6th iteration we will find 67, and in worst case it can take max upto len(A) iteration
                return i # the time complexity for given array will be O(len(A)) or O(n)
    * It will generate a linear function of 'n' as time will increase with size of the list of 'n'.

            Time constant K = an + b # Mathematical representation of linear equation.
        * 2 rules to be followed t find out Time complexity-
          * Consider only bigger values --> if n >=10000, so an>>>b, drop 'b' 
            * Drop any constant --> a is constant and much smaller than n, hence drop constant.
            
                  Time constant K = n or Time Complexity = O(n)
            
          
2. The linear search process is dependant of length of the array and for bigger values the time complexity will be high.
    We can optimise the solution by using 'binary search'. Let's find the index of nth element by using Binary search.

        A = [4,9,12,21,43,67,98] # find 67
        A = [4,9,12,21,43,67,98] # iteration 1 = n/2 as 21 is the middle element and 67>21 so we leave the left part.
        A = [_,_,__,__,43,67,98] # interation 2 = n(1/2 * 1/2) = n/4 ans = 67 found

        Similarly for kth iterations the complexity will be = n/(2**k)
        K = n/2**k or it can also be written as K*2**k = n 
        Assuming 'K' as constant and droping it and taking log both side with base 2
        log 2**k = log n => k log2 = log n => k = log n
        or Time complexity of binary search = O(log n) => faster than linear search.

Question to ask: If Binary search is faster than linear search then why it is used less frequently?

[Solution](search_complexity.py) 

[Know More](linear_vs_binary_search.md)

_[Questionary](linear_vs_binary_search.md)_
