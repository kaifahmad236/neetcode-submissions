class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_wat=0
        i, j= 0, len(heights)-1

        while i<j:
            w= j-i
            h= min(heights[i], heights[j])
            curr_wat= w*h
            max_wat= max(max_wat, curr_wat)

            if heights[i]< heights[j]:
                i+=1
            else:
                j-=1
        return max_wat
        

        