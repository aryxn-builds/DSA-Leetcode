class Solution:
    def largestOverlap(self, img1: list[list[int]], img2: list[list[int]]) -> int:
        n = len(img1)

        A = [(r, c) for r in range(n) for c in range(n) if img1[r][c]]
        B = [(r, c) for r in range(n) for c in range(n) if img2[r][c]]

        count = {}
        ans = 0

        for r1, c1 in A:
            for r2, c2 in B:
                shift = (r2 - r1, c2 - c1)
                count[shift] = count.get(shift, 0) + 1
                ans = max(ans, count[shift])

        return ans