from typing import List

class Solution:
    def sortableIntegers(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0

        for k in range(1, n + 1):
            if n % k:
                continue

            prev = float('-inf')
            ok = True

            for i in range(0, n, k):
                a = nums[i:i + k]
                drops = [j for j in range(k - 1) if a[j] > a[j + 1]]

                if len(drops) > 1:
                    ok = False
                    break

                if drops:
                    j = drops[0]
                    if a[-1] > a[0]:
                        ok = False
                        break
                    a = a[j + 1:] + a[:j + 1]

                if a[0] < prev:
                    ok = False
                    break

                prev = a[-1]

            if ok:
                ans += k

        return ans