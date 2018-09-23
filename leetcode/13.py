# solution 1
# class Solution:
#     def romanToInt(self, s):
#         d = {'I':1, 'IV':4, 'V':5, 'IX':9, 'X':10, 'XL':40, 'L':50, 'XC':90, 'C':100, 'CD':400, 'D':500, 'CM':900, 'M':1000}
#         sum = 0
#         m = 0
#         while m < len(s) - 1:
#             if d.get(s[m] + s[m+1]):
#                 sum = sum + d[s[m] + s[m+1]]
#                 # print('2: '+ s[m] + s[m+1])
#                 m += 2
#             else:
#                 sum = sum + d[s[m]]
#                 # print('1: '+ s[m])
#                 m += 1
#         if m == len(s) - 1:
#             sum = sum + d[s[m]]
#
#         return sum

# solution 2
class Solution:
    def romanToInt(self, s):
        d = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500,'M':1000}
        sum = 0
        s = s[::-1]
        sum = d[s[0]]
        for m in range(1,len(s)):
            if d[s[m]] <d[s[m-1]]:
                sum -= d[s[m]]
            else:
                sum += d[s[m]]
        return sum

l = Solution()
ans = l.romanToInt("MCMXCIV")
print(ans)
