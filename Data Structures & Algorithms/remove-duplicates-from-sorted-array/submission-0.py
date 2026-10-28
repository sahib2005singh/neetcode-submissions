class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 0
        r = 1
        while r != len(nums):
            if nums[l] != nums[r]:
                l+=1
                r+=1
            elif nums[l] == nums[r]:
                nums.pop(r)
                


        return len(nums)

        