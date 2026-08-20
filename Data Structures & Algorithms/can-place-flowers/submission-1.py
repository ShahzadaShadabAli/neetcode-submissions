class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        prev = 0
        flowerbed.append(0)
        for i in range(len(flowerbed)-1):
            print(prev,flowerbed[i],flowerbed[i+1])
            if prev or flowerbed[i] or flowerbed[i+1]:
                ...
            else:
                n-=1
                flowerbed[i]=1
            prev = flowerbed[i]
        return False if n > 0 else True

        