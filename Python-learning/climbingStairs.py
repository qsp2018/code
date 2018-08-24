#
#You are climbing a stair case. 
#It takes n steps to reach to the top.
#Each time you can either climb 1 or 2 steps. 
#In how many distinct ways can you climb to the top? 

class Solution:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
    	wayV = [0] * max((n+1),3)
    	wayV[0] = 0
    	wayV[1] = 1
    	wayV[2] = 2
    	if n <= 2:
    		return wayV[n]
    	for i in range(3,n+1):
    		wayV[i] = wayV[i-1] + wayV[i-2]
    	return wayV[n]
