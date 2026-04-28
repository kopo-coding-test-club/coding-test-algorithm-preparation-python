class MaxHeap:
  def __init__(self):
    self.heap = []
  
  def up_heapify(self, index):
    child_index = index
    while child_index != 0:
      parent_index = (child_index - 1) // 2
      # 부모보다 자식이 더 크면 교환 (Max Heap 조건)
      if self.heap[parent_index] < self.heap[child_index]:
          self.heap[parent_index], self.heap[child_index] = self.heap[child_index], self.heap[parent_index]
          child_index = parent_index
      else:
          return
  
  # [삭제 과정 1: 더 큰 자식의 인덱스 찾기]      
  def find_bigger_child_index(self, index, heap_size):
        parent = index
        left_child = (parent * 2) + 1
        right_child = (parent * 2) + 2

        # 왼쪽 자식이 있고, 부모보다 크다면 갱신
        if left_child < heap_size and self.heap[parent] < self.heap[left_child]:
            parent = left_child
        # 오른쪽 자식이 있고, 현재까지 가장 큰 노드보다 크다면 갱신
        if right_child < heap_size and self.heap[parent] < self.heap[right_child]:
            parent = right_child
        
        return parent
      
  # [삭제 과정 2: 루트 삭제 후 재구조화]
  def down_heapify(self, index):
      parent_index = index
      bigger_child_index = self.find_bigger_child_index(parent_index, len(self.heap))
        
        # 더 큰 자식이 존재할 때까지 반복해서 교체
      while parent_index != bigger_child_index:
          self.heap[parent_index], self.heap[bigger_child_index] = self.heap[bigger_child_index], self.heap[parent_index]
          parent_index = bigger_child_index
          bigger_child_index = self.find_bigger_child_index(parent_index, len(self.heap))
          
  def insert(self, value):
      self.heap.append(value)
      self.up_heapify(len(self.heap) - 1)
        
  def pop(self):
      if not self.heap:
          return None
      
      # 1. 루트 노드 저장
      root_value = self.heap[0]
      
      # 2. 말단 노드를 루트로 이동
      last_node = self.heap.pop()
      
      if self.heap:
          self.heap[0] = last_node
          # 3. 아래로 재구조화
          self.down_heapify(0)
          
      return root_value
  
  