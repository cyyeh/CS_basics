# V0 

# V1 
# http://bookshadow.com/weblog/2015/06/26/leetcode-summary-ranges/
class Solution:
    # @param {integer[]} nums
    # @return {string[]}
    def summaryRanges(self, nums):
        x, size = 0, len(nums)
        ans = []
        while x < size:
            c, r = x, str(nums[x])
            while x + 1 < size and nums[x + 1] - nums[x] == 1:
                x += 1
            if x > c:
                r += "->" + str(nums[x])
            ans.append(r)
            x += 1
        return ans

# V1' 
# http://bookshadow.com/weblog/2015/06/26/leetcode-summary-ranges/
# IDEA : COLLECT THE RANGES, FORMTAT AND RETURN THEM 
def summaryRanges(self, nums):
    ranges = []
    for n in nums:
        if not ranges or n > ranges[-1][-1] + 1:
            ranges += [],
        ranges[-1][1:] = n,
    return ['->'.join(map(str, r)) for r in ranges]

# V1'' 
# http://bookshadow.com/weblog/2015/06/26/leetcode-summary-ranges/
# IDEA : A variation of solution 1', holding the current range in an extra variable r to make things easier.
def summaryRanges(self, nums):
    ranges = []
    for n in nums:
        if not ranges or n > ranges[-1][-1] + 1:
            ranges += [],
        ranges[-1][1:] = n,
    return ['->'.join(map(str, r)) for r in ranges]

# V1''' 
# http://bookshadow.com/weblog/2015/06/26/leetcode-summary-ranges/
def summaryRanges(self, nums):
    ranges = r = []
    for n in nums:
        if `n-1` not in r:
            r = []
            ranges += r,
        r[1:] = `n`,
    return map('->'.join, ranges)

# V2 
# Time:  O(n)
# Space: O(1)
import itertools
import re
class Solution(object):
    # @param {integer[]} nums
    # @return {string[]}
    def summaryRanges(self, nums):
        ranges = []
        if not nums:
            return ranges

        start, end = nums[0], nums[0]
        for i in range(1, len(nums) + 1):
            if i < len(nums) and nums[i] == end + 1:
                end = nums[i]
            else:
                interval = str(start)
                if start != end:
                    interval += "->" + str(end)
                ranges.append(interval)
                if i < len(nums):
                    start = end = nums[i]

        return ranges

# Time:  O(n)
# Space: O(n)
class Solution2(object):
    # @param {integer[]} nums
    # @return {string[]}
    def summaryRanges(self, nums):
        return [re.sub('->.*>', '->', '->'.join(repr(n) for _, n in g))
            for _, g in itertools.groupby(enumerate(nums), lambda i_n: i_n[1]-i_n[0])]
