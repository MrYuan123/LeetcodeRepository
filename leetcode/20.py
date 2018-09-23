class Solution:
    def isValid(self, s):
        mystack = []
        sdict = {")":"(","]":"[","}":"{"}
        for item in s:
            if item in sdict.values():
                mystack.append(item)
            elif len(mystack) > 0 and sdict[item] == mystack.pop():
                continue
            else:
                return False

        return not mystack


l = Solution()
ans = l.isValid("([)]")
print(ans)
