class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
        if len(s)!=len(t):
            return False
        hm1, hm2 = {}, {}
        for i in range(len(s)):
            hm1[s[i]] = 1 + hm1.get(s[i], 0)
            hm2[t[i]] = 1 + hm2.get(t[i], 0)
        for key in hm1:
            if hm1[key] != hm2.get(key, 0):
                return False
        return True

