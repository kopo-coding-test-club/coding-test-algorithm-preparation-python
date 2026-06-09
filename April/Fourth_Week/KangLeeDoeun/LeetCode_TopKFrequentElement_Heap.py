from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        top = counts.most_common(k)
        return [i for i, j in top]
        