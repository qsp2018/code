class Treenode:
	def __init__(self,x):
		self.val = x
		self.left = None
		self.right = None

class Solution1: # recursive solution
	def preorderTraversal(self,root):
		if root is None:
			return []
		thisVal = [root.val]
		thisVal = thisVal + self.preorderTraversal(root.left)
		thisVal = thisVal + self.preorderTraversal(root.right)
		return thisVal


class Solution: # iterative solution
	def preorderTraversal(self,root):
		if root == None:
			return []
		queue = []
		queue.append(root)
		values = []
		while(len(queue)>0):
			thisNode = queue[0]
			values.append(thisNode.val)
			del queue[0]
			left = thisNode.left
			if left is not None:
				queue.append(left) 
			right = thisNode.right
			if right is not None:
				queue.append(right) 
		return values;

test = Treenode(2)
test.left = Treenode(4)
test.right = Treenode(1)
test.right.right = Treenode(5)
test.right.right.left = Treenode(3)


test1 = Solution1()
print test1.preorderTraversal(test)
