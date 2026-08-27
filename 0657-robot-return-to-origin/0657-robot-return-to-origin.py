class Solution:
    def judgeCircle(self, moves: str) -> bool:
        # The robot returns to origin if 'U' equals 'D' and 'L' equals 'R'
        return moves.count('U') == moves.count('D') and moves.count('L') == moves.count('R')