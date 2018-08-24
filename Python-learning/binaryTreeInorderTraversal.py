class Treenode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def inorderTraversal(self, root):
        if root == None:
            return []
        outList = []
        stack = []
        current = root
        while True:
            while current != None:
                stack.append(current)
                current = current.left
            if current == None and len(stack) == 0:
                return outList
            elif current == None and len(stack)>0:
                current = stack[-1]
                del stack[-1]
            outList = outList + [current.val]
            current = current.right

test = Solution()
a = Treenode(2)

test.inorderTraversal(a)




