class Solution:
    def b(self, nums: List[int], left: int, right: int, target: int) -> int: 
        if left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            if target < nums[mid]: # left
                return self.b(nums, left, mid - 1, target)
            else: 
                return self.b(nums, mid + 1, right, target)
        else:
            return -1

    def search(self, nums: List[int], target: int) -> int:
        return self.b(nums, 0, len(nums) - 1, target)