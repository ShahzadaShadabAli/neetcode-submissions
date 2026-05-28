class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        s=0
        numbersSet = set(numbers)
        while s < len(numbers)-1:
            find = target-numbers[s]
            if find in numbersSet:
                f = s+1
                while f < len(numbers):
                    print(s, f)
                    if numbers[f]+numbers[s] == target:
                        return [s+1, f+1]
                    f+=1

            s+=1