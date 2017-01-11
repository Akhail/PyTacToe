# Threex
Tic-tac-toe (also known as noughts and crosses or Xs and Os) is a paper-and-pencil game for two players, X and O, who take 
turns marking the spaces in a 3×3 grid. 
The player who succeeds in placing three of their marks in a horizontal, vertical, or diagonal row wins the game.
Players soon discover that best play from both parties leads to a draw. Hence, Tic-tac-toe is most often played by young 
children.

Because of the simplicity of tic-tac-toe, it is often used as a pedagogical tool for teaching the concepts of
 good sportsmanship and the branch of artificial intelligence that deals with the searching of game trees. 
 It is straightforward to write a computer program to play tic-tac-toe perfectly, 
 to enumerate the 765 essentially different positions (the state space complexity), 
or the 26,830 possible games up to rotations and reflections (the game tree complexity) on this space.

## Algorithm: Minimax
is a decision rule used in decision theory, game theory, statistics and philosophy for minimizing the possible loss 
for a worst case (maximum loss) scenario. Originally formulated for two-player zero-sum game theory, covering both the 
cases where players take alternate moves and those where they make simultaneous moves, 
it has also been extended to more complex games and to general decision-making in the presence of uncertainty.

**Pseudo-Code**

    function minimax(node, depth, maximizingPlayer)
        if depth = 0 or node is a terminal node
            return the heuristic value of node
        if maximizingPlayer
            bestValue := −∞
            for each child of node
                v := minimax(child, depth − 1, FALSE)
                bestValue := max(bestValue, v)
            return bestValue
        else    (* minimizing player *)
            bestValue := +∞
            for each child of node
                v := minimax(child, depth − 1, TRUE)
                bestValue := min(bestValue, v)
            return bestValue