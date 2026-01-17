class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        n = len(bottomLeft)
        max_side = 0

        for i in range(n):
            x1, y1 = bottomLeft[i]
            x2, y2 = topRight[i]

            for j in range(i + 1, n):
                xi, yi = bottomLeft[j]
                xj, yj = topRight[j]

                # compute intersection
                inter_left = max(x1, xi)
                inter_bottom = max(y1, yi)
                inter_right = min(x2, xj)
                inter_top = min(y2, yj)

                width = inter_right - inter_left
                height = inter_top - inter_bottom

                if width > 0 and height > 0:
                    side = min(width, height)
                    max_side = max(max_side, side)

        return max_side * max_side