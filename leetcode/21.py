class Solution:
    def mergeTwoLists(self, l1, l2):
        ListNode startNode
        ListNode nowNode
        startNode = nowNode
        while l1 or l2:
            if l1.val <l2.val:
                ListNode nown
                nown.val = l1.val
                nowNode.next = nown
                l1 = l1.next
            else:
                ListNode nown
                nown.val = l2.val
                nowNode.next = nown
                nowNode = nown
                l2 = l2.next
        return nowNode.next

l = Solution()
ans = l.mergeTwoLists()
print(ans)
