class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        frequency = [[] for i in range(len(nums)+1)]
        ans = []
        for n in nums:
            count[n] = 1+ count.get(n,0)
        for key , value in count.items():
            frequency[value].append(key)
        for i in range(len(frequency)-1,0,-1):
            for n in frequency[i]:
                ans.append(n)
            if len(ans) == k:
                return ans
        
        