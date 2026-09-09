class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hmap1 = {}
        for i in s:
            hmap1[i] = hmap1.get(i, 0) + 1
        hmap2 = {}
        for i in t:
            hmap2[i] = hmap2.get(i, 0) + 1

        return hmap1 == hmap2

