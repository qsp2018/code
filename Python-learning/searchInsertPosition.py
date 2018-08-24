class Solution:
	def searchInsert(self, A, target):
		for i in range(0,len(A)):
			if target < A[i] or target == A[i]:
				return i
		return len(A)

