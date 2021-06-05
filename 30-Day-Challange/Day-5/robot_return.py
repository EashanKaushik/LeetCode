class Solution:
    def judgeCircle(self, moves: str) -> bool:
        magnitude_y = 0
        magnitude_x = 0
        for move in moves:
            if move == 'U':
                magnitude_y += 1
            elif move =='D':
                magnitude_y -= 1
            elif move == 'R':
                magnitude_x += 1
            else:
                magnitude_x -= 1

        if not magnitude_x and not magnitude_y:
            return True

        return False
                
