import input_handler
from word_list import WordList
import string
import time
'''
Main program
'''
def upload_dictionary(dictionary_name="dictionaries/words_alpha.txt"):
    '''
    loads a set of words from a file to serve as the dictionary for the program
    
    :param dictionary_name: file to load words from. Set to the standard dictionary if no file is given (words_alpha.txt)
    '''
    words = input_handler.open_files(dictionary_name, 'r')
    return set(words.split())


def upload_file():
    file_name = input_handler.validator("Please enter a .txt file", ".txt", input_handler.validate_ending)
    return input_handler.open_files(file_name, "r+")

def get_user_words():
    print("\nPlease select what you would like to input. File (a) or Typed Input (b)")
    selection = input_handler.validator("Please Select a or b", ('a', 'b'), input_handler.validate_value)

    if selection == 'a':
        print("Enter Path to your file")
        user_input = upload_file()
    else:
        user_input = input("Enter your input: ")

    return user_input

def spell_check_words(dictionary, words:str):
    '''
    temp naive spell checker
    
    :param dictionary: dictionary to reference words from (set)
    :param words: input of user words (str)
    :param mispelled_words: list of mispelled words
    '''
    words = words.split()
    mispelled_words = WordList()

    for index, word in enumerate(words):
        word = word.rstrip(string.punctuation) # remove trailing punctuation
        comparrison_word = word.strip().casefold() # convert word to lower and remove trailing and leading whitespace

        if comparrison_word not in dictionary:
            mispelled_words.append(word, index)
    return mispelled_words

def print_menu(mispelled_words:WordList):
    # Display current word along with surrounding words if applicable
    current_word = mispelled_words.getInfo()['word']
    size = mispelled_words.getSize()
    print(f'\nCurrent word is "{current_word}"')
    print(f"Total number of mispelled words: {size}")
    if size > 1:
        previous_word = mispelled_words.previousItem()['word']
        next_word = mispelled_words.nextItem()['word']
        print(f'"{previous_word}" <- "{current_word}" -> "{next_word}"')

    print("Enter (w) to display list of all mispelled words")
    if size > 1:
        print("Enter (d) navigate right to next word")
        print("Enter (a) to navigate left to previous word")
    print("Enter (s) to select current word")
    print("Enter (b) to go back to previous screen")
    print("Enter (q) to exit program")
    print("Enter (c) to choose a specific word to select")

def calculate_suggested_words(selection:str):
    pass

def display_suggested_words():
    pass

def add_to_dictionary(dictionary:set, word:str, user_input:str, mispelled_words:WordList):
    dictionary.add(word.casefold().strip())
    mispelled_words.removeAllItems(word)
    print("Word added to dictionary")

def print_selection_menu():
    print("Enter the number associated with a suggested word to replace current word with suggestion")
    print("Enter (d) to add this word to dictionary")
    print("Enter (b) to go back to previous screen")

def select_word(selection:str, mispelled_words:WordList, dictionary:set, user_input:str):
    if selection == 'c':
        mispelled_words_set = mispelled_words.createSet()
        print("Enter your word or (b) to go to previous screen")
        mispelled_words_set.add('b')
        word = input_handler.validator("Please enter a valid word or 'b'", mispelled_words_set, input_handler.validate_value)
        word_info = mispelled_words.findItem(word)
        word = word_info['word']
    else:
        word_info = mispelled_words.getInfo()
        word = word_info['word']
    print(f'You have selected the word "{word}"')

    display_suggested_words()
    print_selection_menu()

    # calculate amount of suggested words
    valid_inputs = {'d', 'b'}
    for i in range(len(word_info['suggestions'])):
        valid_inputs.add(str(i+1))

    selection = input_handler.validator("Please enter a valid selection", valid_inputs, input_handler.validate_value)
    if selection == 'd':
        add_to_dictionary(dictionary, word, user_input, mispelled_words)
    elif selection == 'b':
        return
    else:
        pass
        # select selection and update user input  

def word_navigation(mispelled_words:WordList, dictionary:set, user_input:str):
    '''
    Contains word navigation loop. Continously print menu that allows user to loop 
    
    :param mispelled_words: Description
    :type mispelled_words: WordList
    '''
    while mispelled_words.getSize() > 0:
        size = mispelled_words.getSize()
        print_menu(mispelled_words)

        valid_choices = ['w', 's', 'q', 'b', 'c']
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
            input(": ")
        elif selection == 's' or selection == 'c':
            select_word(selection, mispelled_words, dictionary, user_input)
        elif selection == "b":
            print("Are you sure? This cannot be undone (y/n)") # prolly change
            new_selection = input_handler.validator("Please enter either y or n", ('y', 'n'), input_handler.validate_value)
            if new_selection == 'y':
                return
        elif selection == 'q': 
            return selection

def main():
    print("\n***Welcome to Spell Checker.***\nInput either a file or your own input to spell check the words.\nFeel free to upload your own dictionary or use the standard dictionary")
    print("Would you like to use your own dictionary (a) or the standard dictionary (b)?")

    # open and assign appropriate dictionary
    selection = input_handler.validator("Please Select personal dictionary (a) or standard dictionary (b)", ('a', 'b'), input_handler.validate_value)
    if selection == 'a':
        print("Enter path to your file")
        file_name = input_handler.validator("Please enter a .txt file", ".txt", input_handler.validate_ending)
        dictionary = upload_dictionary(file_name)
    else:
        dictionary = upload_dictionary()

    # Program loop
    while True:
        user_input = get_user_words() # get user input from either typed or file input

        mispelled_words = spell_check_words(dictionary, user_input)
        #print(f"\nAmount of mispelled words: {num_mispelled_words}")
        if mispelled_words.getSize() > 0:
           selection = word_navigation(mispelled_words, dictionary, user_input)
           if selection == 'q':
               print("Exiting Program...")
               break

        print("Would you like to go again with new input? (y/n)")
        selection = input_handler.validator("Please enter either y or n", ('y', 'n'), input_handler.validate_value)
        if selection == 'n':
            break


if __name__ == "__main__":
    main()