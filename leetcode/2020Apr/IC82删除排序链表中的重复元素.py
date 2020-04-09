# Definition for singly-linked list.
'''

给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中 没有重复出现 的数字。

示例 1:

输入: 1->2->3->3->4->4->5
输出: 1->2->5
示例 2:

输入: 1->1->1->2->3
输出: 2->3

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

'''


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def deleteDuplicates(self, head):
        map = {}
        if head is not None:
            map[head.val] = 1
        else:
            return head
        n = head.next

        while n is not None:
            if n.val in map:
                map[n.val] = map[n.val] + 1
            else:
                map[n.val] = 1
            n = n.next
        print(map)

        before = head
        current = head.next
        while current is not None:
            if map[current.val] > 1:
                before.next = current.next
            else:
                before = before.next
            current = current.next
        if map[head.val] > 1:
            head = head.next
        return head


if __name__ == "__main__":
    head = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(3)
    n5 = ListNode(4)
    n6 = ListNode(4)
    n7 = ListNode(5)

    head.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = n6
    n6.next = n7

    s = Solution()
    s.deleteDuplicates(head)
