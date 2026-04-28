class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        i = 1
        isDuplicate = False
        nums.sort()
        for num in range(len(nums) - 1):
            if nums[i - 1] == nums[i]:
                return True
            i += 1
        return False