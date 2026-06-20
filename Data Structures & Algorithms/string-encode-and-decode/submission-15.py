class Solution:

    def encode(self, strs: List[str]) -> str:
        newStr = ''
        for i in strs:
            newStr += str(len(i)) + '.' + i
        return newStr
    def decode(self, s: str) -> List[str]:
        print(s)
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '.':
                j+=1
            count = int(s[i:j])
            end = count + j + 1
            print(end)
            #5#Hello5#World
            i=end
            res.append(s[j+1:end])
            
        return res