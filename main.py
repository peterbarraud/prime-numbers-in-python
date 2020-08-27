# which is more efficient
# import math
import timeit
from math import sqrt, ceil

class Primes:
    def __init__(self, count):
        self.__count = count

    def prime_list(self):
        # we're going to assume that 2 is a prime - without checking for it
        primes = [2]
        # now get a list of all the numbers greater than 1 and equal the square root of x (rounded up)
        for x in range(2, self.__count+1):
            l = [x for x in range(2, ceil(sqrt(x)))] + primes
            if not all([x%s for s in l]):
                pass
            else:
                primes.append(x)
        print(primes)

if __name__ == "__main__":
    primes = Primes(5000)
    primes.prime_list()
