import input_handler
from selection_of_word import select_word
from spell_checker import spell_check_words
from word_list import WordList
from result_class import Result
import string
import time
'''
Main program
'''

def upload_dictionary(dictionary_name:str="dictionaries/words_alpha.txt") -> set:
    '''
    loads a set of words from a file to serve as the dictionary for the program
    
    Input: dictionary_name - file to load words from. Set to the standard dictionary if no file is given (words_alpha)
    Return: set of all words from dictionary
    '''
    words = open_file('r', file_name=dictionary_name)[0]
    #words = input_handler.open_files(dictionary_name, 'r')
    return set(words.split())


def open_file(mode:str, text=None, file_name=None):
    '''
    Opens a specified file and returns value from action based on mode. If no file name is given, user is prompted to enter a path to 
    a file

    Input: mode - mode to open file on, text - text to write into file if need be, file_name - name of file to be opened
    Return: file.read() & file_name or number of characters written to a file
    '''
    if file_name == None:
        file_name = input_handler.validator("Please enter a .txt file", ".txt", input_handler.validate_ending)
        if file_name == 'q':
            return file_name
    return input_handler.open_files(file_name, mode, text)

def get_user_words(result:Result):
    '''
    Gets text from user to spell check using either typed input or input from a file and stores this text in result.value()

    Input: result - object to store value and if user wants to quit program
    Return: None
    '''
    print("\nPlease select what you would like to input. File (a) or Typed Input (b)")
    selection = input_handler.validator("Please Select a or b", ('a', 'b', 'q'), input_handler.validate_value)
    if selection == 'q':
        result.userQuits()
        return
    file_name = None
    input_from_file = False

    if selection == 'a':
        print("Enter Path to your file")
        file, file_name = open_file("r")
        if file_name == 'q':
            result.userQuits()
            return 
        input_from_file = True
        user_input = file
    else:
        user_input = input("Enter your input: ")
        if user_input.casefold().strip() == 'q':
            result.userQuits()
            return 

    result.setValue((user_input, input_from_file, file_name))

def print_menu(mispelled_words:WordList):
    '''
    Print menu for word navigation

    Input: mispelled_words - object containing list of misspelled words
    Return: None
    '''
    # Display current word along with surrounding words if applicable
    current_word = mispelled_words.getInfo()['word']
    size = mispelled_words.getSize()
    print(f'\nCurrent word is "{current_word}"')
    print(f"Total number of mispelled words: {size}")
    if size > 1:
        # display surrounding words
        previous_word = mispelled_words.previousItem()['word']
        next_word = mispelled_words.nextItem()['word']
        print(f'"{previous_word}" <- "{current_word}" -> "{next_word}"')

        print("Enter (d) navigate right to next word")
        print("Enter (a) to navigate left to previous word")

    print("Enter (w) to display list of all mispelled words")
    print("Enter (s) to select current word")
    print("Enter (b) to go back to previous screen")
    print("Enter (q) to exit program")
    print("Enter (c) to choose a specific word to select (selects first occurance of word)")
    print("Enter (i) to show your text")

def word_navigation(mispelled_words:WordList, dictionary:set, user_input:str, result:Result):
    '''
    Contains word navigation loop. Continously print menu that allows user to choose an action from menu and then call appropriate
    functions to do selected action
    
    Input: mispelled_words - object containg list of misspelled words, dictionary - set of dictionary words, user_input - original text
    result - object to store potentially modified user's text and if user wants to quit program
    '''
    while mispelled_words.getSize() > 0:
        size = mispelled_words.getSize()
        print_menu(mispelled_words)

        valid_choices = ['w', 's', 'q', 'b', 'c', 'i']
        if size > 1:
            valid_choices.append('d')
            valid_choices.append('a')
        
        # build string to display valid choices (options to navigate right and left are only available when list size > 1)
        output = ''
        for item in valid_choices:
            output += item + ", "
        output = output.rstrip(", ")
        selection = input_handler.validator(f"Please select from these choices: {output}", valid_choices, input_handler.validate_value)
        if size > 1:
            if selection == 'd':
                mispelled_words.goRight()
            elif selection == 'a':
                mispelled_words.goLeft()

        if selection == 'w':
            print(mispelled_words)
            print("Enter any key to go back")
            if input(": ").casefold().strip() == 'q':
                result.userQuits()
                return
        elif selection == 's' or selection == 'c':
            user_input = select_word(selection, mispelled_words, dictionary, user_input)
            if user_input == 'q':
                result.userQuits()
                return
        elif selection == "b":
            print("Are you sure? This cannot be undone (y/n)") # prolly change
            new_selection = input_handler.validator("Please enter either y or n", ('y', 'n', 'q'), input_handler.validate_value)
            if new_selection == 'y':
                result.setValue(user_input)
                return 
            elif new_selection == 'q':
                result.userQuits()
                return 
        elif selection == 'i':
            print(user_input)
            print("Enter any key to go back")
            if input(": ").casefold().strip() == 'q':
                result.userQuits()
                break
        elif selection == 'q': 
            result.userQuits()
            return 
    #return user_input

