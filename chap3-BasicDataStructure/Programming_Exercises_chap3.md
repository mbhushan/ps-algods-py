## Programming Exercises - Chapter-3: Basic Data Structures
=====================================================================

##### 1. Modify the infix-to-postfix algorithm so that it can handle errors.
> Please refer to InfixToPostfix.py - very generic question - I have added basic error checking.  

##### 2. Modify the postfix evaluation algorithm so that it can handle errors.
> Please refer to PostfixEval.py - Though there are basic error handling checks - see if you can extend it.  

##### 3. Implement a direct infix evaluator that combines the functionality of infix-to-postfix conversion and the postfix evaluation algorithm. Your evaluator should process infix tokens from left to right and use two stacks, one for operators and one for operands, to perform the evaluation.
> Please refer to InfixCalc.py for implementation and InfixCalc_inout.txt for sample input/output.  

##### 4. Turn your direct infix evaluator from the previous problem into a calculator. 
> Please refer to Calculator.py, Tokenizer.py and Calculator_inout.py for implementation, and sample input/output.  

##### 5. Implement the Queue ADT, using a list such that the rear of the queue is at the end of the list.  
> Refer to QueueADT.py and QueueADTClient.py for implementation and sample input/output  

##### 6. Design and implement an experiment to do benchmark comparisons of the two queue implementations. What can you learn from such an experiment?
> Refer to QueueADTClient.py and QueueADTClient_inout.txt. we learn that with List implementation one of the enqueue/dequeue operation would be O(n) and if we need both enqueue/dequeue operation be O(1) then we need to resort to linked list implementation of Queue.

##### 7. It is possible to implement a queue such that both enqueue and dequeue have O(1) performance on average. In this case it means that most of the time enqueue and dequeue will be O(1) except in one particular circumstance where dequeue will be O(n).
> Please refer to QueueLinkedList.py and QueueLinkedListClient.py for the linked list implementation of Queue. Here both enqueue and dequeue operations are O(1) 

##### 9. Modify the Hot Potato simulation to allow for a randomly chosen counting value so that each pass is not predictable from the previous one.
> Please refer to HotPotatoRand.py for implementation and HotPotatoRand_inout.txt for input/output examples

##### 10. Implement a radix sorting machine. A radix sort for base 10 integers is a mechanical sorting technique that utilizes a collection of bins, one main bin and 10 digit bins. Each bin acts like a queue and maintains its values in the order that they arrive. The algorithm begins by placing each number in the main bin. Then it considers each value digit by digit. The first value is removed and placed in a digit bin corresponding to the digit being considered. For example, if the ones digit is being considered, 534 is placed in digit bin 4 and 667 is placed in digit bin 7. Once all the values are placed in the corresponding digit bins, the values are collected from bin 0 to bin 9 and placed back in the main bin. The process continues with the tens digit, the hundreds, and so on. After the last digit is processed, the main bin contains the values in order. 
> Refer to RadixSort.py for implementation and RadixSort_inout.txt for sample input/output.

##### 11. Another example of the parentheses matching problem comes from hypertext markup language (HTML). In HTML, tags exist in both opening and closing forms and must be balanced to properly describe a web document. This very simple HTML document:  
``` html
<html>
<head>
<title>
Example
</title>
</head>
<body>
<h1>Hello, world</h1>
</body>
</html>
```
is intended only to show the matching and nesting structure for tags in the language. Write a program that can check an HTML document for proper opening and closing tags. 
> Please refer to HTMLTagValidator.py for implementation and HTMLTagValidator_inout.txt for sample input/output.

##### 12. To implement the length method, we counted the number of nodes in the list. An alter- native strategy would be to store the number of nodes in the list as an additional piece of data in the head of the list. Modify the UnorderedList class to include this information and rewrite the length method. 
> Please refer to LinkedList.py for unordered link list implementation and LinkedListClient.py for testing the main class LinkedList.py

##### 13. Implement the remove method so that it works correctly in the case where the item is not in the list.
> refer to remove method in LinkedList.py and LinkedListClient.py testing methods.

##### 14. Modify the list classes to allow duplicates. Which methods will be impacted by this change?
##### 15. Implement the \'__str__\' method in the UnorderedList class. What would be a good string representation for a list?
##### 16. Implement \'__str__\' method so that lists are displayed the Python way (with square brackets).
> LinkedList.py has \'__str__\' method which represents(prints) the LinkedList like python lists and LinkedList.py allows for duplicates nodes as well - remove method deletes the first first occurance of the data from head if found.

##### 17. Implement the remaining operations defined in the UnorderedList ADT (append, index, pop, insert).
> Refer to SLList.py for implementation of append, index, pop and insert. Test client code is written in SLListClient.py

##### 18. Implement a slice method for the UnorderedList class. It should take two parameters, start and stop, and return a copy of the list starting at the start position and going up to but not including the stop position. 
> Please refer the slice(start, stop) method in SLList.py - testing method has been added in SLListClient.py

##### 19. Implement the remaining operations defined in the OrderedList ADT.
> Please refer to OrderedList.py for operations implementation and OrderedListClient.py for testing OrderedList.py class

##### 20. Implement a stack using linked lists.
> Please refer to StackLinkedList.py for implementation and StackLinkedListClient.py for test client code.

##### 21. Implement a queue using linked lists.
> Please refer to QueueLinkedList.py for implementation and QueueLinkedListClient.py for test client code. 

##### 22. Implement a deque using linked lists.
> Please refer to DequeLinkedList.py for Deque implementation and DequeLinkedListClient.py for client test code

###### 23. Design and implement an experiment that will compare the performance of a Python list with a list implemented as a linked list.
> Approach: List in python has array implementation - what this means is elements of list are stored in contiguous memory locations. So operations like index(), search()(binary search - if data is sorted), sort() can be really efficient. Cons here is when the list is full and we need to add more data to it, python has to copy the old list to a bigger contiguous space, similarly when we have removed a lot of elements from the list we need to resize() it to smaller size - this again requires copy to smaller contiguous memory locations. Experimentation is left as an exercise to user :)

###### 24. Design and implement an experiment that will compare the performance of the Python list based stack and queue with the linked list implementation.
> In Contrast Linked List implementation works really well when we need to add elements as we never have to copy the whole list (unlike List in python), or when we need to remove lot of elements from the linked list - This implementation ensures optimal usage of memory. Though there are associated overheads of maintaining pointers. Indexing and Search (BinarySearch) can be challenging and deteriorate performance when implemented in linked list. Experimentation is left as an exercise :)

##### 25. The linked list implementation given above is called a singly linked list because each node has a single reference to the next node in sequence. An alternative implementation is known as a doubly linked list. In this implementation, each node has a reference to the next node (commonly called next) as well as a reference to the preceding node (commonly called back). The head reference also contains two references, one to the first node in the linked list and one to the last. Code this implementation in Python. 
