# Definition for singly-linked list.
# Merge Two Sorted Lists

# l1 = [1,2,4], l2 = [1,3,4]
# output = [1,1,2,3,4,4]


def mergeTwoLists(list1, list2):
    dummy = ListNode(0)
    current = dummy

    while list1 and list2:
        if list1.val > list2.val:
            current.next = list2
            current = list2
            list2 = list2.next
        else:
            current.next = list1
            current = list1
            list1 = list1.next
    if list1:
        current.next = list1
    else:
        current.next = list2
    
    return dummy.next

list1 = [1,2,4]
list2 = [1,3,4]
print(mergeTwoLists(list1, list2))  # Output: [1,1,2,3,4,4]

# Time Complexity: O(n + m)
# Space Complexity: O(1)




    
    
    
