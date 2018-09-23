# sort the rows
# class Solution:
#     def convert(self, s, numRows):
#         if numRows == 1:
#             print(s)
#         nlist = [""]*numRows
#         flag = 0
#         dire = 0
#         for m in range(len(s)):
#             nlist[flag] = nlist[flag] + s[m]
#             if dire == 0:
#                 if flag == numRows-1:
#                     dire = 1
#                     flag -= 1
#                 else:
#                     flag += 1
#             else:
#                 if flag == 0:
#                     dire = 0
#                     flag += 1
#                 else:
#                     flag -= 1
#
#         return ''.join(nlist)

# Finding the characters
class Solution:
    def convert(self, s, numRows):
        if numRows == 1:
            return s
        nlist = ['']*numRows
        for m in range(numRows):
            if m == 0:
                flag = 0
                while flag*(2*numRows - 2) < len(s):
                    nlist[m] = nlist[m] + s[flag*(2*numRows - 2)]
                    flag += 1

            elif m == numRows -1:
                flag = 0
                while (flag*(2*numRows - 2) + numRows - 1) < len(s):
                    nlist[m] = nlist[m] + s[flag*(2*numRows - 2) + numRows - 1]
                    flag += 1

            else:
                flag = 0
                while (flag*(2*numRows-2) + m) < len(s) or ((flag + 1)*(2*numRows - 2) - m) < len(s):
                    if (flag*(2*numRows-2) + m) < len(s):
                        nlist[m] = nlist[m] + s[flag*(2*numRows-2) + m]
                    if ((flag + 1)*(2*numRows - 2) - m) < len(s):
                        nlist[m] = nlist[m] + s[(flag + 1)*(2*numRows - 2) - m]

                    flag += 1

        return ''.join(nlist)


l = Solution()
ans = l.convert("PAYPALISHIRING", 3)
print(ans)
