class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        verticalBoxes = defaultdict(set)
        horizontalBoxes = defaultdict(set)
        cubeBoxes = defaultdict(set)

        for i, n in enumerate(board):
            for j, m in enumerate(n):
                if m != ".":

                    if m in verticalBoxes[j]:
                        return False
                    else:
                        verticalBoxes[j].add(m)

                    if m in horizontalBoxes[i]:
                        return False
                    else:
                        horizontalBoxes[i].add(m)

                    r, c = ((i)//3), ((j)//3)
                    if m in cubeBoxes[(r, c)]:
                        return False
                    else:
                        cubeBoxes[(r, c)].add(m)
        return True

        