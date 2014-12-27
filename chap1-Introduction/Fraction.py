# Fraction class

from gcd import gcd


class Fraction:

    # #2 solution for exercise 2 from 1.7 module chap-1
    def __init__(self, top, bottom):
        common = gcd(top, bottom)
        self.num = top // common
        self.den = bottom // common

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def show(self):
        print (self.num, "/", self.den)

    # #1 solution for programming exercise 1 from 1.7 modude of chap1
    def get_num(self):
        return self.num

    # #1 solution for programming exercise 1 from 1.7 modude of chap1
    def get_den(self):
        return self.den

    # #2 solution for exercise 2 from 1.7 module chap-1
    def __add__(self, other):
        new_num = (self.num * other.den) + (self.den * other.num)
        new_den = self.den * other.den
        return Fraction(new_num, new_den)
        # common = gcd(new_num, new_den)
        # return Fraction(new_num // common, new_den // common)

    def __eq__(self, other):
        first_num = self.num * other.den
        second_num = self.den * other.num

        return first_num == second_num

    def __gt__(self, other):
        first_num = self.num * other.den
        second_num = self.den * other.num
        return first_num > second_num

    def __lt__(self, other):
        first_num = self.num * other.den
        second_num = self.den * other.num
        return first_num < second_num

    # #3 solution for exercise 3 from 1.7 module chap-1
    def __mul__(self, other):
        num = self.num * other.num
        den = self.den * other.den
        return Fraction(num, den)

    # #3 solution for exercise 3 from 1.7 module chap-1
    def __truediv__(self, other):
        num = self.num * other.den
        den = self.den * other.num
        common = gcd(num, den)
        return Fraction(num // common, den // common)

    # #3 solution for exercise 3 from 1.7 module chap-1
    def __sub__(self, other):
        num = (self.num * other.den) - (self.den * other.num)
        den = self.den * other.den
        common = gcd(num, den)
        return Fraction(num // common, den // common)
