def diameterOfBinaryTree(root):
    res = 0
    def depth(root):
        if root is None:
            return 0
        left = depth(root.left)
        right = depth(root.right)
        res = max(res, left + right)
        return 1 + max(left, right)
    depth(root)
    return res