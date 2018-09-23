class Solution:
    def letterCombinations(self, digits):
        intger_char = {
        '0':[],
        '1':[],
        '2':['a','b','c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']
        }

        if len(digits) == 0:
            return [""]
        else:
            rlist = intger_char[digits[0]]
            for num in digits[1:]:
                temp = []
                for m in intger_char[num]:
                    for item in rlist:
                        temp.append(item + m)
                rlist = temp
        return rlist

l = Solution()
ans = l.letterCombinations("23444")
print(ans)
