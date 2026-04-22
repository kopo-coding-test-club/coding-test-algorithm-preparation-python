class CircleQueue:
  rear = 0
  front = 0
  MAX_SIZE = 100
  queue = list()
  
  def __init__(self):
    self.rear = 0
    self.front = 0
    self.queue = [0 for i in range(self.MAX_SIZE)]
  
  def is_empty(self):
    return self.rear == self.front
  
  def is_full(self):
    return (self.rear + 1) % self.MAX_SIZE == self.front
  
  def enqueue(self,data):
    if self.is_full():
      raise Exception("Queue is full")
    
    self.rear = (self.rear + 1) % self.MAX_SIZE
    self.queue[self.rear] = data
  
  def dequeue(self):
    if self.is_empty():
      raise Exception("Queue is empty")
    
    self.front = (self.front + 1) % self.MAX_SIZE
    data = self.queue[self.front]
    
    return data
  
  def peek(self):
    if self.is_empty():
      raise Exception("Queue is empty")
    data = self.queue[(self.front + 1) % self.MAX_SIZE]
    return data
  
  def print(self):
    if self.is_empty():
      raise Exception("Queue is empty")
    
    while True:
      self.front = (self.front + 1) % self.MAX_SIZE
      print(self.queue[self.front]) 
      if self.front == self.rear:
        break
    
  def find(self, value):
    i = (self.front + 1) % self.MAX_SIZE
    while i != (self.rear + 1) % self.MAX_SIZE:
        if self.queue[i] == value:
            return i
        i = (i + 1) % self.MAX_SIZE
      
    return -1
        