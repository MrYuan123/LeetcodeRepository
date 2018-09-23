# class Solution:
#     def swapPairs(self, head):
#         return recursion(head)
#
#     def recursion(self, head):
#         if !head or !head.next:
#             return head
#         else:
#             x= head.next
#             head.next = recursion(head.next.next)
#             x.next = head
#             return x

# solution2
class Solution:
    def swapPairs(self, head):
        temp = ListNode(0)
        temp.next = head
        current = temp
        while current.next and current.next.next:
            now = current.next
            further = current.next.next
            now.next = further.next
            current.next = further
            further.next = now
            current = current.next.next

        return temp.next

l = Solution()
ans = l.swapPairs()
print(ans)


        dummy = ListNode(0)
        dummy.next = head
        curr = dummy
        while curr.next and curr.next.next:
            first = curr.next
            second = curr.next.next
            first.next = second.next
            curr.next = second
            second.next = first
            curr = curr.next.next
        return dummy.next
