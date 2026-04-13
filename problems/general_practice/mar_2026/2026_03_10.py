from collections import defaultdict, deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
    
    # write level by level using BFS. Using a Queue. Add elements to a Q and then 
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
        return self.root             
    

    def __str__(self):
        res = []
        q = deque([self.root])

        while q:            
            curr = q.popleft()
            res.append(str(curr.val))
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)

        return ' '.join(res)
    

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
    tree = BinaryTree()
    vals = [1, 2, 3, 4, 5]

    tree.insert_level_order(vals)

    print(tree.dfs_tree())


            




