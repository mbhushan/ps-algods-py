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



