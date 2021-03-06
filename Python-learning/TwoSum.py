#Given an array of integers, find two numbers such that they add up to a 
# specific target number.
#The function twoSum should return indices of the 
#two numbers such that they add up to the target, 
#where index1 must be less than index2. Please note that your
#returned answers (both index1 and index2) are not zero-based.

#You may assume that each input would have exactly one solution.

#Input: numbers={2, 7, 11, 15}, target=9
#Output: index1=1, index2=2 

class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
    	inxDict = {}
    	for i in range(len(num)):
    		if num[i] in inxDict:
    			if num[i] * 2 == target:
    				return (inxDict[num[i]]+1,i+1)
    		else:
    			inxDict[num[i]] = i
    	for i in range(len(num)):
    		rest = target - num[i] 
    		if rest in inxDict:
    			if inxDict[rest] != i:
	    			if inxDict[num[i]] <= inxDict[rest]:
	    				return(inxDict[num[i]]+1, inxDict[rest]+1)
	    			else:
	    				return(inxDict[rest] + 1, inxDict[num[i]]+1)



s = Solution()
x = [1,2,3,3,4]
print s.twoSum(x,5)