class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        nodes = root

        while nodes:
            stack.append(nodes)
            nodes = nodes.left
        counter = 0
        while stack and (counter < k):
            temp = stack.pop()
            counter += 1
            right = temp.right
            while right:
                stack.append(right)
                right = right.left
        return temp.val