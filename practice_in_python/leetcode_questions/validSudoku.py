class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        st = set()
        # checks rows only
        for row in board:
            for num in row:
                if num == '.':
                    continue
                if num in st:
                    return False
                st.add(num)
            st.clear()
        # check cols only
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[j][i] == '.':
                    continue
                if board[j][i] in st:
                    return False
                st.add(board[j][i])
            st.clear()
        # check 3 x 3
        for i in range(0,9,3):
            for j in range(0,9,3):
                # 3 x 3 iteration
                for k in range(i,i+3):
                    for l in range(j,j+3):
                        if board[k][l] == '.':
                            continue
                        if board[k][l] in st:
                            return False
                        st.add(board[k][l])
                st.clear()
        return True
                
                
                
        
                
            
        
        
        