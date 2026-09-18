class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        first = {c: s.index(c) for c in set(s)}
        last = {c: s.rindex(c) for c in set(s)}
        a = []

        for c in first:
            l, r = first[c], last[c]
            i = l
            while i <= r:
                if first[s[i]] < l:
                    break
                r = max(r, last[s[i]])
                i += 1
            else:
                a.append((r, l))

        a.sort()
        ans, end = [], -1

        for r, l in a:
            if l > end:
                ans.append(s[l:r + 1])
                end = r

        return ans