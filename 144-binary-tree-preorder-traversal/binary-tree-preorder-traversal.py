# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = [root]
        while stack:
            root = stack.pop()
            if not root:
                continue
            res.append(root.val)
            stack.append(root.right)
            stack.append(root.left)

        return res




       


 #Recursive Solution: 
  #           res = []
  #      def dfs(root):
   #         if not root:
    #            return
   #         res.append(root.val)
    #        dfs(root.left)
     #       dfs(root.right)

     #   dfs(root)

    #    return res        '''