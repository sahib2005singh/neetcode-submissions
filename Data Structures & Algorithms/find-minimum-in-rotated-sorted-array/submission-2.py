class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0 
        r = len(nums)-1
        while l<=r:
            if nums[l]<nums[r]:
                minnum = nums[l]
                r-=1
            else:
                minnum = nums[r]
                l+=1
        return minnum
        