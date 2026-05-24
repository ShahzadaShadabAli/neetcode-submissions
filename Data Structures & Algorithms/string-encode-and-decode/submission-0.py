class Solution:

    def encode(self, strs: List[str]) -> str:
        myStr = ""
        for n in strs:
            length = len(n)
            myStr += str(length)+"#"+n
        print(myStr)
        return myStr

    def decode(self, s: str) -> List[str]:
        num = ""
        new_arr = []
        i=0
        while i < len(s):
            myStr = ""
            if s[i] != "#" and s[i].isdigit():
                num += s[i]
                i+=1
            else:
                print(i)
                for _ in range(int(num.strip())+1):
                    if _ != 0:
                        myStr += s[i]
                        
                    i+=1
                num = ""
                new_arr.append(myStr)
            myStr = ""
        return new_arr