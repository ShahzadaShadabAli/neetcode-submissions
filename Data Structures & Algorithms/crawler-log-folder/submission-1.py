class Solution:
    def minOperations(self, logs: List[str]) -> int:
        layer = 0
        for l in logs:
            if l == "../":
                if layer >0:
                    layer-=1
            elif l == "./":
                ...
            else:
                layer+=1
        return layer