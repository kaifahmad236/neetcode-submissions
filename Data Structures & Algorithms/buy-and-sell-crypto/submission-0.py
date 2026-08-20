class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        l, r=0, 1
       
        maxi=0
        while r<len(prices):
            if prices[l] < prices[r]:
                curr_pr= prices[r]- prices[l]
                maxi= max(maxi, curr_pr)
            else:
                l=r
            r+=1  
        return maxi


        