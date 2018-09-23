class Solution:
    def threeSumClosest(self, numbers, target):
        numbers = sorted(numbers)
        retans = None
        for m in range(len(numbers)):
            left = m + 1
            right = len(numbers) - 1
            while left < right:
                sum = numbers[left] + numbers[right] + numbers[m]
                if retans is None or abs(retans - target) >abs(sum - target):
                    retans = sum
                if sum <target:
                    left += 1
                else:
                    right -= 1
        return retans


l = Solution()
ans = l.threeSumClosest([-1, 2, 1, -4], 1)
print(ans)
