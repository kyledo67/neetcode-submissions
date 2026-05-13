class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = {}
        arr = [[] for i in range(len(nums)+1)]
        for num in nums:
            c[num] = c.get(num, 0) + 1
        for n, v in c.items():
            arr[v].append(n)
        res = []
        for i in range(len(arr)-1, 0, -1):
            for n in arr[i]:
                res.append(n)
                if len(res) == k:
                    return res
    