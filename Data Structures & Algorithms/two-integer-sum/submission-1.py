class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = {}
        for i, num in enumerate(nums):
            need = target - num

            if need in n:
                return [n[need], i]

            n[num] = i


        
        