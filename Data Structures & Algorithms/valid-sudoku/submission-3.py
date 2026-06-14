class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        verticalBoxes = defaultdict(set)
        horizontalBoxes = defaultdict(set)
        cubicBoxes = defaultdict(set)

        for i,row in enumerate(board):
            
            for j, col in enumerate(row):
                if col != ".":
                    print(col)
                    if col in horizontalBoxes[i]:
                        return False
                    else:
                        horizontalBoxes[i].add(col)

                    if col in verticalBoxes[j]:
                        return False
                    else:
                        verticalBoxes[j].add(col)

                    r = i//3
                    c = j//3

                    if col in cubicBoxes[(c, r)]:
                        return False
                    else:
                        cubicBoxes[(c, r)].add(col)

        return True

        