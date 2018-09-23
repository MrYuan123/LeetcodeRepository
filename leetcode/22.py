class Solution:
    def generateParenthesis(self, n):
        relist = []

        def recurisonfunc(left, right, temp):
            if len(temp) == 2*n:
                relist.append(temp)
                return
            else:
                if left < n:
                    recurisonfunc(left + 1, right, temp + '(')
                if right < left:
                    recurisonfunc(left, right + 1, temp + ')')
            return
        recurisonfunc(0, 0, '')
        return relist


l = Solution()
ans = l.generateParenthesis(10)
print(ans)
