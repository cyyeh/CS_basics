# V1  : to do : solve again with regular expression 

# class Solution(object):
# 	def solveEquation(self, equation):
# 		eq = equation.split("=")
# 		left_eq, right_eq = eq[0], eq[1]
# 		sum_constant = sum([ int(i) for i in eq[1] if i.isdigit()]) - [ int(i) for i in eq[0] if i.isdigit()]
# 		sum_var = len([ i for i in eq[0] if i.isalpha()]) - len([ i for i in eq[1] if i.isalpha()])
# 		if sum_var ==0 and sum_constant == 0:
# 			return "Infinite solutions"
# 		elif sum_var ==0 and sum_constant != 0:
# 			return "No solution"
# 		else:
# 			return "x={}".format(int(sum_constant/sum_var))

# V2 
# https://blog.csdn.net/fuxuemingzhu/article/details/80656224
class Solution(object):
    def solveEquation(self, equation):
        """
        :type equation: str
        :rtype: str
        """
        left, right = equation.split('=')
        if left[0] == '-':
            left = '0' + left
        if right[0] == '-':
            right = '0' + right
        left = left.replace('-', '+-')
        right = right.replace('-', '+-')
        left_x, left_val, right_x, right_val = 0, 0, 0, 0
        for num in left.split('+'):
            if 'x' in num:
                if num == 'x':
                    left_x += 1
                elif num == '-x':
                    left_x -= 1
                else:
                    left_x += int(num[:-1])
            else:
                left_val += int(num)
        for num in right.split('+'):
            if 'x' in num:
                if num == 'x':
                    right_x += 1
                elif num == '-x':
                    right_x -= 1
                else:
                    right_x += int(num[:-1])
            else:
                right_val += int(num)
        left_x -= right_x
        right_val -= left_val
        if left_x != 0 and right_val == 0:
            return "x=0"
        elif left_x != 0 and right_val != 0:
            return 'x=' + str(right_val / left_x)
        elif left_x == 0 and right_val == 0:
            return "Infinite solutions"
        elif left_x == 0 and right_val != 0:
            return "No solution"

# V3 
# Time:  O(n)
# Space: O(n)
import re
class Solution(object):
    def solveEquation(self, equation):
        """
        :type equation: str
        :rtype: str
        """
        a, b, side = 0, 0, 1
        for eq, sign, num, isx in re.findall('(=)|([-+]?)(\d*)(x?)', equation):
            if eq:
                side = -1
            elif isx:
                a += side * int(sign + '1') * int(num or 1)
            elif num:
                b -= side * int(sign + num)
        return 'x=%d' % (b / a) if a else 'No solution' if b else 'Infinite solutions'

