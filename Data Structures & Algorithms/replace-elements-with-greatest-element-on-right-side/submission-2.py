class Solution:

    def replaceElements(self, arr: list[int]) -> list[int]:
        max_so_far = -1

        for i in range(len(arr) - 1, -1, -1):
            temp = arr[i]  # Save original value
            arr[i] = max_so_far  # Replace current element
            max_so_far = max(max_so_far, temp)

        return arr