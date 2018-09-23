class Solution:
    def isPalindrome(self, x):
        x = str(x)
        head = 0
        end = len(x) -1
        while end - head > 0:
            if x[head] == x[end]:
                head += 1
                end -= 1
            else:
                return False

        return True

l = Solution()
ans = l.isPalindrome(1234567890987654321)
print(ans)
