## 간단한 구현문제
## 단순히 그냥 시작 판상태만 체크하면 되는 문제이다
## 일반 스도쿠 문제에 비하면 상당히 쉬운편(O(MN))

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rowcheck=[[False]*10 for _ in range(10)]
        colcheck=[[False]*10 for _ in range(10)]
        squarecheck=[[False]*10 for _ in range(10)]
        
        
        
        
        
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j]!='.':
                    tmp=int(board[i][j])
                    if rowcheck[i][tmp]:
                        return False
                    if colcheck[j][tmp]:
                        return False
                    if squarecheck[(i//3)*3+j//3][tmp]:
                        return False
                    rowcheck[i][tmp]=True
                    colcheck[j][tmp]=True
                    squarecheck[(i//3)*3+j//3][tmp]=True
        
        return True