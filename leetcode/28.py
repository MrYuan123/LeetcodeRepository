class Solution:
    def strStr(self, haystack, needle):
        for m in range(len(haystack) - len(needle) + 1):
            if haystack[m : m + len(needle)] == needle:
                return m
        return -1


l = Solution()
ans = l.strStr("aaaaa", "bba")
print(ans)
