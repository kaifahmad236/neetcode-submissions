# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node, m):
            if not node:
                return 0
            r=1 if node.val>= m else 0
            m= max(m, node.val)
            r += dfs(node.left, m)
            r += dfs(node.right, m)
            return r

        return dfs(root, root.val)



        