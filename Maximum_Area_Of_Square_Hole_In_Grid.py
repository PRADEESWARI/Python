class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        def max_gap(bars):
            bars.sort()
            longest = 1
            current = 1
            for i in range(1, len(bars)):
                if bars[i] == bars[i - 1] + 1:
                    current += 1
                    longest = max(longest, current)
                else:
                    current = 1
            return longest + 1  
        max_height = max_gap(hBars)
        max_width = max_gap(vBars)
        side = min(max_height, max_width)
        return side * side