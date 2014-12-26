
def readInt(val=''):
    while True:
        n = input("value {}: ".format(val))
        try:
            n = int(n)
            return n
        except ValueError:
            print ("Non numeric input - please try again!")


def gcd(n, m):
    if n == 0 or m == 0:
        return None
    if n < m:
        n, m == m, n

    while n % m != 0:
        old_n = n
        old_m = m
        n = old_m
        m = old_n % old_m
    return m


def main():
    n = readInt('n')
    m = readInt('m')
    ans = gcd(n, m)
    print ("GCD of {} and {} is: {}".format(n, m, ans))


if __name__ == '__main__':
    main()
