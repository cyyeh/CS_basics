# Time:  O(n)
# Space: O(1)

# Initially, there is a Robot at position (0, 0). Given a sequence of its moves,
# judge if this robot makes a circle, which means it moves back to the original place.
#
# The move sequence is represented by a string. And each move is represent by a character.
# The valid robot moves are R (Right), L (Left), U (Up) and D (down).
# The output should be true or false representing whether the robot makes a circle.
#
# Example 1:
# Input: "UD"
# Output: true
# Example 2:
# Input: "LL"
# Output: false

# V0 

# V1 
# http://bookshadow.com/weblog/2017/08/13/leetcode-judge-route-circle/
class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        x = y = 0
        for m in moves:
            if m == 'U': y += 1
            elif m == 'D': y -= 1
            elif m == 'R': x += 1
            elif m == 'L': x -= 1
        return x == y == 0

# V2
class Solution:
    def judgeCircle(self, moves):
        x_move = 1*(moves.count('R')) + (-1)*(moves.count('L'))
        y_move = 1*(moves.count('U')) + (-1)*(moves.count('D'))
        if (x_move == 0  and y_move == 0):
            return True 
        else:
            return False

# V3 
class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        v, h = 0, 0
        for move in moves:
            if move == 'U':
                v += 1
            elif move == 'D':
                v -= 1
            elif move == 'R':
                h += 1
            elif move == 'L':
                h -= 1
        return v == 0 and h == 0