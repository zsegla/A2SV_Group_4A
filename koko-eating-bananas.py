# https://leetcode.com/problems/koko-eating-bananas/



class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        bananas, max_pile = sum(piles), max(piles)
        min_rate = (bananas + h - 1)//h
        max_rate = max_pile

        while min_rate < max_rate:
            rate = (min_rate + max_rate)//2
            time = 0

            for pile in piles:
                time += (pile + rate - 1)//rate
                if time > h:
                    break
            if time > h:
                min_rate = rate + 1
            else:
                max_rate = rate

        return min_rate
