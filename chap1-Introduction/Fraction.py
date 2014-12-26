# Fraction class

from gcd import gcd


class Fraction:

    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def show(self):
        print (self.num, "/", self.den)

    def __add__(self, other):
        new_num = (self.num * other.den) + (self.den * other.num)
        new_den = self.den * other.den
        common = gcd(new_num, new_den)
        return Fraction(new_num // common, new_den // common)

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

    def __mul__(self, other):
        num = self.num * other.num
        den = self.den * other.den
        return Fraction(num, den)

    def __truediv__(self, other):
        num = self.num * other.den
        den = self.den * other.num
        common = gcd(num, den)
        return Fraction(num // common, den // common)

    def __sub__(self, other):
        num = (self.num * other.den) - (self.den * other.num)
        den = self.den * other.den
        common = gcd(num, den)
        return Fraction(num // common, den // common)
