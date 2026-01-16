class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        MOD = 10**9 + 7

        # add boundaries
        h = [1] + sorted(hFences) + [m]
        v = [1] + sorted(vFences) + [n]

        # get all possible heights
        heights = set()
        for i in range(len(h)):
            for j in range(i + 1, len(h)):
                heights.add(h[j] - h[i])

        # get all possible widths
        widths = set()
        for i in range(len(v)):
            for j in range(i + 1, len(v)):
                widths.add(v[j] - v[i])

        # find common maximum
        common = heights.intersection(widths)

        if not common:
            return -1

        side = max(common)

        return (side * side) % MOD