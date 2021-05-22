import sys
input = sys.stdin.readline

board=[list(map(int,input().split())) for _ in range(9)]

board_y=[ [0]*9 for _ in range(9)]

board_box=[[0]*9 for _ in range(9)]

num={1,2,3,4,5,6,7,8,9}

done=False
def dfs(n):
    global done
    if done:
        return
    for i in range(n,9):
        for j in range(9):
            if i==8 and j==8 and board[i][j]!=0 and done==False:
                for f in range(9):
                    print(' '.join(map(str,board[f])))
                        
                done=True

            if board[i][j]==0:
                tmp = num - set(board[i])
                tmp = tmp - set(board_y[j])
                tmp = tmp - set(board_box[(i//3)*3+j//3])
                if i==8 and j==8 and len(tmp)==1 and done==False:
                    board[i][j]=list(tmp)[0]
                    for f in range(9):
                        print(' '.join(map(str,board[f])))
                        
                    done=True
                for k in tmp:
                    board[i][j]=k
                    dfs(i)
                    board[i][j]=0



for i in range(9):
    for j in range(9):
        board_y[i][j]=board[j][i]

for i in range(9):
    for j in range(9):
        board_box[(i//3)*3+j//3][(i%3)*3+j%3]=board[i][j]

dfs(0)