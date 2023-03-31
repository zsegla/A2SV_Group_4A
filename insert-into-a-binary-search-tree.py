# https://leetcode.com/problems/insert-into-a-binary-search-tree/



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        new_node = TreeNode(val)
        if not root:
            return new_node
        
        node = root
        while True:
            if val < node.val:
                if not node.left:
                    node.left = new_node
                    return root
                node = node.left
            else:
                if not node.right:
                    node.right = new_node
                    return root
                node = node.right
