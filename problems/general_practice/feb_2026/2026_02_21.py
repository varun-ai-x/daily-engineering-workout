class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left   # ← Left child
        self.right = right # ← Right child

"""
A valid BST:

- Left subtree of node contains only nodes with keys less than node's key - root.left.val < root.val
- Right subtree of node contains only nodes with keys greater than node's key - root.right.val > root.val
- Both left and right subtrees must also be BSTs - recursive

    2
   / \
  1   3

  
    5
   / \
  1   4
     / \
    3   6  

Base Case - 
Recursive Case - At every point need to check if these above 2 conditions hold true. 

- left subtree
- right subtree

- Smallest recursive case: 

- How to check the next case in a Tree?


"""

