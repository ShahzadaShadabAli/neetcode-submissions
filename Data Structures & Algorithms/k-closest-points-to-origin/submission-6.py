class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        hashMap = {}
        for p in points:
            dis = math.sqrt(abs(p[0]*p[0] + p[1]*p[1]))
            if hashMap.get(dis, []):
                hashMap[dis].append(p)
            else:
                hashMap[dis] = [p]
        for i in (sorted(list(hashMap.keys()))):
            for n in hashMap[i]:
                res.append(n)
                if len(res) == k:
                    return res