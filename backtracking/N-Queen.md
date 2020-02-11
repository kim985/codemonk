# N-Queen

" Given a chess board having cells, you need to place N queens on the board in such a way that no queen attacks any other queen."

- Input: The only line of input consists of a single integer denoting N.

- Output: If it is possible to place all the N queens in such a way that no queen attacks another queen, then print "YES" (without quotes) in first line, then print N lines having N integers. The integer in line and column will denote the cell of the board and should be 1 if a queen is placed at otherwise 0. If there are more than way of placing queens print any of them. If it is not possible to place all N queens in the desired way, then print "NO" (without quotes).

- Constraints: 1<=N<=10

# Pseudocode

    is_attacked( x, y, board[][], N)
        //checking for row and column
        if any cell in xth row is 1
            return true
        if any cell in yth column is 1
            return true
    
        //checking for diagonals
        if any cell (p, q) having p+q = x+y is 1          
            return true
        if any cell (p, q) having p-q = x-y is 1
            return true
        return false
    
    
    N-Queens( board[][], N )
        if N is 0                     //All queens have been placed
            return true
        for i = 1 to N {
            for j = 1 to N {
                if is_attacked(i, j, board, N) is true
                    skip it and move to next cell
                board[i][j] = 1            //Place current queen at cell (i,j)
                if N-Queens( board, N-1) is true    // Solve subproblem
                    return true                   // if solution is found return true
                board[i][j] = 0            /* if solution is not found undo whatever changes 
                                           were made i.e., remove  current queen from (i,j)*/
            }
        }
        return false
