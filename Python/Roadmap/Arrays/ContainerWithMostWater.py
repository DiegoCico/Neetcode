class Solution:
    def maxArea(self, heights: List[int]) -> int:
        best = 0
        right = len(heights) -1
        left = 0
        while True:
            distance = abs(left - right)
            min_height = min(heights[left], heights[right])
            area = distance*min_height
            if best < area: 
                best = area
            
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

            if left == right:
                break
        
        return best 