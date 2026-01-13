class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        total = 0
        low = float('inf')
        high = 0
        for x, y, l in squares:
            total += l * l
            low = min(low, y)
            high = max(high, y + l)
        target = total / 2
        def area_below(Y):
            area = 0
            for x, y, l in squares:
                if Y <= y:
                    continue
                elif Y >= y + l:
                    area += l * l
                else:
                    area += l * (Y - y)
            return area
        for _ in range(60):  
            mid = (low + high) / 2
            if area_below(mid) < target:
                low = mid
            else:
                high = mid

        return low