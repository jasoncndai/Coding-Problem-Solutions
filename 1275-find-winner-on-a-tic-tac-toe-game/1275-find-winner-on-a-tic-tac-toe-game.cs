public class Solution {
    public string Tictactoe(int[][] moves) {
        // for n x n board, change n to any size
        int n = 3;
        int[] col = new int[n];
        int[] row = new int[n];
        int diag1 = 0;
        int diag2 = 0;
        // A is 1, B is -1
        int currPlayer = 1;
        
        foreach (int[] move in moves) {
            row[move[0]] += currPlayer;
            col[move[1]] += currPlayer;
            diag1 = move[0] == move[1] ? diag1 + currPlayer : diag1;
            diag2 = move[0] + move[1] == n-1 ? diag2 + currPlayer : diag2;
            
            if (Math.Abs(row[move[0]]) == n || Math.Abs(col[move[1]]) == n || Math.Abs(diag1) == n || Math.Abs(diag2) == n ){
                return currPlayer == 1 ? "A" : "B";
            }
                
            currPlayer *= -1;
        }
        
        return moves.Length < n * n ? "Pending" : "Draw";
    }
}