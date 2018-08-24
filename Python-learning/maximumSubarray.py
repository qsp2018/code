class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
    	if len(A) == 0:
    		return None

    	_max = A[0]
    	_cum = A[0]

    	for i in range(1,len(A)):
    		if _cum<=0:
    			_cum = A[i]
    		elif _cum>0:
    			_cum = _cum + A[i]
    		_max = max(_max,_cum)

    	return _max

    		