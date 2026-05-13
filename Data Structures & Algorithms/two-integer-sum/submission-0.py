class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        for index, i in enumerate(nums):
            if target - i in hmap:
                return [hmap[target-i], index]
            hmap[i] = index
            
