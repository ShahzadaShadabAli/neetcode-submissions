class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i, n in enumerate(numbers):
            find = target-n
            if find in numbers:
                j=i+1
                while j < len(numbers):
                    if numbers[j] == find:
                        return[i+1, j+1]
                    j+=1