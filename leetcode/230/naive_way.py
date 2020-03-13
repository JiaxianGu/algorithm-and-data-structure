class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        counter = 0
        def inOrder(root):
            if root:
                inOrder(root.left)
                stack.append(root)
                counter += 1
                if counter == k
                    return root
                inOrder(root.right)