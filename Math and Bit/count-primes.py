# https://leetcode.com/problems/count-primes/



class Solution:
    def countPrimes(self, n: int) -> int:
        sieve = [False, False] + [True for _ in range(n-2)]     # 0 and 1 are not prime

        for i in range(2, int(n**0.5) + 1):     # end at sqrt since any j not prime must have a factor <= sqrt(j)

            if sieve[i]:                        # i is prime

                sieve[i*i:n:i] = [False] * len(sieve[i*i:n:i])  # list comprehension faster than loop
                                                                # start at i*i since i*(i-1) already eliminated
        return sum(sieve)
