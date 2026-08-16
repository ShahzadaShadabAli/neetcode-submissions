class Solution:
    def countSeniors(self, details: List[str]) -> int:
        cnt = 0
        for n in details:
            if int(n[11:13]) > 60:
                cnt+=1
        return cnt