class Solution:
    def longestCommonPrefix(self, strs):
        if len(strs) == 1:
            return strs[0]
        elif len(strs) == 0:
            return ''
        else:
            rstr = ''
            for m in range(len(strs[0])):
                for l in strs[1:]:
                    if strs[0][0:m+1] == l[0: m + 1]:
                        pass
                    else:
                        return rstr
                rstr = rstr + strs[0][m]

            return rstr

l = Solution()
ans = l.longestCommonPrefix([''])
print(ans)
