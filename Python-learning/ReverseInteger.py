#Reverse digits of an integer.
#Example1: x = 123, return 321
#Example2: x = -123, return -321 
#Test
import sys
class Solution:
    # @return an integer
    def reverse(self, x):
    	if not isinstance(x,int):
    		sys.exit(0)
    	flag_positive = True
    	if x<=0:
			x = -1 * x
			flag_positive = False
    	xStr = str(x)
    	xStr = xStr[::-1]
    	x = int(xStr) if flag_positive == True else int(xStr)
    	return x

num = int(sys.argv[1].strip());

test = Solution()
print test.reverse(num)


