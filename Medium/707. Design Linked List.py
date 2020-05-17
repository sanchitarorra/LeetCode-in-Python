class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.tail = None
        self.length = 0
        

    def get(self, index: int) -> int:
        
        if index < 0 or index >= self.length: #-1 case(out of bounds conditions)
            return -1
        
        if index == 0: # if we're searching head
            return self.head.val
        
        elif index == (self.length):
            return self.tail.val
        
        else:
            node = self.head #any element other than head or tail to search
            current = 0 # counter for iteration
            while node is not None:
                if current == index:
                    return node.val
                node = node.next
                current += 1
            return -1 # if list is empty
                
        

    def addAtHead(self, val: int) -> None:
        
        newNode = Node(val)
        if self.head is None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode
        self.length += 1
        
        
        

    def addAtTail(self, val: int) -> None:
      
        newNode = Node(val)
        node = self.head
        while node.next is not None:
            node = node.next
        node.next = newNode
        self.length += 1
            
        

    def addAtIndex(self, index: int, val: int) -> None:
        
        if index == 0:
            self.addAtHead(val)
        
        elif index == (self.length):
            self.addAtTail(val)
            
        else:
            current = 0
            prev = None
            node = self.head
            newNode = Node(val)
            while current != index and node.next != None:
                prev = node
                node = node.next
                current += 1
            if current == index:
                prev.next = newNode
                newNode.next = node
                self.length += 1
                
                
            
        

    def deleteAtIndex(self, index: int) -> None:
        
        if index == 0: # if head to delete
            tempNode = self.head.val #keeping temp variable to return that value
            newHead = self.head.next
            self.head = newHead
            self.length -= 1 #because of deletion
            return tempNode #return the deleted node's value
        
        else:
            node = self.head 
            current = 0
            prev = None # prev is a previous node which will be the new node after deletion
            while current != index and node.next != None: # conds for deletion(anywhere and end)
                prev = node
                node = node.next
                current += 1
            if current == index: #we're at the node
                prev.next = node.next #pointing the prev node to deleted node's next node
                self.length -= 1 #because of deletion
                
