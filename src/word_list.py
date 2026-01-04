'''
Word List
Hilda Ajakpovi

This WordList class is used to store a list of misspelled words. It contains properties such as items - a list of the actual items 
that eventually becomes a list of dicts, current - an int that stores the index item in the list that the user is currently viewing
as the current word, size - an int that stores the number of words in the list (allows for duplicates)

This class has the following methods
    - add: adds a dictionary with keys 'word' - str of the actual misspelled word, 'start' - the start index of the word from original
            text, 'end' - the end index of the word from the original text, 'suggestions' - a list suggested correctly spelt words based
            on the misspelled word from the given dictionary
    - append: same as add but instead adds the dictionary to the end of the list
    - goLeft: increments the current property and wraps around to beggining of list if current is set to the last element
    - goRight decrements the current property and wraps around to the end of the list if current is set to the first element
    - delete: removes item at a specified index or the item at current index if no index is given
    - getInfo: returns item at current index
    - current: returns int - current index
    - setCurrent: allows for current index to be changed to any valid value
    - previousItem: returns the item at the index one less than current or at end of list if current = 0
    - nextItem: returns the item at the index one greater than current or at the beggining of list if current = size-1
    - getSize: returns the amount of items in the list (size)
    - createSet: creates and returns a set representaion of items in the list
    - findItem: finds and returns the first instance of an item in the list whose key 'word' has a value that matches the given value
    - removeAllItems: removes all items in the list whose 'word' key has a value that matches the given value
    - updateSuggestions: adds suggested words as value for 'suggestions' key for a value item in the list
    - getIndex: returns the index of the first occurance of an item whose 'word' key has a value that matches the given value
    - getItems: returns the list of items
'''
class WordList():
    '''
    An instance of this class represents a blackbox circular list of words 
    '''
    def __init__(self):
        self.__items = []
        self.__current = 0 # Index of active node
        self.__size = 0
        
    def add(self, item, start, end):
        '''
        Responsible for adding a new node to the circular list.
        Input: item - data that will go into the new node
        Return: None
        '''
        word_info = {
            'word': item,
            'start': start,
            'end': end,
            'suggestions': []
        }
        self.__size += 1  
        self.__items.insert(self.__current, word_info)

    def append(self, item, start, end, index):
        '''
        Responsible for adding a new node to the end of the list
        Input: item - data that will go inside new node
        Return: None
        '''
        word_info = {
            'word': item,
            'start': start,
            'end': end,
            'og_index': index,
            'suggestions': []
        }
        self.__size += 1  
        self.__items.append(word_info)


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
    
    def delete(self, index=None):
        '''
        Removes an item at a specified index
        Input: N/A
        Return: None
        '''
        if index == None:
            index = self.__current
        try:
            self.__items.pop(index)
            self.__size -= 1
            if index <= self.__current:
                self.goLeft() # without this, current goes to the item to the right of the deleted item
        except Exception as e:
            print(e)     
    
    def getInfo(self) -> dict:
        '''
        Retrieves and returns the info of the active node of the list
        Input: N/A
        Return: items - the data in the active node (double linked list)
        '''
        item = self.__items[self.__current]
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
        Setter function for the current attribute. Throws an exception if newCurrent is not a valid value
        Input: newCurrent - what the new current (index of active node) should be
        Return: None
        '''
        assert 0 <= newCurrent < self.__size
        self.__current = newCurrent
    
    def __str__(self):
        '''
        Creates a string representation of the list
        Input: N/A
        Return: string reprsenation of list
        '''
        output = ''
        for i in range(self.__size):
            output += str(i+1) + '. ' + str(self.__items[i]['word']) + '\n'
        output = output.rstrip()
        return output
        
    def previousItem(self) -> dict:
        '''
        Retreives the data in the previous node from the active node
        Input: N/A
        Return: data from previous node
        '''
        if self.__current == 0:
            previousNode = self.__items[-1]
        else:
            previousNode = self.__items[self.__current - 1]

        return previousNode
    
    def nextItem(self) -> dict:
        '''
        Retrieves the data in the next node from the active node
        Input: N/A
        Return: data from next node
        '''
        if self.__current >= self.__size - 1:
            nextNode = self.__items[0]
        else:
            nextNode = self.__items[self.__current + 1]
        
        return nextNode
    
    def getSize(self):
        '''
        Getter function for size of list
        Input:N/A
        Return: int - sive of list
        '''
        return self.__size
    
    def createSet(self):
        '''
        Creates python set represenation of words in list
        
        Input: N/A
        Return: word_set - set containg all the values in list
        '''
        word_set = set()
        for item in self.__items:
            word_set.add(item['word'].casefold().strip())
        return word_set
    
    def findItem(self, item):
        '''
        Finds first occurance of word in list
        
        Input: item - item to find
        Return: dictionary associated to item, None if not found
        '''
        item = next((i for i in self.__items if i["word"].lower() == item.lower()), None)
        return item
    
    def removeAllItems(self, item):
        '''
        Finds all instances of the item and removes them from list
        
        Input: item to be removed
        Return: None
        '''
        for index, list_item in enumerate(self.__items):
            if item.lower() == list_item["word"].lower():
                self.delete(index)

    def updateSuggestions(self, new_suggestions:list, item:str):
        '''
        changes the suggestions for all items in the list that are the same word
        
        Input: new_suggestions - list of suggested words, item - word whose suggestions should be updated
        Return: None
        '''
        for list_item in self.__items:
            if item.lower() == list_item["word"].lower() and len(list_item['suggestions']) == 0:
                for suggestion in new_suggestions:
                    list_item['suggestions'].append(suggestion['word'])

    def getIndex(self, item:str):
        '''
        Finds and returns the index of the first occurance of an item give
        
        Input: item - item to find
        Return: index - index of item, None if not found
        '''
        for index, list_item in enumerate(self.__items):
            if list_item['word'].lower() == item.lower():
                return index

    def getItems(self):
        '''
        Getter function for list of items

        Input: N/A
        Return: None
        '''
        return self.__items