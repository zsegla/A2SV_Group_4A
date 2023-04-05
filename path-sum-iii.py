# https://leetcode.com/problems/path-sum-iii/



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        paths = defaultdict(int)
        paths[0] = 1

        def helper(node, partial):
            if not node:
                return 0
            partial += node.val
            count = paths[partial - targetSum]

            paths[partial] += 1
            count += helper(node.left, partial)
            count += helper(node.right, partial)
            paths[partial] -= 1
            
            return count
        return helper(root, 0)
