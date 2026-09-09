class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hmap1 = {}
        for i in s:
            hmap1[i] = hmap1.get(i, 0) + 1
        hmap2 = {}
        for i in t:
            hmap2[i] = hmap2.get(i, 0) + 1

        if hmap1 == hmap2:
            return True
        return False

