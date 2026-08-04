class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car = [[p, s] for p, s in zip(position, speed)]
        stack = []

        for p, s in sorted(car)[::-1]:
            timeToReach = (target-p)/s
            if not stack or stack[-1] < timeToReach:
                stack.append(timeToReach)

        return len(stack)