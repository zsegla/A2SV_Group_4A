# https://leetcode.com/problems/additive-number/



class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)
        if n < 3:
            return False

        for second in range(1, 1 + (n - 1) // 2):       # first digit of second integer
            if num[0] == "0" and second > 1:
                break
            third = second + 1                          # first digit of third integer

            while n - third >= max(second, third - second):
                if num[second] == "0" and third > second + 1:
                    break

                n1, n2 = int(num[0:second]), int(num[second:third])
                start = third
                while True:
                    next_int = n1 + n2
                    next_start = start + len(str(next_int))
                    if num[start] == "0" and next_start > start + 1:
                        break
                    if next_int != int(num[start:next_start]):
                        break
                    if next_start == n:
                        return True
                    n1, n2, start = n2, next_int, next_start

                third += 1

        return False
