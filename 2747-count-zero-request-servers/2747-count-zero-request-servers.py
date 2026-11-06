
class Solution:
    def countServers(self, n, logs, x, queries):
        logs.sort(key=lambda a: a[1])
        q = sorted((t, i) for i, t in enumerate(queries))

        freq = {}
        ans = [0] * len(queries)
        l = r = 0

        for t, i in q:
            while r < len(logs) and logs[r][1] <= t:
                s = logs[r][0]
                freq[s] = freq.get(s, 0) + 1
                r += 1

            while l < r and logs[l][1] < t - x:
                s = logs[l][0]
                freq[s] -= 1
                if freq[s] == 0:
                    del freq[s]
                l += 1

            ans[i] = n - len(freq)

        return ans
