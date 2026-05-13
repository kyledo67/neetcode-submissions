class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num = sorted(nums)
        hmap = {}
        for i in num:
            hmap[i] = hmap.get(i, 0) + 1
        sorted_keys = sorted(hmap, key=lambda x: hmap[x], reverse=True)
        return sorted_keys[:k]


            


        

        

