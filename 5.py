class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode()
        current = dummy

        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        if list1:
            current.next = list1
        elif list2:
            current.next = list2

        return dummy.next

def list_to_linkedlist(lst):
    dummy = ListNode()
    current = dummy
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return dummy.next


list1 = list_to_linkedlist([1, 2, 4])
list2 = list_to_linkedlist([1, 3, 4])

solution_instance = Solution()
result = solution_instance.mergeTwoLists(list1, list2)


def linkedlist_to_list(node):
    result_list = []
    while node:
        result_list.append(node.val)
        node = node.next
    return result_list

print(linkedlist_to_list(result))  
