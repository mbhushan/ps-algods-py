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
> **object.\_\_repr\_\_(self):**
> Called by the repr() built-in function and by string conversions (reverse quotes) to compute the “official” string representation of an object. If at all possible, this should look like a valid Python expression that could be used to recreate an object with the same value (given an appropriate environment). If this is not possible, a string of the form <...some useful description...> should be returned. The return value must be a string object. If a class defines \_\_repr\_\_() but not \_\_str\_\_(), then \_\_repr\_\_() is also used when an “informal” string representation of instances of that class is required.
This is typically used for debugging, so it is important that the representation is information-rich and unambiguous.

> **object.\_\_str\_\_(self):**
> Called by the str() built-in function and by the print statement to compute the “informal” string representation of an object. This differs from __repr__() in that it does not have to be a valid Python expression: a more convenient or concise representation may be used instead. The return value must be a string object.

- Please refer to #9 comment in Fraction.py and FractionClient.py file.

#### 10. Design a class to represent a playing card. Now design a class to represent a deck of cards. Using these two classes, implement a favorite card game.
** We are going to implement the War card game - following resources might be useful for reference**

> -  http://www.pagat.com/war/war.html
> - http://en.wikipedia.org/wiki/War_(card_game)

**Please refer following files:**

> * Card.py
> * Deck.py
> * WarCardGame.py

#### 11. Find a Sudoku puzzle in the local newspaper. Write a program to solve the puzzle.
