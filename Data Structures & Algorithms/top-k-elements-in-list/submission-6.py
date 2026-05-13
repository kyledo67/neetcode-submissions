class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = {}
        for i in nums:
            hmap[i] = hmap.get(i, 0) + 1
        buckets = [[] for _ in range(len(nums) + 1)]
        for key, val in hmap.items():
            buckets[val].append(key)
        res = []
        for i in range(len(buckets)-1, 0, -1):
            for c in buckets[i]:
                res.append(c)
                if len(res) == k:
                    return res

            


        

        

