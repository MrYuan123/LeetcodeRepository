class Solution:
    def removeDuplicates(self, nums):
        if len(nums) == 0:
            return
        i = 0
        for m in range(1,len(nums)):
            if nums[m] != nums[i]:
                nums[i+1]=nums[m]
                i+=1
        return i+1

l = Solution()
ans = l.removeElement([0,1,2,2,3,0,4,2])
print(ans)
