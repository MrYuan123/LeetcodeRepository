# brute force
# class Solution:
#     def longestPalindrome(self, s):
#         if len(s) == 0:
#             return s
#         elif len(s) == 1:
#             return s
#         else:
#             substring = ''
#             for m in range(len(s)):
#                 for n in range(m+1,len(s)+1):
#                     flag = self.whetherpa(s[m:n])
#                     if flag == 1 and len(s[m:n]) > len(substring):
#                         substring = s[m:n]
#
#             return substring
#
#     def whetherpa(self, m):
#         l = m[::-1]
#         if l == m:
#             return 1
#         else:
#             return 0

# dynamic programming
class Solution:
    def longestPalindrome(self, s):
        substring = ''
        for m in range(len(s)):
            returnstring = self.findstring(s,m,m)

            if len(returnstring) > len(substring):
                substring = returnstring

            returnstring = self.findstring(s,m,m+1)
            if len(returnstring) > len(substring):
                substring = returnstring

        return substring

    def findstring(self, s, p, q):
        while p > -1 and q <len(s) and s[p] == s[q]:
            p -= 1
            q += 1

        return s[p+1:q]


l = Solution()
answer = l.longestPalindrome('sdbffdsfwesdasdfghgfdsa')
print(answer)
