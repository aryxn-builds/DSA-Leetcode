class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        median = median_low(nums)
        return sum(abs(num - median) for num in nums)