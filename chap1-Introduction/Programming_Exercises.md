1.7 Programming Exercises And Solution
=================================================================================

#### 1. Implement the simple methods get_num and get_den that will return the numerator and denominator of a fraction.
- Please refer to #1 comment in Fraction.py file (same directory) for solution to this problem. 
- Test code is added in the FractionClient.py with #1 comment.

#### 2. In many ways it would be better if all fractions were maintained in lowest terms right from the start. Modify the constructor for the Fraction class so that GCD is used to reduce fractions immediately. Notice that this means the \_\_add\_\_ function no longer needs to reduce. Make the necessary modifications.
- Refer to #2 comment in the Fraction.py file (current directory)

#### 3. Implement the remaining simple arithmetic operators ( \_\_sub\_\_ , \_\_mul\_\_ , and \_\_truediv\_\_ ).
- Refer to #3 comment in the Fraction.py and FractionClient.py files.

#### 4. Implement the remaining relational operators ( \_\_gt\_\_ , \_\_ge\_\_ , \_\_lt\_\_ , \_\_le\_\_ , and \_\_ne\_\_ )
- Refer to #4 comment in the Fraction.py and FractionClient.py files.


#### 5. Modify the constructor for the fraction class so that it checks to make sure that the numerator and denominator are both integers. If either is not an integer the constructor should raise an exception.
- Refer to #5 comment in the Fraction.py and FractionClient.py files.


#### 6. In the definition of fractions we assumed that negative fractions have a negative numerator and a positive denominator. Using a negative denominator would cause some of the relational operators to give incorrect results. In general, this is an unnecessary constraint. Modify the constructor to allow the user to pass a negative denominator so that all of the operators continue to work properly.
- Refer to #6 comment in the Fraction.py file.


#### 7. Research the \_\_radd\_\_ method. How does it differ from \_\_add\_\_ ? When is it used? Implement \_\_radd\_\_ .
- Refer to #7 comment in the Fraction.py and FractionClient.py File.


#### 8. Repeat the last question but this time consider the \_\_iadd\_\_ method.
- Refer to #8 comment in the Fraction.py and FractionClient.py File.

#### 9. Research the \_\_repr\_\_ method. How does it differ from \_\_str\_\_ ? When is it used? Implement \_\_repr\_\_ .

#### 10. Design a class to represent a playing card. Now design a class to represent a deck of cards. Using these two classes, implement a favorite card game.

#### 11. Find a Sudoku puzzle in the local newspaper. Write a program to solve the puzzle.
