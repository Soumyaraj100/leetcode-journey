class Solution(object):
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            width = right - left

            if height[left] < height[right]:
                current_height = height[left]
            else:
                current_height = height[right]

            area = width * current_height

            if area > max_area:
                max_area = area

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area