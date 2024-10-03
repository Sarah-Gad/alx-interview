#!/usr/bin/python3
"""
Prime Game
"""


def isWinner(x, nums):
    """Solution to Prime Game Task"""
    if x < 1 or not nums:
        return None

    maxPrime = max(nums)
    primeNumbers = [True for _ in range(maxPrime + 1)]
    primeNumbers[0] = False
    primeNumbers[1] = False
    p = 2

    while p * p <= maxPrime:
        if primeNumbers[p]:
            for i in range(p * p, maxPrime + 1, p):
                primeNumbers[i] = False
        p += 1

    benCount = 0
    mariaCount = 0
    for num in nums:
        numSet = list(range(1, num + 1))
        isMariaTurn = True
        primes = [
            i for i, is_prime in enumerate(primeNumbers)
            if is_prime and i <= num
            ]

        while numSet:
            found_prime = False
            for prime in primes:
                if prime in numSet:
                    found_prime = True
                    numSet = [n for n in numSet if n % prime != 0]
                    break
            if not found_prime:
                break

            isMariaTurn = not isMariaTurn

        if isMariaTurn:
            benCount += 1
        else:
            mariaCount += 1

    if mariaCount > benCount:
        return "Maria"
    elif benCount > mariaCount:
        return "Ben"
    else:
        return None
