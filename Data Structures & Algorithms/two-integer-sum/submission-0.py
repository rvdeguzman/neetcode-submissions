class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffs = {} 

        for x, y in enumerate(nums):
            diff = target - y
            if (diff in diffs):
                return [diffs[diff], x]
            diffs[y] = x
                
        