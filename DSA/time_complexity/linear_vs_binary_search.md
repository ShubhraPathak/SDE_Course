## Basic differance between Linear Search and Binary Search.

| **Linear Search**                                     | **Binary Search**                                       |                                
|-------------------------------------------------------|---------------------------------------------------------|
| In linear search input data need not to be in sorted. | In binary search input data need to be in sorted order. |
| It is also called sequential search.                  | It is also called half-interval search.                 |
| The time complexity of linear search O(n).            | The time complexity of binary search O(log n).          |          
| Multidimensional array can be used.	                  | Only single dimensional array is used.                  |            
| Linear search performs equality comparisons	          | Binary search performs ordering comparisons             |           
| It is less complex.	                                  | It is more complex.                                     |          
| It is very slow process.                              | It is very fast process.                                |      


## Practice Questions --
1. What is the time, and space complexity of the following code: 

        a = 0
        b = 0
        for i in range(N):
            a = a + random()
 
        for i in range(M):
            b= b + random()
         
         Ans: O(N+M) and space complexity O(1)

2. What is the time, and space complexity of the following code:

         a = 0;
         for i in range(N):
            for j in reversed(range(i,N)):
               a = a + i + j;

         Ans: O(N*N) 
   The above code runs total no of times 

   = N + (N – 1) + (N – 2) + … 1 + 0 

   = N * (N + 1) / 2 

   = 1/2 * N^2 + 1/2 * N 

   O(N^2) times.

3. What is the time complexity of the following code: 


         k = 0;
         for i in range(n//2,n):
           for j in range(2,n,pow(2,j)):
               k = k + n / 2;

         Ans: O(nlogn)

   Explanation: If you notice, j keeps doubling till it is less than or equal to n. Several times, we can double a number till it is less than n would be log(n). 
   Let’s take the examples here. 

   for n = 16, j = 2, 4, 8, 16 
   for n = 32, j = 2, 4, 8, 16, 32 

   So, j would run for O(log n) steps. 

   i runs for n/2 steps. 

   So, total steps = O(n/ 2 * log (n)) = O(n*logn)

4. Time complexity for below code

         for i in range(n):
            i=i*k
         
         Ans: O(logkn)

Explanation: Because the loop will run kc-1 times, where c is the number of times
i can be multiplied by k before i reaches n. Hence, kc-1=n. Now to find the value of c we can apply log and it becomes logkn.

