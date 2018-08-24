#Given n, how many structurally unique BST's (binary search trees) 
#that store values 1...n?
#For example,
#Given n = 3, there are a total of 5 unique BST's. 
import sys
class Solution:
    # @return an integer
    def numTrees(self, n):
    	arr = [0] * (n + 1)
    	arr[1] = 1
    	arr[0] = 1
    	for i in range(2,n+1):
    		this_cum = 0
    		for j in range(1,i+1): #1,...,i-1
    			this_cum +=  arr[j-1]*arr[i-j]
    		arr[i] = this_cum
    	return arr[n]
   
test = Solution()
input = int(sys.argv[1].strip())
print test.numTrees(input)