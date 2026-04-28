class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # list to set
        s = set(nums)
        return len(s) != len(nums)
