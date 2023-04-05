# https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        x2y_and_val = defaultdict(list)

        def helper(node, x, y):
            if not node:
                return
            x2y_and_val[x].append((-y, node.val))
            helper(node.left, x - 1, y - 1)
            helper(node.right, x + 1, y - 1)
        helper(root, 0 ,0)
        result = []

        xs = sorted(x2y_and_val.keys())
        for x in xs:
            x2y_and_val[x].sort()
            result.append([val for _, val in x2y_and_val[x]])

        return result
