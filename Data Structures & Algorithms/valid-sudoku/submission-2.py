class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        verticalBoxes = defaultdict(list)
        horizontalBoxes = defaultdict(list)
        cubicBoxes = defaultdict(list)

        for i,row in enumerate(board):
            
            for j, col in enumerate(row):
                if col != ".":
                    print(col)
                    if col in horizontalBoxes[i]:
                        return False
                    else:
                        horizontalBoxes[i].append(col)

                    if col in verticalBoxes[j]:
                        return False
                    else:
                        verticalBoxes[j].append(col)

                    r = i//3
                    c = j//3

                    if col in cubicBoxes[(c, r)]:
                        return False
                    else:
                        cubicBoxes[(c, r)].append(col)
            print(cubicBoxes)
            print(horizontalBoxes)
            print(verticalBoxes)
        return True

        