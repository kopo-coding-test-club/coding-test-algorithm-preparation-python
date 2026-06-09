
from heapq import heappush, heappop
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        count = Counter(nums)
        result = []
        for val, freq in count.items():
            heappush(heap, (-freq, val))
        for _ in range(k):
            freq , val = heappop(heap)
            result.append(val)
        return result