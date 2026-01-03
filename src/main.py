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
    
    :param dictionary_name: file to load words from. Set to the standard dictionary if no file is given (words_alp
    '''
    words = open_file('r', file_name=dictionary_name)[0]
    #words = input_handler.open_files(dictionary_name, 'r')
    return set(words.split())


def open_file(mode:str, text=None, file_name=None):
    if file_name == None:
        file_name = input_handler.validator("Please enter a .txt file", ".txt", input_handler.validate_ending)
        if file_name == 'q':
            return file_name
    return input_handler.open_files(file_name, mode, text)

def get_user_words():
    print("\nPlease select what you would like to input. File (a) or Typed Input (b)")
    selection = input_handler.validator("Please Select a or b", ('a', 'b', 'q'), input_handler.validate_value)
    if selection == 'q':
        return selection, None, None
    file_name = None
    input_from_file = False

    if selection == 'a':
        print("Enter Path to your file")
        file, file_name = open_file("r")
        if file_name == 'q':
            return file_name, None, None
        input_from_file = True
        user_input = file
    else:
        user_input = input("Enter your input: ")
        if user_input.casefold().strip() == 'q':
            return user_input, None, None

    return user_input, input_from_file, file_name

def split_words(text:str) -> list[dict]:
    '''
    Takes a string, and splits it into words keeping track of start and end indecies from original text
    
    Input: text - string to split
    Return: words - list of dictionary
    '''
    words = []
    in_word = False
    start = 0
    extra_valid_ch = ('-', "'")

    for i, ch in enumerate(text):
        if ch.isalnum() or ch in extra_valid_ch:
            if not in_word:
                in_word = True
                start = i
        else:
            if in_word:
                words.append({
                    "word": text[start:i],
                    "start": start,
                    "end": i
                })
                in_word = False

    # handle case where text ends in a word
    if in_word:
        words.append({
            "word": text[start:len(text)],
            "start": start,
            "end": len(text)
        })

    return words


def spell_check_words(dictionary, words:str):
    '''
    temp naive spell checker
    
    :param dictionary: dictionary to reference words from (set)
    :param words: input of user words (str)
    :param mispelled_words: list of mispelled words
    '''
    words = split_words(words)
    mispelled_words = WordList()

    for index, word in enumerate(words):
        comparrison_word = word['word'].casefold() # convert word to lower and remove trailing and leading whitespace

        if comparrison_word not in dictionary:
            mispelled_words.append(word['word'], word['start'], word['end'], index)
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
    print("Enter (c) to choose a specific word to select (selects first occurance of word)")
    print("Enter (i) to show your text")

def add_to_dictionary(dictionary:set, word:str, user_input:str, mispelled_words:WordList):
    dictionary.add(word.casefold().strip())
    mispelled_words.removeAllItems(word)
    print("Word added to dictionary")

def edit_distance(word1:str, word2:str) -> int:
    '''
    Calculates minimum number of edits needed to transform word1 into word2 using Damerau-Levenshtein edit distance algorithm by
    comaparing substrings
    Edits allowed includ deletion of a letter, insertion of a letter, substituting a letter with another and swapping adjacent letters
    
    Input: word1 and word2 are the words to calculate edit distance
    Return: dp[m][n] last element of Dynamic programming table that conatins min edit distance for full words
    '''
    m = len(word1)
    n = len(word2)

    # dp[i][j] = min edits to convert word1[:i] → word2[:j]
    dp = [[0] * (n + 1) for _ in range(m + 1)] # set up dp table and fill with zeros

    # base cases - comparing against empty string
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    # calculate starting from first substring and onwards
    for i in range(1, m + 1):
        for j in range(1, n + 1):

            if word1[i - 1] == word2[j - 1]:
                cost = 0
            else:
                cost = 1

            # insertion, deletion, substitution
            dp[i][j] = min(
                dp[i - 1][j] + 1,        # deletion
                dp[i][j - 1] + 1,        # insertion
                dp[i - 1][j - 1] + cost  # substitution
            )

            # transposition (swap of adjacent characters)
            if (
                i > 1 and j > 1 and
                word1[i - 1] == word2[j - 2] and
                word1[i - 2] == word2[j - 1]
            ):
                dp[i][j] = min(
                    dp[i][j],
                    dp[i - 2][j - 2] + 1
                )

    return dp[m][n]

def max_allowed_distance(word:str) -> int:
    '''
    Calculates the max allowed edit distance and length distance allowed for this word when comapring against other words
    
    Input: word - word to calculate for
    Return: max distance
    '''
    length = len(word)

    if length <= 4:
        return 1
    elif length <= 7:
        return 2
    else:
        return 3

def get_suggestions(mispelled_words:WordList, dictionary:set, word:dict):
    print("Calculating word suggestions from dictionary...")
    dictionary_list = list(dictionary)
    max_dist = max_allowed_distance(word['word'].strip())
    suggestions = []

    for candidate in dictionary_list:
        if abs(len(candidate) - len(word['word'])) > max_dist:
            continue

        dist = edit_distance(word['word'].casefold().strip(), candidate)

        if dist <= max_dist:
            suggestions.append({
                'word':candidate,
                "distance": dist
            })
    suggestions.sort(key=lambda x: (x["distance"], x["word"])) # sort based on distance from low to high and alphabetically if there is a tie
    mispelled_words.updateSuggestions(suggestions, word['word'])

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

def word_navigation(mispelled_words:WordList, dictionary:set, user_input:str):
    '''
    Contains word navigation loop. Continously print menu that allows user to loop 
    
    :param mispelled_words: Description
    :type mispelled_words: WordList
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
                break
        elif selection == 's' or selection == 'c':
            user_input = select_word(selection, mispelled_words, dictionary, user_input)
            if user_input == 'q':
                break
        elif selection == "b":
            print("Are you sure? This cannot be undone (y/n)") # prolly change
            new_selection = input_handler.validator("Please enter either y or n", ('y', 'n', 'q'), input_handler.validate_value)
            if new_selection == 'y':
                return user_input
            elif new_selection == 'q':
                return new_selection
        elif selection == 'i':
            print(user_input)
            print("Enter any key to go back")
            if input(": ").casefold().strip() == 'q':
                break
        elif selection == 'q': 
            return selection
    return user_input

def main():
    print("\n***Welcome to Spell Checker.***\nInput either a file or your own input to spell check the words.\nFeel free to upload your own dictionary or use the standard dictionary")
    print("Enter (q) at any point to exit the program")
    print("Would you like to use your own dictionary (a) or the standard dictionary (b)?")

    # open and assign appropriate dictionary
    selection = input_handler.validator("Please Select personal dictionary (a) or standard dictionary (b)", ('a', 'b', 'q'), input_handler.validate_value)
    if selection == 'q':
        print("Exiting Program...")
        return
    elif selection == 'a':
        print("Enter path to your file")
        file_name = input_handler.validator("Please enter a .txt file", ".txt", input_handler.validate_ending)
        if file_name == 'q':
            print("Exiting Program...")
            return
        dictionary = upload_dictionary(file_name)
    else:
        dictionary = upload_dictionary()

    # Program loop
    while True:
        user_input, input_from_file, file_name = get_user_words() # get user input from either typed or file input
        if user_input == 'q':
            print("Exiting Program...")
            break

        mispelled_words = spell_check_words(dictionary, user_input)
        #print(f"\nAmount of mispelled words: {num_mispelled_words}")
        if mispelled_words.getSize() > 0:
            output = word_navigation(mispelled_words, dictionary, user_input)
            if output == 'q':
                print("Exiting Program...")
                break

            print("Would you like to save your text to a file? (y/n)")
            selection = input_handler.validator("Please enter either y or n", ('y', 'n'), input_handler.validate_value)
            if selection == 'q':
                print("Exiting Program...")
                return
            elif selection == 'y':
                if input_from_file:
                    print("Would you like to save your text to your original file? (y/n)")
                    selection = input_handler.validator("Please enter either y or n", ('y', 'n', 'q'), input_handler.validate_value)
                    if selection == 'y':
                        open_file("w", output, file_name)
                    if selection == 'q':
                        print("Exiting Program...")
                        return
                    else:
                        if open_file("w", output) == 'q':
                            print("Exiting Program...")
                            return
                else:
                    if open_file("w", output) == 'q':
                        print("Exiting Program...")
                        return

                print("File updated.") 

        else:
            print("No misspelled words found.")
            
        print("Would you like to go again with new input? (y/n)")
        selection = input_handler.validator("Please enter either y or n", ('y', 'n', 'q'), input_handler.validate_value)
        if selection == 'n' or selection == 'q':
            print("Goodbye")
            break


if __name__ == "__main__":
    main()