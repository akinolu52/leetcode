import math


def isPrime(number):
    if number < 3:
        return True
    
    start = 2
    stop = int(math.sqrt(number)) + 1

    return all(number % index != 0 for index in range(start, stop))


print(isPrime(1))
print(isPrime(2))
print(isPrime(3))
print(isPrime(9))
print(isPrime(5))
