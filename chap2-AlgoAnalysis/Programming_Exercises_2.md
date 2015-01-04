## 2.7 Chapter-2 Programming Exercises - Algorithm Analysis
=====================================================================

##### 1. Devise an experiment to verify that the list index operator is O(1).
> Please refer to the file list_index.py  
> Approach: we create a list of size 1000000 and do 10K index access,  
> then we increase the size of list 1M at each step and continue with 10K index access.  
> As we can see in the list_index_input.txt the time remains constant (0.038751423 secs)  
> So we can conclude the access time does not depend on list length and is constant ie O(1)  


2. Devise an experiment to verify that get item and set item are O(1) for dictionaries.
3. Devise an experiment that compares the performance of the del operator on lists and
dictionaries.
4. Given a list of numbers in random order write a linear time algorithm to find the kth
smallest number in the list. Explain why your algorithm is linear.
5. Can you improve the algorithm from the previous problem to be O(n log(n))?
