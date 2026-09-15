class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        idx=0
        output=0
        while(idx+k<=len(s)):
            if s[idx:idx+k]==s[idx:idx+k][::-1]:
                output+=1
                idx+=k
            elif s[idx:idx+k+1]==s[idx:idx+k+1][::-1]:
                output+=1
                idx+=k+1
            else:
                idx+=1

        return output