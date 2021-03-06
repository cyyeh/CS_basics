# V0

# V1
# https://www.hrwhisper.me/leetcode-range-sum-query-mutable/
class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.sum_array = [0] * (len(nums) + 1)
        self.nums = nums
        self.n = len(nums)
        for i in range(len(nums)):
            self.add(i + 1,nums[i])
 
 
    def add(self,x,val):
        while x <= self.n:
            self.sum_array[x] += val
            x += self.lowbit(x)
 
 
    def lowbit(self,x):
        return x & -x
 
    def sum(self,x):
        res = 0
        while x >0:
            res += self.sum_array[x]
            x -= self.lowbit(x)
        return res
 
    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: int
        """
        self.add(i + 1, val - self.nums[i])
        self.nums[i] = val
 
    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        if not self.nums: return  0
        return self.sum(j+1) - self.sum(i)

# V2 
# Time:  ctor:   O(n),
#        update: O(logn),
#        query:  O(logn)
# Space: O(n)
class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        if not nums:
            return
        self.__nums = nums
        self.__bit = [0] * (len(self.__nums) + 1)
        for i in range(1, len(self.__bit)):
            self.__bit[i] = nums[i-1] + self.__bit[i-1]

        for i in reversed(range(1, len(self.__bit))):
            last_i = i - (i & -i)
            self.__bit[i] -= self.__bit[last_i]

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: int
        """
        if val - self.__nums[i]:
            self.__add(i, val - self.__nums[i])
            self.__nums[i] = val

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.__sum(j) - self.__sum(i-1)

    def __sum(self, i):
        i += 1
        ret = 0
        while i > 0:
            ret += self.__bit[i]
            i -= (i & -i)
        return ret

    def __add(self, i, val):
        i += 1
        while i <= len(self.__nums):
            self.__bit[i] += val
            i += (i & -i)


# Time:  ctor:   O(n),
#        update: O(logn),
#        query:  O(logn)
# Space: O(n)
# Segment Tree solutoin.
class NumArray2(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        # Build segment tree.
        self.__nums = nums
        def buildHelper(nums, start, end):
            if start > end:
                return None

            # The root's start and end is given by build method.
            root = self._SegmentTreeNode(start, end, 0)

            # If start equals to end, there will be no children for this node.
            if start == end:
                root.sum = nums[start]
                return root

            # Left child: start=nums.left, end=(nums.left + nums.right) / 2.
            root.left = buildHelper(nums, start, (start + end) / 2)

            # Right child: start=(nums.left + nums.right) / 2 + 1, end=nums.right.
            root.right = buildHelper(nums, (start + end) / 2 + 1, end)

            # Update sum.
            root.sum = (root.left.sum if root.left else 0) + \
                       (root.right.sum if root.right else 0)
            return root

        self.__root = buildHelper(nums, 0, len(nums) - 1)

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: int
        """
        def updateHelper(root, i, val):
            # Out of range.
            if not root or root.start > i or root.end < i:
                return

            # Change the node's value with [i] to the new given value.
            if root.start == i and root.end == i:
                root.sum = val
                return

            updateHelper(root.left, i, val)
            updateHelper(root.right, i, val)

            # Update sum.
            root.sum =  (root.left.sum if root.left else 0) + \
                        (root.right.sum if root.right else 0)
        if self.__nums[i] != val:
            self.__nums[i] = val
            updateHelper(self.__root, i, val)

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        def sumRangeHelper(root, start, end):
            # Out of range.
            if not root or root.start > end or root.end < start:
                return 0
            # Current segment is totally within range [start, end]
            if root.start >= start and root.end <= end:
                return root.sum
            return sumRangeHelper(root.left, start, end) + \
                   sumRangeHelper(root.right, start, end)

        return sumRangeHelper(self.__root, i, j)

    class _SegmentTreeNode:
        def __init__(self, i, j, s):
            self.start, self.end, self.sum = i, j, s