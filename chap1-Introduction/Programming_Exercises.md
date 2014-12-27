1.7 Programming Exercises And Solution
=================================================================================

#### 1. Implement the simple methods get_num and get_den that will return the numerator and denominator of a fraction.
- Please refer to #1 comment in Fraction.py file (same directory) for solution to this problem. 
- Test code is added in the FractionClient.py with #1 comment.

#### 2. In many ways it would be better if all fractions were maintained in lowest terms right from the start. Modify the constructor for the Fraction class so that GCD is used to reduce fractions immediately. Notice that this means the __add__ function no longer needs to reduce. Make the necessary modifications.
- Please refer to #2 comment in the Fraction.py file (current directory)

3. Implement the remaining simple arithmetic operators ( __sub__ , __mul__ , and
__truediv__ ).
4. Implement the remaining relational operators ( __gt__ , __ge__ , __lt__ , __le__ , and
__ne__ )
5. Modify the constructor for the fraction class so that it checks to make sure that the nu-
merator and denominator are both integers. If either is not an integer the constructor
should raise an exception.
6. In the definition of fractions we assumed that negative fractions have a negative numera-
tor and a positive denominator. Using a negative denominator would cause some of the
relational operators to give incorrect results. In general, this is an unnecessary constraint.
Modify the constructor to allow the user to pass a negative denominator so that all of the
operators continue to work properly.
7. Research the __radd__ method. How does it differ from __add__ ? When is it used?
Implement __radd__ .
8. Repeat the last question but this time consider the __iadd__ method.
9. Research the __repr__ method. How does it differ from __str__ ? When is it used?
Implement __repr__ .
10. Design a class to represent a playing card. Now design a class to represent a deck of
cards. Using these two classes, implement a favorite card game.
11. Find a Sudoku puzzle in the local newspaper. Write a program to solve the puzzle.
