class Solution:
    def maxArea(self, height):
        maxn = 0
        head = 0
        end = len(height) - 1
        while end - head> 0:
            print('%d : %d'% (head,end))
            if (end - head) * min(height[head], height[end]) > maxn:
                maxn = (end - head) * min(height[head], height[end])
            if height[head] < height[end]:
                head += 1
            else:
                end -= 1
        return maxn


l = Solution()
ans = l.maxArea([1,8,6,2,5,4,8,3,7])
print(ans)
