# https://leetcode.com/problems/open-the-lock/



class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        q, target = {"0000"}, {target}
        visited = set()
        deadends = set(deadends)
        steps = 0

        def shift(combo): # find all combinations
            shifts = set()
            for i, c in enumerate(combo):
                shifted = (int(c) + 1) % 10  # increase 
                shifts.add(combo[:i] + str(shifted) + combo[i+1:]) # strings are immutable
                shifted = (int(c) - 1) % 10  # decrease 
                shifts.add(combo[:i] + str(shifted) + combo[i+1:]) # strings are immutable
            return shifts

        while q:
            if target & q: # intersection between q and target
                return steps
            new_q = set()
            steps += 1

            for combo in q:
                if combo in visited or combo in deadends:
                    continue # ignore seen before or not allowed
                visited.add(combo)
                new_q |= shift(combo) # add all shifted combinations
            q, target = target, new_q
        return -1
