class Solution:
    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        encoded = ""
        for i in strs:
            encoded += str(len(i)) + '#' + str(i)
        return encoded

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            j = i
            while s[j] != '#':
                j+=1
            length = int(s[i:j])
            i = j+1
            j = j+length+1
            print(i)
            print(j)
            res.append(s[i:j])
            i = j
            5#Hello
        return res
            

