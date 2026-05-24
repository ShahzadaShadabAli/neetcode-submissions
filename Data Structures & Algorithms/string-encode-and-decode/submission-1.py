class Solution:

    def encode(self, strs: List[str]) -> str:
        myStr = ""
        for n in strs:
            length = len(n)
            myStr += str(length)+"#"+n
        return myStr

    def decode(self, s: str) -> List[str]:
        num_arr = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            print(j, i)                
            length = int(s[i:j])
            myStr = s[j+1: length+j+1]
            num_arr.append(myStr)
            i = j+1+length
        return num_arr