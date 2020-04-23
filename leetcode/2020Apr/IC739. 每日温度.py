class node(object):
    def __init__(self, val, index):
        self.val = val
        self.index = index
        self.next = None

class Solution(object):
    def InsertIntoLinkedList(self, root, node):
        if root is None:
            root = node
            return root
        current = root
        next = current.next
        if node.val <= current.val: # append ahead
                node.next = current
                return node
        while next is not None:
            if node.val <= next.val:
                current.next = node
                node.next = next
                return root
            current = next
            next = next.next
        current.next = node
        return root

    def SearchFromLinkedList(self, root, node):
        if root is None:
            return 0
        while root is not None:
            if node.val < root.val:
                return root.index - node.index
            root = root.next
        return 0
                
    def dailyTemperatures(self, T):
        root = None
        result = []
        for i in range(len(T)-1,-1,-1):
            n = node(T[i],i)
            days = self.SearchFromLinkedList(root,n)
            result.append(days)
            root = self.InsertIntoLinkedList(root,n)
        result.reverse()
        return result


if __name__ == '__main__':
    s = Solution()
    s.dailyTemperatures([73,74,75,71,69,72,76,73])
