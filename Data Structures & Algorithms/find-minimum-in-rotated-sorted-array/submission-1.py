class Solution:
    def findMin(self, nums: List[int]) -> int:
        min = max(nums)
        for i in nums:
            if i < min:
                min = i
        return min
        