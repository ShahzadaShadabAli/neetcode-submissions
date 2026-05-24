class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        verticals = defaultdict(list)
        horizontals = defaultdict(list)
        boxes = defaultdict(list)
     
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] != ".":               
                                  
                    indicex = math.ceil((i+1)/3)
                    indicey = math.ceil((j+1)/3)
                    if board[i][j] in boxes[indicex,indicey]:
                        return False
                    print(indicey, indicey)
                    boxes[indicex,indicey].append(board[i][j])
                    
                    if board[i][j] in horizontals[i]:
                        return False
                    horizontals[i].append(board[i][j])
                    
                    if board[i][j] in verticals[j]:
                        return False
                    verticals[j].append(board[i][j])

        return True

        