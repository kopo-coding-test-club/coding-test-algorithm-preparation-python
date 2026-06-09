from heapq import heappush, heappop
class MedianFinder:

    def __init__(self):
        self.max_heap = []#전체 숫자 중 작은 절반의 값
        #이 중 가장 큰 값(중앙 값 근처)이 항상 루트에 와야 함
        self.min_heap = []#전체 숫자 중 큰 절반의 값
        #이 중 가장 작은 값(중앙 값 근처)이 항상 루트에 와야 함
        #한쪽으로 쏠리지 않아 가운데에 중간값이 맞대어 있는 상태로 유지
    def addNum(self, num: int) -> None:
        heappush(self.max_heap, -num)
        heappush(self.min_heap, -heappop(self.max_heap))
        if len(self.min_heap) > len(self.max_heap):
            heappush(self.max_heap, -heappop(self.min_heap))

    def findMedian(self) -> float:
        if len(self.max_heap) == len(self.min_heap):
            return (self.min_heap[0] + (-self.max_heap[0])) / 2.0
        return float(-self.max_heap[0])
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()