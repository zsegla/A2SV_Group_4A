# https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/



class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def canShip(capacity):
            d = days
            load = 0

            for weight in weights:
                if weight + load > capacity:
                    d -= 1
                    load = 0
                load += weight
                if d == 0:
                    return False
            return True
        
        min_cap = max(weights)
        max_cap = sum(weights)

        while min_cap < max_cap:
            mid_cap = (min_cap + max_cap)//2
            if canShip(mid_cap):
                max_cap = mid_cap
            else:
                min_cap = mid_cap + 1
        return min_cap
