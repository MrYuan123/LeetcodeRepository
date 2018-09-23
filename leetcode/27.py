class Solution:
    def removeElement(self, nums, val):
        while val in nums:
            nums.remove(val)
        return len(nums)

l = Solution()
ans = l.removeElement()
print(ans)
