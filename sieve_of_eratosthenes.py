'''
❓ PROMPT
The [Sieve of Eratosthenes](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes) is an ancient algorithm for finding all of the prime numbers between up to a given upper bound. It's much more efficient than a function to check whether or not a given single number is prime, if that function is going to be called many times.

The way it works is quite straight foward: We start by assuming all of the numbers between two and the upper bound are prime. Then starting from two, if that number is still marked as prime, we then start counting by twos and remove all of it's multiples. Then move on to three. When we get to four, we've already removed it from our set of candidates, so we continue to five. Five has not been removed so is prime, now count by fives and remove all of those numbers.

This is often implemented with an array of booleans and they all start out as true, then we mark the composites as false, but it makes a lot of sense to do this with a set, first filling it with all of the candidates and then removing the composites.

Example(s)
sieveOfEratosthenes(5) => 2, 3, 5
sieveOfEratosthenes(10) => 2, 3, 5, 7
'''


def sieveOfEratosthenes(n):
    num_set = set([i for i in range(2, n + 1)])
    start = 2
    while start < n:
        for n in range(start + start, n + 1, start):
            if n in num_set:
                num_set.remove(n)
        start += 1
    return list(num_set)


print(sieveOfEratosthenes(5)) # 2, 3, 5

print(sieveOfEratosthenes(10)) # => 2, 3, 5, 7
