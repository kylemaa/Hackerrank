# Definition for a binary tree node.
class TreeNode:
  def __init__(self, x):
    self.val = x 
    self.left = None
    self.right = None
class Solution:
  def isValidBST(self, root):
    def helper(node, lower, upper):
      # base case:
      if not node:
        return True 
      if lower >= node.val or upper <= node.val:
        return False 
      # recursively call the helper function. But the right node is the 'root' this time 
      if not helper(node.right, node.val, upper):
        return False 
      # recursively call the helper function. But the left node is the 'root' this time 
      if not helper(node.left, lower, node.val):
        return False 
      return True 
    # pass the root to the helper function, 
    # the lower and upper values are big so helper function can have passing params
    return helper(root, float('-inf'), float('inf'))


node = TreeNode(5)
node.left = TreeNode(4)
node.right = TreeNode(7)
print(Solution().isValidBST(node))