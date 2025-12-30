from circular_dlinked_list import CircularDLinkedList

class WordList():
    '''
    An instance of this class represents a carousel
    '''
    def __init__(self):
        self.__items = CircularDLinkedList()
        self.__current = 0 # Index of active node
        self.__size = 0
        
    def add(self, item):
        '''
        Responsible for adding a new node to the circular doubly-linked list.
        Input: item - data that will go into the new node
        Return: None
        '''
        self.__items.insert(self.__current, item)
        self.__size += 1  

    def append(self, item):
        '''
        Responsible for adding a new node to the end of the list
        Input: item - data that will go inside new node
        Return: None
        '''
        self.__items.append(item)
        self.__size += 1

    def goLeft(self):
        '''
        Method to navigate through list by moving to the previous node. Increments the current index
        Input: N/A
        Return: None
        '''
        if self.__size != 0:
            self.__current -= 1
            self.__current %= self.__size
    
    def goRight(self):
        '''
        Method to navigate through list by moving to the next node. Increments the current index
        Input: N/A
        Return: None
        '''
        if self.__size != 0:
            self.__current += 1
            self.__current %= self.__size  
    
    def delete(self):
        '''
        Removes the current node from the list. Increments the current index
        Input: N/A
        Return: None
        '''
        try:
            self.__items.delete(self.__current)
            self.__size -= 1
            self.goLeft() # without this, current goes to the item to the right of the deleted item
        except Exception as e:
            print(e)
             
    
    def getInfo(self):
        '''
        Retrieves and returns the data of the active node of the list
        Input: N/A
        Return: items - the data in the active node (double linked list)
        '''
        item = self.__items.getItem(self.__current)
        return item
    
    def current(self):
        '''
        Getter function for the current attribute - index of active node
        Input: N/A
        Return: self.__current - index of active node (int)
        '''
        return self.__current
    
    def setCurrent(self, newCurrent):
        '''
        Setter function for the current attribute
        Input: what the new current (index of active node) should be
        Return: None
        '''
        self.__current = newCurrent
    
    def __str__(self):
        '''
        Creates a string representation of the list
        Input: N/A
        Return: string reprsenation of list
        '''
        return str(self.__items)
        
    def previousItem(self):
        '''
        Retreives the data in the previous node from the active node
        Input: N/A
        Return: data from previous node
        '''
        return self.__items.getPreviousNode(self.__current)
    
    def nextItem(self):
        '''
        Retrieves the data in the next node from the active node
        Input: N/A
        Return: data from next node
        '''
        return self.__items.getNextNode(self.__current)
    
    def getSize(self):
        '''
        Getter function for size of list
        Input:N/A
        Return: int - sive of list
        '''
        return self.__size
    
    def createSet(self):
        '''
        Creates python set represenation of list
        
        Input: N/A
        Return: word_set - set containg all the values in list
        '''
        word_set = set()
        current = self.__current # store current value
        self.__current = 0
        for i in range(self.__size):
            word_set.add(self.getInfo())
            self.__current += 1
        self.__current = current # restore current value
        return word_set

