class TreeNode:
    def __init__(self, val): 
        self.val = int(val)
        self.left = self.right = None

def build_tree(nodes):
    from collections import deque
    if not nodes or nodes[0] == 'null': return None
    root = TreeNode(nodes[0])
    q = deque([root])
    i = 1
    while i < len(nodes):
        node = q.popleft()
        if nodes[i] != 'null':
            node.left = TreeNode(nodes[i])
            q.append(node.left)
        i += 1
        if i < len(nodes) and nodes[i] != 'null':
            node.right = TreeNode(nodes[i])
            q.append(node.right)
        i += 1
    return root

def max_depth(root):
    if not root: return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))


tree = input().split()
print(max_depth(build_tree(tree)))
