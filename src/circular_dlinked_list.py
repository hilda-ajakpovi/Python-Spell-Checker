'''
Cicular Double Linked List 
Hilda Ajakpovi

This is a modified Doubly Linked List so that the first node points to the end and the last node points to the beginning
'''

class DLinkedListNode:
    '''
    An instance of this class represents a node in Doubly-Linked List
    '''
    def __init__(self, initData, initNext, initPrevious):
        self.__data = initData
        self.__next = initNext
        self.__previous = initPrevious

        # create links for previous and next nodes to point to this node
        if initNext != None:
            self.__next.__previous = self
        if initPrevious != None:
            self.__previous.__next = self

    def getData(self):
        '''
        Returns the data of the node
        Input: N/A
        Return: data in node
        '''
        return self.__data

    def setData(self, newData):
        '''
        Changes the data of a node
        Input: newData - new data of the node
        Return: None
        '''
        self.__data = newData

    def getNext(self):
        '''
        Returns the next node of this node
        Input: N/A
        Return: Next node
        '''
        return self.__next

    def getPrevious(self):
        '''
        Returns the previous node of this node
        Input: N/A
        Return: Previous Node
        '''
        return self.__previous

    def setNext(self, newNext):
        '''
        Sets the next node of this node to be a different node
        Input: newNext - new next node
        Return: None
        '''
        self.__next = newNext

    def setPrevious(self, newPrevious):
        '''
        Sets the previous node of this node to be a different node
        Input: newPrevious - new previous node
        Return: None
        '''
        self.__previous = newPrevious
        
    


class CircularDLinkedList:
    '''
    An instance of this class represents a Circular Doubly-Linked List
    '''
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0
        #self.__maxSize = maxSize

    def add(self, item):
        '''
        Adds and item to the begining of the list and increments the size of the list
        Input: item - item to add
        Return: None
        '''
        # Raise an exception if the list is full
       # if self.__size >= self.__maxSize:
            #raise Exception('List is Full')
        
        empty = False
        if self.__head == None:
            empty = True
        
        newNode = DLinkedListNode(item, self.__head, self.__tail)
        self.__head = newNode
        
        # if empty, all aspects of this node point to this only node (next, previous, head and tail)
        if empty:
            self.__tail = newNode
            self.__head.setPrevious(self.__tail)
            self.__tail.setNext(self.__head)        
        
        self.__size += 1
        

    def append(self, item):
        '''
        Adds an item to the end of the list and icrements the size
        Input: item - item to add
        Return: None
        '''
        # Raise and exception if the list if full
        #if self.__size >= self.__maxSize:
            #raise Exception('List is Full')
        
        empty = False
        if self.__tail == None:
            empty = True
            
        newNode = DLinkedListNode(item, self.__head, self.__tail)
        self.__tail = newNode
        if empty:
            self.__head = newNode
            self.__head.setPrevious(self.__tail)
            self.__tail.setNext(self.__head)
        self.__size += 1

    def insert(self, pos, item):
        '''
        Adds a new node at the given position with item as its data and increments the size
        Input: pos - postion that item should be inserted at; item - item to be added
        Return: None
        '''
        # Assert that the position is a positive integer
        assert type(pos) == int, ('Position must be an integer')
        assert 0 <= pos <= self.__size, ('Position must be positive but less than or equal to the size') 
                
        # Insert at the front
        if pos == 0:
            self.add(item)  
           
        # Insert at the end
        elif pos == self.__size:
            self.append(item)
        
        # Insert at the middle        
        else:
            current = self.__head
            for i in range(pos):
                current = current.getNext()
                
            nextNode = current
            current = current.getPrevious()
            newNode = DLinkedListNode(item, nextNode, nextNode.getPrevious())                
            current.setNext(newNode)
            self.__size += 1
            

    def pop(self):
        '''
        Removes and returns the last item in the list
        Input: N/A
        Return: item that was removed
        '''
        # Raise and exception if the list is empty
        if self.__size == 0:
            raise Exception("List is empty")
        
        discardNode = self.__tail
        current = self.__tail.getPrevious()
        current.setNext(self.__head)
        self.__tail = current
        self.__head.setPrevious(self.__tail)        
        self.__size -= 1
        return discardNode.getData()

    def delete(self, pos=None):
        '''
        Removes and returns the item in the given position.
        Input: pos - position that item should be removed from. If no arguement is 
        given, it's assigned to None and the item at the last position is removed
        Return: Item that was removed
        '''
        # Assert that the position is a positive integer
        if pos != None:
            assert type(pos) == int, ('Position must be an integer')
            assert pos >= 0, ('Position must be positive')  

        # Raise and exception if the list is empty
        if self.__size == 0:
            raise Exception("List is empty")
            
        
        # remove if only one item in list
        if self.__size == 1:
            discardNode = self.__head
            self.__head = None
            self.__tail = None
            self.__size -= 1
            return discardNode.getData()
        
        # remove from end
        if pos == None or pos == self.__size-1:
            return self.pop()        
        
        # remove from begining
        elif pos == 0:
            discardNode = self.__head
            current = self.__head.getNext()
            current.setPrevious(self.__tail)
            self.__head = current
            self.__tail.setNext(self.__head)
            self.__size -= 1
            return discardNode.getData() 
        
        # remove from middle
        else:
            current = self.__head
            for i in range(pos):
                current = current.getNext()
                
            nextNode = current.getNext()
            previousNode = current.getPrevious()
            previousNode.setNext(nextNode)
            nextNode.setPrevious(previousNode)
            self.__size -= 1 
            return current.getData()                
            

    def getSize(self):
        '''
        Getter method for the size
        Input: N/A
        Return: size of the list
        '''
        return self.__size

    def getItem(self, pos):
        '''
        Returns the item at the given position.
        Input: pos - position of the item that we want to retrieve
        Return: data of the node that was retrieved
        '''
        # Assert that the pos is an integer
        assert type(pos) == int, ('Position must be an integer')
        # Raise exception if the position is out of range for the list
        if pos > self.__size-1 or pos < self.__size*-1:
            raise IndexError('Position out of range')
        
        # Convert negative index to positive index
        if pos < 0:
            pos += self.__size
            
        current = self.__head
        for i in range(pos):
            current = current.getNext()
        return current.getData()
            
            
    def getNextNode(self, pos):
        '''
        Gets the data of the next node of a given node
        Input: pos - postion of the node that we want to get the next one of
        Return: Data of the next node
        '''
        current = self.__head
        for i in range(pos):
            current = current.getNext()
        return current.getNext().getData()
    
    def getPreviousNode(self, pos):
        '''
        Gets the data of the previous node of a given node
        Input: pos - position of the node that we want to get the next node of 
        Return: Data of the next node
        '''
        current = self.__head
        for i in range(pos):
            current = current.getNext()
        return current.getPrevious().getData()
    
    def __str__(self):
        '''
        Creates the string representation of the linked list
        Input: N/A
        Return: output - string representation of the list
        '''
        current = self.__head
        output = ''
        for i in range(self.__size):
            output += str(i+1) + ". " + str(current.getData()) + "\n"
            #output += str(current.getData()) + ', '
            current = current.getNext()
        output = output.strip()
        return output
    




