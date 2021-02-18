from typing import List

from test_framework import generic_test


# Given n, return all primes up to and including n.
def generate_primes(n: int) -> List[int]:
    # TODO - you fill in here.
    # primes = []
    # # is_prime[p] represents if p is prime or not. Initially, set each to true,
    # # expecting 0 and 1. Then use sieving to eliminate nonprimes.
    # is_prime = [False, False] + [True] * (n - 1)
    # for p in range(2, n + 1):
    #     if is_prime[p]:
    #         primes.append(p)
    #         # Sieve p's multiples
    #         for i in range(p * 2, n + 1, p):
    #             is_prime[i] = False
    # return primes
    if n < 2:
        return []
    size = (n - 3) // 2 + 1
    primes = [2]  # Stores the primes from 1 to n.
    # is_prime[i] represents (2i + 3) is prime or not.
    # For example, is_prime[0] represents 3 is prime or not, is_prime[1] represents 5,
    # is_prime[2] represents 7, etc.
    # Initially set each to true. Then use sieving to eliminate nonprimes.
    is_prime = [True] * size
    for i in range(size):
        if is_prime[i]:
            p = i * 2 + 3
            primes.append(p)
            # Sieving from p^2, where p^2 = (4i^2 + 12i + 9). The index in is_prime
            # is (2i^2 + 6i + 3) because is_prime[i] represents 2i + 3.
            # Note that we need to use long for j because p^2 might overflow.
            for j in range(2 * i**2 + 6 * i + 3, size, p):
                is_prime[j] = False
    return primes


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('prime_sieve.py', 'prime_sieve.tsv',
                                       generate_primes))
