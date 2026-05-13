class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = {}
        for i in nums:
            hmap[i] = hmap.get(i, 0) + 1

        res = []
        buckets = [[] for _ in range(len(nums)+1)]

        for n, c in hmap.items():
            buckets[c].append(n)
        

        for i in range(len(buckets)-1, 0, -1):
            for n in buckets[i]:
                res.append(n)
                if len(res) == k:
                    return res






        

        

 