class Solution:
    def minMoves(self, a: List[int]) -> int:
        return max(a)*len(a)-sum(a)