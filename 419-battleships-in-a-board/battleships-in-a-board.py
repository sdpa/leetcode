class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        count = 0
        rows = len(board)
        cols = len(board[0])

        def isAdjacent(r, c):
            return r >= 0 and c >= 0 and r < rows and c < cols and board[r][c] == 'X'


        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'X':
                    # Check if its start of a new battleship -> 
                    # If it has an adjacent one. Check only left and top. 
                    existing = isAdjacent(r-1, c) or isAdjacent(r, c-1)

                    print(existing)
                    if not existing:
                        count += 1

        return count

             

                