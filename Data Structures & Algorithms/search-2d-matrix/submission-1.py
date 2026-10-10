class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m,n=len(matrix), len(matrix[0])

        i, j=0, (m*n)-1
        while i<=j:
            mid= (i+j)//2
            
            x= matrix[mid//n][mid%n]
            if x==target:
                return True
            elif x<target:
                i=mid +1
            else:
                j=mid-1
        return False

        
        