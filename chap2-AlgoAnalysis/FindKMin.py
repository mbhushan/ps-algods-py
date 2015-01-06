import random


def partition(L, p, r):
    x = L[r]
    i = p-1
    for j in range(p, r):
        if L[j] <= x:
            i += 1
            L[i], L[j] = L[j], L[i]
    L[i+1], L[r] = L[r], L[i+1]
    return i+1


def randomPartition(L, p, r):
    if p == r:
        return p
    i = random.randint(p, r)
    L[i], L[r] = L[r], L[i]
    return partition(L, p, r)


def randomizedSelect(L, p, r, i):
    if p == r:
        return L[p]
    q = randomPartition(L, p, r)
    k = q - p + 1
    if i == k:
        return L[q]
    elif i < k:
        return randomizedSelect(L, p, q-1, i)
    else:
        return randomizedSelect(L, q+1, r, i-k)


def kthMinLinear(L, k):
    """ Assumption: L is a list of numbers. k is the index to be found.
    time complexity: O(n) - expected linear time implementation
    randomizedSelect method finds the Kth elemenet by repeated partitioning
    the List around randomly chosen pivot.
    """
    if L is None:
        return None
    if k < 0 or k > len(L):
        return None
    value = randomizedSelect(L, 0, len(L)-1, k)
    return value


def kthMin(L, k):
    """ Assumption is L is a list, here we will sort the list and return the
    Kth index - time complexity: O(nlog(n)) """
    if L is None:
        return None
    if k < 0 or k > len(L):
        return None
    L.sort()
    return L[k-1]


def readInput():
    flag = True
    while flag:
        try:
            print ("Enter comma separated numbers: ")
            S = input()
            S = S.split(",")
            S = [int(s.strip()) for s in S]
            flag = False
        except ValueError as e:
            print ("Invalid entry! Try Again..", e)

    flag = True
    while flag:
        try:
            print ("Enter k value: ")
            k = input()
            k = int(k.strip())
            flag = False
        except ValueError as e:
            print ("Bad Input! try again..", e)

    return (S, k)


def main():
    L, k = readInput()
    print ("Sorted list for reference is: ")
    print (sorted(L))
    kthVal = kthMin(L, k)
    print ("{} min value in list is - log_linear: {}".format(k, kthVal))
    random.shuffle(L)
    kthVal = kthMinLinear(L, k)
    print ("{} min value in list is - expected_linear: {}".format(k, kthVal))


if __name__ == '__main__':
    main()
