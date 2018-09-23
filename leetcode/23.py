class Solution:
    def mergeKLists(self, lists):
        firstNode = nowNode = ListNode(0)
        newlists = []
        for m in range(len(lists)):
            if lists[m] != None:
                newlists.append(lists[m])
        lists = newlists
        while len(lists) != 0:
            flag = -1
            num =  100000000
            for m in range(len(lists)):
                if lists[m].val < num:
                    num = lists[m].val
                    flag = m
            tempNode = ListNode(num)
            nowNode.next = tempNode
            nowNode = tempNode
            lists[flag] = lists[flag].next
            if lists[flag] == None:
                del lists[flag]

        return firstNode.next

l = Solution()
ans = l.mergeKLists()
print(ans)
