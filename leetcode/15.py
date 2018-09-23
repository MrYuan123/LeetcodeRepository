class Solution:
    def threeSum(self, nums):
        if len(nums) == 0:
            return []
        else:
            retset = []
            # ===================
            # progress part
            # ===================
            nums = sorted(nums)
            head = 0

            while head < len(nums) - 2:
                end = len(nums) - 1
                while end > head + 1:
                    if head != 0 and nums[head] == nums[head-1]:
                        break
                    m = 0 - (nums[end] + nums[head])
                    if m in nums[head + 1: end]:
                        if [nums[head] ,m , nums[end]] not in retset:
                            print('1 %d : %d'%(nums[head], nums[end]))
                            retset.append([nums[head] ,m , nums[end]])
                        end -= 1
                    elif nums[end] - nums[head] > 0:
                        print('1 %d : %d'%(nums[head], nums[end]))
                        end -= 1
                    else:
                        head += 1
                head += 1
                if nums[head] > 0:
                    break
            return retset

            # ==========================
            # brute force algorithm part
            # ==========================

            # nums = sorted(nums)
            # for m in range(0, len(nums) - 2):
            #     for n in range( m + 1, len(nums) - 1):
            #         if 0 - (nums[m] + nums[n]) in nums[n+1 : len(nums)]:
            #             temp = sorted([nums[m], nums[n], 0 - nums[m] - nums[n]])
            #             if temp  not in retset:
            #                 retset.append(temp)
            # return retset



l = Solution()
ans = l.threeSum([-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6])
# [-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]
print(ans)