def print_welcome_message():
    '''
    Prints welcome message for begining of program
    '''
    print("\n***Welcome to Spell Checker.***\nInput either a file or your own input to spell check the words.\nFeel free to upload your own dictionary or use the standard dictionary")
    print("Enter (q) at any point to exit the program")
    print("Would you like to use your own dictionary (a) or the standard dictionary (b)?")

def assign_dictionary(result:Result):
    '''
    Gets either a user dictionary or standard dictionary from file

    Input: result - object that stores dictionary values from function or if user wants to quit program
    Return: None
    '''
    selection = input_handler.validator("Please Select personal dictionary (a) or standard dictionary (b)", ('a', 'b', 'q'), input_handler.validate_value)
    if selection == 'q':

        #print("Exiting Program...")
        return
    elif selection == 'a':
        print("Enter path to your file")
        file_name = input_handler.validator("Please enter a .txt file", ".txt", input_handler.validate_ending)
        if file_name == 'q':
            result.userQuits()
            #print("Exiting Program...")
            return
        dictionary = upload_dictionary(file_name)
    else:
        dictionary = upload_dictionary()
    result.setValue(dictionary)

def main():
    print_welcome_message()
    result = Result()

    # open and assign appropriate dictionary
    assign_dictionary(result)
    if result.quit():
        print("Exiting Program...")
        return
    dictionary = result.value()

    # Program loop
    while True:
        #user_input, input_from_file, file_name = get_user_words() # get user input from either typed or file input
        get_user_words(result)
        if result.quit():
            break
        user_input, input_from_file, file_name = result.value()

        mispelled_words = spell_check_words(dictionary, user_input)
        #print(f"\nAmount of mispelled words: {num_mispelled_words}")
        if mispelled_words.getSize() > 0:
            #output = word_navigation(mispelled_words, dictionary, user_input)
            if result.quit():
                break
            output = result.value()

            print("Would you like to save your text to a file? (y/n)")
            selection = input_handler.validator("Please enter either y or n", ('y', 'n', 'q'), input_handler.validate_value)
            if selection == 'q':
                result.userQuits()
                break
                #print("Exiting Program...")
                #return
            elif selection == 'y':
                if input_from_file:
                    print("Would you like to save your text to your original file? (y/n)")
                    selection = input_handler.validator("Please enter either y or n", ('y', 'n', 'q'), input_handler.validate_value)
                    if selection == 'y':
                        print(file_name)
                        open_file("w", output, file_name)
                        print("done")
                    elif selection == 'q':
                        result.userQuits()
                        break
                        #print("Exiting Program...")
                        #return
                    else:
                        if open_file("w", output) == 'q':
                            #print("Exiting Program...")
                            #return
                            result.userQuits()
                            break
                else:
                    if open_file("w", output) == 'q':
                        #print("Exiting Program...")
                        #return
                        result.userQuits()
                        break

                print("File updated.") 

        else:
            print("No misspelled words found.")
            
        print("Would you like to go again with new input? (y/n)")
        selection = input_handler.validator("Please enter either y or n", ('y', 'n', 'q'), input_handler.validate_value)
        if selection == 'n' or selection == 'q':
            print("Goodbye")
            break
    print("Exiting Program")

if __name__ == "__main__":
    main()