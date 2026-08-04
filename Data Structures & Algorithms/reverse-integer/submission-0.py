class Solution:
    def reverse(self, x: int) -> int:
        this = str(x)
        num = 0
        if this[0] == "-":
            new = this[1:][::-1]
            num = int("-"+new)
        else:
            num = int(this[::-1])
        return num if -2147483648 < num < 2147483647 else 0