class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        events = []
        for x, y, l in squares:
            events.append((y, x, x + l, 1))     
            events.append((y + l, x, x + l, -1)) 
        events.sort()
        def get_width(intervals):
            if not intervals:
                return 0
            intervals.sort()
            width = 0
            start, end = intervals[0]
            for s, e in intervals[1:]:
                if s > end:
                    width += end - start
                    start, end = s, e
                else:
                    end = max(end, e)
            width += end - start
            return width
        active = []
        total_area = 0
        prev_y = events[0][0]
        for y, x1, x2, typ in events:
            height = y - prev_y
            if height > 0:
                total_area += get_width(active) * height
            if typ == 1:
                active.append((x1, x2))
            else:
                active.remove((x1, x2))
            prev_y = y
        half = total_area / 2
        active = []
        area = 0
        prev_y = events[0][0]
        for y, x1, x2, typ in events:
            height = y - prev_y
            if height > 0:
                width = get_width(active)
                band_area = width * height
                if area + band_area >= half:
                    return prev_y + (half - area) / width
                area += band_area
            if typ == 1:
                active.append((x1, x2))
            else:
                active.remove((x1, x2))
            prev_y = y