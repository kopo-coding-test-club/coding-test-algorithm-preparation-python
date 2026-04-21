class Node:
  def __init__(self,data):
    self.data = data
    self.next = None
    self.prev = None

class DoublyLinkedListStack:
  def __init__(self):
    self.head = None
    self.tail = self.head
    self.no = 0
  
  def is_empty(self):
    return self.no == 0
  
  def __len__(self):
    return self.no
  
  def push(self, data):
    new_node = Node(data)
    
    if self.head is None:
      self.head = new_node
      self.tail = new_node
    else:
      new_node.prev = self.tail
      self.tail.next = new_node
      self.tail = new_node
    self.no += 1
  
  def pop(self):
    if self.tail is None:
      return None
    data = self.tail.data
    if self.no == 1:
      self.head = None
      self.tail = None
    else:
      self.tail = self.tail.prev
      self.tail.next = None
    self.no -= 1
    return data
  
  def peek(self):
    if self.tail is None:
      return None
    data = self.tail.data
    return data
  
  def dump(self):#스택에서 순서대로 출력하는 함수
    curr = self.head
    while curr:
      print(curr.data)
      curr = curr.next
  
  def __contains__(self, data):
    curr = self.head
    while curr:
      if curr.data == data:
        return True
      curr = curr.next
    return False
  
  def clear(self):
    self.head = None
    self.tail = None
    self.no = 0
    
  def find(self , data):
    curr = self.head
    idx = 0
    while curr:
      if curr.data == data:
        return idx
      curr = curr.next
      idx += 1
    return -1
      
      
    
      
      
