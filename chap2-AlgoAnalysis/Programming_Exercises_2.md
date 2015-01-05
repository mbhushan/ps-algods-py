## 2.7 Chapter-2 Programming Exercises - Algorithm Analysis
=====================================================================

##### 1. Devise an experiment to verify that the list index operator is O(1).
> Please refer to the file list_index.py  
> **Approach** : we create a list of size 1000000 and do 10K index access,  
> then we increase the size of list 1M at each step and continue with 10K index access.  
> As we can see in the list_index_input.txt the time remains constant (0.038751423 secs)  
> So we can conclude the access time does not depend on list length and is constant ie O(1)  

##### 2. Devise an experiment to verify that get item and set item are O(1) for dictionaries.
> Refer to file dict_getset.py for implementation and dict_getset_input.txt for output.  
> **Approach** : We do n number of sets and gets in dictionary and measure the time for  
> 1 set and get and see that its fairly constant and independent of the size of the dictionary.

##### 3. Devise an experiment that compares the performance of the del operator on lists and dictionaries.
> Refer to file del_dictlist.py for implementation and del_dictlist_inout.txt for output.  
> **Approach**: First we insert 100K to 1M (step of 100K) elements in dictionary and lists  
> and then call 100K to 1M del operations(step of 100K)  on each of them. As seen in the  
> del_dictlist_inout.txt file - dict del operations are much much faster(100X+) than del on lists.

##### 4. Given a list of numbers in random order write a linear time algorithm to find the kth smallest number in the list.  
Explain why your algorithm is linear.
##### 5. Can you improve the algorithm from the previous problem to be O(n log(n))?
