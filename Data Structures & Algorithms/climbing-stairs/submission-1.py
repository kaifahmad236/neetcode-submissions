class Solution:
    def climbStairs(self, n: int) -> int:
        # return n
        i=1
        j=2
        if n==1:
            return i
        if n == 2:
            return j
        
        for x in range(3, n+1):
            current= i+j
            i=j
            j=current
        return j

        
        