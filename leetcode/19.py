class Solution:
    def removeNthFromEnd(self, head, n):
        temp = head
        mlist = []
        while temp != None:
            mlist.append(temp.val)
            temp = temp.next

        return mlist.remove(len(mlist) - n)

l = Solution()
ans = l.removeNthFromEnd()
print(ans)
