class Solution:
    def longestValidParentheses(self, s: str) -> int:
        dp = [0] * len(s)
        ans = 0

        for i in range(1, len(s)):
            if s[i] == ')':
                j = i - dp[i - 1] - 1

                if j >= 0 and s[j] == '(':
                    dp[i] = dp[i - 1] + 2
                    if j > 0:
                        dp[i] += dp[j - 1]

                    ans = max(ans, dp[i])

        return ans