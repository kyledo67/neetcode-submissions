class Solution:

    def encode(self, strs: List[str]) -> str:
        newstr = ''
        for i in strs:
            newstr += str(len(i)) + '#' + i
        return newstr
    def decode(self, s: str) -> List[str]:
        arr, i = [], 0
        while i < len(s):
            j=i
            while s[j] != '#':
                j+=1
                #5#Hello
                #012
            length = int(s[i:j])
            i = j + 1
            j = i + length
            arr.append(s[i:j])
            i = j
        return arr