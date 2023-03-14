# https://leetcode.com/problems/powx-n/description/



class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        neg = n < 0   # negative powers are the inverse of positive powers
        pos_result = self.pos_pow(x, abs(n))   # call the recursive function here
        
        return 1/pos_result  if neg else pos_result  # playing with sign of the powers
    
    
    def pos_pow(self, x, n):
        
        if n == 0:  # base case
            return 1
        
        temp = self.pos_pow(x, n//2)  # recursive case
        temp *= temp 
        
        return temp if n%2 == 0 else temp * x  # even powers and odd powers
