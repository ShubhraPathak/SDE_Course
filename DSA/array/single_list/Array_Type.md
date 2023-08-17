| Static Array                                                                                                                       | Dynamic Array                                                                                                                                                                                                                                                                                     |
|------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Fix size of memory provided while initialization. <br/> eg: for int[5] Contiguous 5 memory location will be assigned to the array. | No fix size, it can dynamically grow.<br/> eg: ArrayList<integer>(); Initially some x capacity is allocated in contiguous memory stack.                                                                                                                                                           |
| We can not insert more elements once the max size is reached. --> Index error.                                                     | Once the initial allotted memory is filled with element and we want to insert more values to the ArrayList, the system will dynamically allot new memory location with x + 2x capacity.<br/> Also the 'x' values stored at previous location will be copied to new location with extra 2x memory. |

| Static Array memory stack |
|---------------------------|
| int[0]                    |
| int[1]                    |
| .                         |
| .                         |
| .                         |
| int[5]                    |


| Dynamic Array memory Stack    |
|-------------------------------|
| //////////////////////////    |
| /////////////////////////     |
| memory stack above allocation |
| start index 0                 |
| .                             |
| .                             |
| .                             |
| end index 'x'                 |
| memory stack below allocation |
| /////////////////////////     |
| /////////////////////////     |
| /////////////////////////     |
