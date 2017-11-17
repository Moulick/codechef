"""Trozan Number is a number that is strong but not a perfect power. A number n is known as a strong number if,
for every prime divisor or factor p of n, p2 is also a divisor. In other words, every prime factor appears at least
squared.

All Trozan numbers are strong. However, not all strong numbers are Trozan numbers: only those that cannot be
represented as mk, where m and k are positive integers greater than 1.

For a given a N you have to output whether it is a trozan number or not.

Input

First line of input contains a single integer T (1 ≤ T ≤ 5000), the number of test cases.

Each test case contains a line containing the number N (2 ≤ N ≤ 1000000000).

Output

for each testcase output YES if it is a Trozan Number or NO otherwise.

The function should return true, if the number is a Trojan Number. It should return false, otherwise.

Note: You are allowed to edit the code as you please. Add / delete headers. Add / delete methods. And so on.. So long
as your final code solves the problem with Input and Output as described above. You may submit your own code,
without using the template at all.

Example

Input:
3
2
8
108

Output:
NO
NO
YES
Example (if you use the Solution Template)

isTrojan(2) should return false
isTrojan(8) should return false
isTrojan(108) should return true



Created on Fri Nov 17 22:19:50 2017

@author: moulick
"""

import random


def primesbelow(n):
    # http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    # """ Input n>=6, Returns a list of primes, 2 <= p < n """
    correction = n % 6 > 1
    n = {0: n, 1: n - 1, 2: n + 4, 3: n + 3, 4: n + 2, 5: n + 1}[n % 6]
    sieve = [True] * (n // 3)
    sieve[0] = False
    for i in range(int(n ** .5) // 3 + 1):
        if sieve[i]:
            k = (3 * i + 1) | 1
            sieve[k * k // 3::2 * k] = [False] * ((n // 6 - (k * k) // 6 - 1) // k + 1)
            sieve[(k * k + 4 * k - 2 * k * (i % 2)) // 3::2 * k] = [False] * (
                (n // 6 - (k * k + 4 * k - 2 * k * (i % 2)) // 6 - 1) // k + 1)
    return [2, 3] + [(3 * i + 1) | 1 for i in range(1, n // 3 - correction) if sieve[i]]


smallprimeset = set(primesbelow(100000))
_smallprimeset = 100000


def isprime(n, precision=7):
    # http://en.wikipedia.org/wiki/Miller-Rabin_primality_test#Algorithm_and_running_time
    if n < 1:
        raise ValueError("Out of bounds, first argument must be > 0")
    elif n <= 3:
        return n >= 2
    elif n % 2 == 0:
        return False
    elif n < _smallprimeset:
        return n in smallprimeset

    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1

    for repeat in range(precision):
        a = random.randrange(2, n - 2)
        x = pow(a, d, n)

        if x == 1 or x == n - 1:
            continue

        for r in range(s - 1):
            x = pow(x, 2, n)
            if x == 1:
                return False
            if x == n - 1:
                break
        else:
            return False

    return True


# https://comeoncodeon.wordpress.com/2010/09/18/pollard-rho-brent-integer-factorization/
def pollard_brent(n):
    if n % 2 == 0:
        return 2
    if n % 3 == 0:
        return 3

    y, c, m = random.randint(1, n - 1), random.randint(1, n - 1), random.randint(1, n - 1)
    g, r, q = 1, 1, 1
    while g == 1:
        x = y
        for i in range(r):
            y = (pow(y, 2, n) + c) % n

        k = 0
        while k < r and g == 1:
            ys = y
            for i in range(min(m, r - k)):
                y = (pow(y, 2, n) + c) % n
                q = q * abs(x - y) % n
            g = gcd(q, n)
            k += m
        r *= 2
    if g == n:
        while True:
            ys = (pow(ys, 2, n) + c) % n
            g = gcd(abs(x - ys), n)
            if g > 1:
                break

    return g


smallprimes = primesbelow(
    1000)  # might seem low, but 1000*1000 = 1000000, so this will fully factor every composite < 1000000


def primefactors(n, sort=False):
    factors = []

    for checker in smallprimes:
        while n % checker == 0:
            factors.append(checker)
            n //= checker
        if checker > n:
            break

    if n < 2:
        return factors

    while n > 1:
        if isprime(n):
            factors.append(n)
            break
        factor = pollard_brent(n)  # trial division did not fully factor, switch to pollard-brent
        factors.extend(
            primefactors(factor))  # recurse to factor the not necessarily prime factor returned by pollard-brent
        n //= factor

    if sort:
        factors.sort()

    return factors


def factorization(n):
    factors = {}
    for p1 in primefactors(n):
        try:
            factors[p1] += 1
        except KeyError:
            factors[p1] = 1
    return factors


totients = {}


def totient(n):
    if n == 0:
        return 1

    try:
        return totients[n]
    except KeyError:
        pass

    tot = 1
    for p, exp in factorization(n).items():
        tot *= (p - 1) * p ** (exp - 1)

    totients[n] = tot
    return tot


def gcd(a, b):
    if a == b:
        return a
    while b > 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    return abs((a // gcd(a, b)) * b)


def is_square(apositiveint):
    x = apositiveint // 2
    seen = {x}
    while x * x != apositiveint:
        x = (x + (apositiveint // x)) // 2
        if x in seen:
            return False
        seen.add(x)
    return True


def strong(n):

    primes = primefactors(n)

    for x in primes:
        if n % (x * x) != 0:
            return False

    return True
