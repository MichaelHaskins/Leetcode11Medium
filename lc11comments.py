class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        #i and j are two pointers on opposite sides of the array
        i = 0
        j = len(height)-1
        max = 0
        #end loop when i = j
        while i < j:
            #left and right values
            l = height[i]
            r = height[j]
            #temp area calculation
            #min of l and r is the height and j-i is the length
            temp = min(l, r) * (j-i)
            #update max if new max is found
            if temp > max:
                max = temp
            #determine which pointer to increment/decrement
            if l > r:
                j -= 1
            else:
                i += 1

        return max