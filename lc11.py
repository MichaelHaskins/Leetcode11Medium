class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        i = 0
        j = len(height)-1
        max = 0
        while i < j:
            l = height[i]
            r = height[j]
            temp = min(l, r) * (j-i)
            if temp > max:
                max = temp 
            if l > r:
                j -= 1
            else:
                i += 1

        return max