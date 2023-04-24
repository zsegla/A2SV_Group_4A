# https://leetcode.com/problems/binary-tree-paths/description/




# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def helper(node, part): 
            if not node: 
                return
            part.append(str(node.val))
            if not node.left and not node.right:
                paths.append("->".join(part))
                return
            helper(node.left, part[:])
            helper(node.right, part)
            
        paths = []
        helper(root, [])
        return paths
