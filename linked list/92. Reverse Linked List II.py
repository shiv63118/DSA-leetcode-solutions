class Solution:
    def reverseBetween(self, head, left, right):
        dummy = ListNode(0)
        dummy.next = head

        prev = dummy

        # Move prev to the node before left
        for _ in range(left - 1):
            prev = prev.next

        curr = prev.next

        # Reverse the sublist
        for _ in range(right - left):
            temp = curr.next
            curr.next = temp.next
            temp.next = prev.next
            prev.next = temp

        return dummy.next