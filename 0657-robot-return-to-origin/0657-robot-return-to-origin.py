class Solution:
    def judgeCircle(self, moves: str) -> bool:
        vertical = 0
        horizontal = 0
        for x in moves:
            match x:
                case 'U':
                    vertical += 1
                case 'D':
                    vertical -= 1
                case 'R':
                    horizontal += 1
                case 'L':
                    horizontal -= 1
        if vertical == 0 and horizontal == 0:
            return True
        return False