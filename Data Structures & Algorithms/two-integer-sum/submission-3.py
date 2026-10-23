class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            sec_element = target - nums[i]
            if sec_element in nums:
                j = nums.index(sec_element)

                if i != j :
                    return sorted([i, j])