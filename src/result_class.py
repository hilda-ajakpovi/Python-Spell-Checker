class Result():
    '''
    An instance of this class represents the returned result from a function
    '''
    def __init__(self):
        self.__value = None
        self.__quit = False

    def userQuits(self):
        self.__quit = True

    def quit(self):
        return self.__quit
    
    def value(self):
        return self.__value
    
    def setValue(self, value):
        self.__value = value