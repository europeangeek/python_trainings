# Given the head of a singly linked list, reverse the list, and return the reversed list.
# example

# original linkeList
# 1 -> 2 -> 3 -> 4 -> 5

# reversed linkedList
# 5 -> 4 -> 3 -> 2 -> 1

# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]

# Input: head = [1,2]
# Output: [2,1]
# Example 3:

# Input: head = []
# Output: []

# Constraints:

# The number of nodes in the list is the range [0, 5000].
# -5000 <= Node.val <= 5000
 

# Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?
class Node:
    def __init__(self, data=None) -> None:
        self.data = data
        self.next = None
        self.previous = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev, curr = None, head
        
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
    
class SolutionRecursive(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        
        new_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        
        return new_head
linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)

lst = [1, 2, 3, 4, 5]
solution = Solution()
print(solution.reverseList(linked_list))

