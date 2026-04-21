class Node:
  def __init__(self, data):
    self.data = data
    self.prev = None
    self.next = None
class Doubled_LinkedList:
  def __init__(self):
    self.head = None
    self.tail = self.head
    self.no = 0
  
  def __len__(self):
    return self.no
  
  def is_empty(self):
    return self.no == 0
  
  def search(self, data):
    node = self.head
    while node is not None:
      if node.data == data:
        return True
      node = node.next
    else:
      return False
  
  def __contains__(self,data):
    return self.search(data)
  
  def print(self):
    node = self.head
    
    while node is not None:
      print(node.data)
      node = node.next
  
  def print_reverse(self):
    node = self.tail
    while node is not None:
      print(node.data)
      node = node.prev
  
  #맨 앞에 추가
  def append_first(self, data):
    if self.head is None:
      self.head = Node(data)
      self.tail = self.head
      self.no += 1
    else:
      new_node = Node(data)
      new_node.next = self.head
      self.head.prev = new_node
      self.head = new_node
      self.no += 1
  
  ## 맨끝에 추가
  def append_last(self, data):
    if self.head is None:
      self.head = Node(data)
      self.tail = self.head
      self.no += 1
    else:
      new_node = Node(data)
      new_node.prev = self.tail
      self.tail.next = new_node
      self.tail = new_node
      self.no += 1

  
  def insert_before(self, data, new_data):
    if self.head is None:
      self.head = Node(new_data)
      self.tail = self.head
      self.no += 1
    else:
      node = self.tail
      
      while node is not None:
        if node.data == data:
          break
        node = node.prev
      else:
        return False        
      
      new_node = Node(new_data)
      new_node.next = node
      new_node.prev = node.prev
      
      if node.prev is not None:#중간에 삽입하는 경우
        node.prev.next = new_node
      else:
        self.head = new_node#맨 처음에 삽입하는 경우
      
      node.prev = new_node
      self.no += 1
      return True
  
  def insert_after(self, data, new_data):
    if self.head is None:
      self.head = Node(new_data)
      self.tail = self.head
      self.no += 1
    else:
      node = self.head
      while node is not None:
        if node.data == data:
          break
        node = node.next
      else:
        return False
      
      new_node = Node(new_data)
      
      new_node.prev = node
      new_node.next = node.next
      if node.next is not None:#중간에 삽입하는 경우
        node.next.prev = new_node
      else:#맨끝에 삽입하는 경우
        self.tail = new_node
      node.next = new_node
      self.no += 1
      return True
             
  #맨 앞의 요소 삭제
  def remove_first(self):
    if self.head is None:
      return False
    
    self.head = self.head.next
    if self.head is not None:
      self.head.prev = None
    else:
      self.tail = None
    self.no -= 1
    
  #맨 끝의 요소 삭제
  def remove_last(self):
    if self.tail is None:
      return False
    
    self.tail = self.tail.prev
    if self.tail is not None:
      self.tail.next = None
    else:
      self.head = None
    
    self.no -= 1
    return True
   
  #중간에 있는 요소 삭제  
  def remove(self, data):
    if self.head is None:
      return False
    
    node = self.head
    while node is not None:
      if node.data == data:
        if node.prev is not None:#해당 노드의 왼쪽이 있는 경우
          node.prev.next = node.next
        else:#해당 노드의 왼쪽이 없는 경우 즉 해당 노드가 헤드인 경우
          self.head = node.next
        
        if node.next is not None:#해당 노드의 오른쪽이 있는 경우
          node.next.prev = node.prev
        else:#해당 노드의 오른쪽이 없는 경우 즉 해당 노드가 tail
          self.tail = node.prev
        self.no -= 1
        return True
      node = node.next
    return False
  
  #모든 요소 지우는 함수
  def clear(self):
    self.head = None
    self.tail = None
    self.no = 0