# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from heapq import heappush , heappop
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy
        heap = []
        #i는 같은 값 구분하기 위한 인덱스
        for i , list in enumerate(lists):
            if list:
                heappush(heap, (list.val, i , list))
        while heap:
            val, i, node = heappop(heap)
            curr.next = node
            curr = curr.next
            if node.next:
                heappush(heap,(node.next.val, i, node.next))
        return dummy.next

        