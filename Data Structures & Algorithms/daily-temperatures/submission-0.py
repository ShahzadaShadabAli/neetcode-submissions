class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = []
        for i in range(len(temperatures)):
            count = 0
            final = 0
            for j in range(i+1, len(temperatures)):

                if temperatures[j] > temperatures[i]:
                    final = count + 1
                    break
                elif temperatures[j] < temperatures[i] and count == 0:
                    coun = 0
                    final = 0
                count+=1
            output.append(final)
        return output