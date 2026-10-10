class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        i=1
        j=max(piles)
        while i<=j:
            mid= (i+j)//2
            t= sum((p+mid-1)//mid for p in piles)
        
            if t<=h:
                j=mid-1
            else:
                i=mid+1
        return i