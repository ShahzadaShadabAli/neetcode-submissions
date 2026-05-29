class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for m in matrix:
            if m[0] <= target <= m[-1]:

                l, r = 0, len(m)-1
                while l<=r:
                    mid = int((l+r)/2)
                    if target == m[mid]:
                        return True
                    elif target > m[mid]:
                        l = mid+1
                    elif target < m[mid]:
                        r = mid-1
                return False
        return False