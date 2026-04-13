from collections import defaultdict, deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None


    """
    - BFS for implementing level order
    - Use a queue to add the nodes to
    - Initialize the queue with self.root
    - Append the left and right nodes
    """

    def insert_level_order(self, vals):
        if not self.root:
            self.root = TreeNode(vals[0])

        q = deque([self.root])
        i = 1

        while q:
            curr = q.popleft()

            if i < len(vals) and not curr.left:
                curr.left = TreeNode(vals[i])
                q.append(curr.left)
                i += 1

            if i < len(vals) and not curr.right:
                curr.right = TreeNode(vals[i])
                q.append(curr.right)
                i += 1

    """
    - BFS implementation to read the tree
    """
    
    def __str__(self):
        q = deque([self.root])
        res = []

        while q:
            curr = q.popleft()
            res.append(str(curr.val))

            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)

        return " ".join(res)
    

    """
    - Base Case
    - Decision
    - Recursion

    
    
    - Read the value
    - Recurse through the left tree
    - Recurse through the right tree
    - 

    """
    
    def dfs_tree(self):
        res = []

        def dfs(node):
            res.append(node.val)
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)
        
        dfs(self.root)

        return res



if __name__ == "__main__":
    bt = BinaryTree()
    vals = [1, 2, 3, 4, 5]

    bt.insert_level_order(vals)
    print(bt)

    print(bt.dfs_tree())



