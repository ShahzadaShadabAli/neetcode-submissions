class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # hashNums = defaultdict(int)
        # dihNums = defaultdict(list)
        # output = []
        # for n in nums:
        #     hashNums[n]+=1
        # high = -1
        # for key, value in (hashNums.items()):
        #     if high < value:
        #         high = value
        #     dihNums[value].append(key)
        # count = 0
        # print(dihNums, high)
        # while count < k:
        #     if len(dihNums[high]) != 0:
        #         output.append(dihNums[high].pop())
        #         count += 1
        #     else:
        #         high-=1
        output = []
        count = Counter(nums)
        for i in range(k):
            output.append(count.most_common()[i][0])
        return(output)

        
