class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        L, R = 0, len(matrix)-1
        while L <= R:
            MID = int((L+R)/2)
            if target > matrix[MID][-1]:
                L = MID+1
            elif target < matrix[MID][0]:
                R = MID-1
            else:

                l, r = 0, len(matrix[MID])-1
                while l<=r:
                    mid = int((l+r)/2)
                    if target == matrix[MID][mid]:
                        return True
                    elif target > matrix[MID][mid]:
                        l = mid+1
                    elif target < matrix[MID][mid]:
                        r = mid-1
                return False
        return False

        # L, R = 0, len(matrix)-1
        # while L<=R:
        #     mid = (L+R)//2
        #     if matrix[mid][0] <= target <= matrix[mid][-1]:
        #         l, r = 0, len(matrix[mid])
        #         while l<=r:
        #             Mid = (l+r)//2
        #             if target == matrix[mid][Mid]:
        #                 return True
                        
        #             elif target < matrix[mid][Mid]:
        #                 r = Mid-1
                        
        #             elif target > matrix[mid][Mid]:
        #                 l = Mid+1
        #         return False
                    
        #     elif target > matrix[mid][-1]:
        #         L = mid+1
        #     elif target < matrix[mid][0]:
        #         R = mid-1
        # return False