# Linked List
-> There are some issues with Arrays/List, which linked list tries to solve.

-> we have seen and discussed the behaviour of Dynamic list on element insertion or deletion.

-> In simple words Arrays/list lacks in memory allocation and utilization, due to this time complexity increases.

### How Linked List and Doubly linked list over-come this issue?
Before we start please recollect the memory allocation/insertion/deletion operation in list. [here](../single_list/array_definition.md)

### How data is stored in Linked list: 
* Linked list stores data at random memory locations and each element (called as node) has a pointer for its next element.
* Whereas in Array/list the elements are store as contiguous memory location and list pointer is at 0th index.

Stock_price = [298, 302, 942, 201]

| **Memory Stack** | **Stock Price value** | **Next Node Information** |
|------------------|-----------------------|---------------------------| 
| 0*00500          | 298                   | 0*00A1                    |
| 0*00A1           | 302                   | 0*00D5                    |
| 0*00D5           | 942                   | 0*00C2                    |
| 0*00C2           | 201                   | null                      |

As we can see element 1 has the reference of the next element in row and so on.

### Let's see how Linked list offer better optimization over Array while insertion or deletion or say increasing size of array.
Now if we want to insert/delete an element from the given linked list, we just need to modify the reference of its previous node.
Hence, Time complexity on insertion/deletion become **O(1)**

-> Please node that we need to modify the reference of its previous node.

Example: Insert 284 at location 1.


| **Memory Stack** | **Stock Price value** | **Next Node Information** |
|------------------|-----------------------|---------------------------| 
| 0*00500          | 298                   | 0*00B1                    |
| 0*00B1           | 284                   | 0*00A1                    |
| 0*00A1           | 302                   | 0*00D5                    |
| 0*00D5           | 942                   | 0*00C2                    |
| 0*00C2           | 201                   | null                      |

As can be seen the 'Next node information' present at index 0 has been changed to new Node memory stack location. And other memory 
location and their reference remains the same.

### **Case 1 : Insert at beginning** --> O(1)

### **Case 2 : Delete at beginning** --> O(1)

### **Case 3 : Insert/Delete at end** --> O(n)

### **Case 4 : Linked list Traversal** --> O(n)

### **Case 5 : Accessing element by value** --> O(n)

### Two Main benefit of linked list / Double linked list:
* No need to pre-allocate the space
*  Insertion is easier


[Linked-List-Structure](linked_list_structure.py)

## Questionary on Linked list:---
1. Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example: 

`Input: head = [1,2,3,4,5], n = 2`

`Output: [1,2,3,5]`


[Solution](linkedlist_practice_questions.py) 

2. Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

Example:

`Input: head = [1,1,2]`

`Output: [1,2]`

[Solution](linkedlist_practice_questions.py)

3. Find the middle of the given linked list.

[Two pointer solution explanation](2pointer_solution_for_linked_list.png) 

[Solution](linkedlist_practice_questions.py)

4. Find if the linked list is circular.
Note: An empty linked is considered as circular linked list. A linked list will be circular if it is not NULL-terminated
 and iterator reaches its head again.

[Solution](linkedlist_practice_questions.py)

5. count node of a given circular linked list

[Solution](linkedlist_practice_questions.py)

6. Exchange tail to head in a circular linked list.

[Solution](linkedlist_practice_questions.py)

7. Reverse a linked list

##### Different Approaches:

* 3 pointer iteration method
* Recursion method
* Stack method