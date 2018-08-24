#Given an array of integers, every element appears three times except for one. 
#Find that single one.
#
#Note:
#Your algorithm should have a linear runtime complexity. 
#Could you implement it without using extra memory? 


class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        ones = 0
        twos = 0
        for i in A:
        	twos = twos | (ones & i)
        	ones = ones ^ i
        	non_threes = ~(twos & ones)
        	ones = ones & non_threes
        	twos = twos & non_threes
        return ones