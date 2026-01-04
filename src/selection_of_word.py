import input_handler
import string
from suggestions import get_suggestions
from word_list import WordList

def add_to_dictionary(dictionary:set, word:str, user_input:str, mispelled_words:WordList):
    dictionary.add(word.casefold().strip())
    mispelled_words.removeAllItems(word)
    print("Word added to dictionary")

def display_word_suggestions(mispelled_words:WordList, word:dict, dictionary:set, start:int, end:int):

    if len(word['suggestions']) > 0:
        # create output string
        output = ''
        if end > len(word['suggestions']):
            end = len(word['suggestions'])
        for index in range(start, end):
            output += str(index+1) + '. ' + word['suggestions'][index] + '\n'
        output = output.rstrip()
        print("Suggested word(s) to replace with")
        print(output)
        return end+1
    else:
        print("Sorry no suggestions availible")

def contains_punctuation(word:str) -> bool:
    '''
    Helper function that returns true if a word contains punctuation at the end
    
    :param word: Description
    :type word: str
    :return: Description
    :rtype: bool
    '''
    if word[-1] in string.punctuation:
        return True

def display_word_context(word:dict, user_input:str):
    '''
    Display context for given word by displaying 5 words before and after the word
    
    Input: word - word to find context for, user_input - where to get context from
    Return: None
    '''
    print("Context for seleted word:")
    user_words = user_input.split()
    index = word['og_index']
    start = index-5
    if start < 0:
        start = 0
    end = index + 6
    if end >= len(user_words):
        end = len(user_words) - 1

    context_words = user_words[start:end]
    output = '...'

    #create output string
    for item in context_words:
        output += item + ' '
    output = output.rstrip()
    output += '...'
    print(output)

def modify_capitalization(user_input:str, start:int, word:str) -> str:
    '''
    Changes the first letter of a word to match the capitalization of the original word in the user's input
    '''
    if user_input[start].isupper():
        return word[0].upper() + word[1:]
    return word

def replace_word(word:dict, mispelled_words:WordList, user_input:str, selection:str, selected_option:int=None, new_word:str=None) -> str:
    '''
    Replace a mispelled word with a selected suggested and modify user input
    
    Input: selected_option - suggested word num seleted, word - word information of misspelled word, mispelled_words - list of all misspelled 
    words, user_input - string of user input, selection - whether user selected current word or typed a word
    Return: user_input - modified user_input
    '''
    if selected_option != None:
        new_word = word['suggestions'][selected_option-1]
    print(f'You have selected "{new_word}" to replace with')

    new_word = modify_capitalization(user_input, word['start'], new_word)

    print("Would you like to replace all occurances? (y/n)")
    user_answer = input_handler.validator("Please select either y or n", ('y', 'n', 'q'), input_handler.validate_value)
    if user_answer == 'q':
        return user_answer
    elif user_answer == 'n':
        new_user_input = user_input[:word['start']] + new_word + user_input[word['end']:]
        # remove word from list of missplled words
        if selection == 'c':
            index = mispelled_words.getIndex(word['word'].casefold())
            assert index != None
            mispelled_words.delete(index)
        else:
            mispelled_words.delete()
    else:
        new_user_input = user_input
        mispelled_words_list = mispelled_words.getItems()
        for index, item in enumerate(mispelled_words_list):
            if item['word'].casefold() == word['word'].casefold():
                new_user_input = new_user_input[:item['start']] + new_word + new_user_input[item['end']:]
                mispelled_words.delete(index)
    print(f'Your new text is: "{new_user_input}"\n Would you like to save and continue? (y/n)')
    user_answer = input_handler.validator("Please select either y or n", ('y', 'n', 'q'), input_handler.validate_value)
    if user_answer == 'y':
        return new_user_input
    elif user_answer == 'q':
        return user_answer
    else:
        return user_input

def set_up_start_end(start:int, end:int, word_info:dict) -> tuple[int]:
    if start < 0:
        start = 0
        if end >= len(word_info['suggestions']):
            end = len(word_info['suggestions'])
        if abs(start - end) < 5:
            start = end - 5
            if start < 0:
                start = 0
            if abs(start - end) < 5:
                end = start + 5
    return start, end

def print_selection_menu():
    print("Enter the number associated with a suggested word to replace current word with suggestion")
    print("Enter (d) to add this word to dictionary")
    print("Enter (c) to write your own custom replacement")
    print("Enter (r) to remove this word as a misspelled word")
    print("Enter (b) to go back to previous screen")

def select_word(selection:str, mispelled_words:WordList, dictionary:set, user_input:str):
    if selection == 'c':
        mispelled_words_set = mispelled_words.createSet()
        mispelled_words_set.add('q')
        print("Enter your word or (b) to go to previous screen")
        mispelled_words_set.add('b')
        word = input_handler.validator("Please enter a valid word or 'b'", mispelled_words_set, input_handler.validate_value)
        if word == 'b':
            return user_input
        elif word == 'q':
            return user_input
        word_info = mispelled_words.findItem(word)
        index = mispelled_words.getIndex(word)
        word = word_info['word']
    else:
        index = mispelled_words.current()
        word_info = mispelled_words.getInfo()
        word = word_info['word']

    print(f'You have selected the word "{word}"')
    display_word_context(word_info, user_input)

    get_suggestions(mispelled_words, dictionary, word_info)

    start = 0 # start index to display suggested words from
    end = 5 # end index so that only 5 are displayed at a time
    total_words = len(word_info['suggestions'])
    while True:
        # set up start and end indecies to display at most 5 suggested words at at time
        start, end = set_up_start_end(start, end, word_info)
        display_word_suggestions(mispelled_words, word_info, dictionary, start, end)

        print_selection_menu()

        # set up valid_input
        valid_inputs = {'d', 'b', 'c', 'r', 'q'}
        for i in range(start, end):
            valid_inputs.add(str(i+1))
        if total_words >= 5:
            print("Enter (m) to see more suggestions")
            valid_inputs.add('m')
        if start >= 1:
            print("Enter (l) to show previous suggested words")
            valid_inputs.add('l')

        selected_option = input_handler.validator("Please enter a valid selection", valid_inputs, input_handler.validate_value)
        if selected_option == 'd':
            add_to_dictionary(dictionary, word, user_input, mispelled_words)
            return user_input
        elif selected_option == 'b':
            return user_input
        elif selected_option == 'm':
            start += 5
            end += 5
            total_words -= 5
        elif selected_option == 'l':
            start -= 5
            end -= 5
            total_words += 5
        elif selected_option == 'c':
            custom_word = input("Enter your new word (Entering 'q' here does not exit program): ").strip()
            return replace_word(word_info, mispelled_words, user_input, selection, new_word=custom_word)
        elif selected_option == 'r':
            mispelled_words.delete(index)
            print("Word removed")
            return user_input
        elif selected_option == 'q':
            return selected_option
        else:
            # select selection and update user input  
            return replace_word(word_info, mispelled_words, user_input, selection, int(selected_option))