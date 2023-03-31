# https://leetcode.com/problems/count-good-numbers/description/



class Solution:
    def countGoodNumbers(self, n: int) -> int:
        modulo = 10**9 + 7
        count = 1

        if n % 2 == 0:
            count *= pow(4, (n//2), modulo)
            count *= pow(5, (n//2), modulo)
            count %= modulo
        else :
            count *= pow(4, (n //2), modulo)
            count *= pow(5, (n + 1)//2, modulo)
            count %= modulo
        return count
