import input_handler

'''
Main program
'''
def upload_dictionary(dictionary_name="words_alpha.txt"):
    while True:
        try:
            with open(dictionary_name) as f:
                return set(f.read().split())
        except:
            print("File does not exist. Please input file name again")
            dictionary_name = input_handler.validator("Please enter a .txt file", ".txt", input_handler.validate_ending)


def main():
    print("\n***Welcome to Spell Checker.***\nInput either a file or your own input to spell check the words.\nFeel free to upload your own dictionary or use the standard dictionary")
    print("Would you like to use your own dictionary (a) or the standard dictionary (b)?")

    selection = input_handler.validator("Please Select a or b", ('a', 'b'), input_handler.validate_value)
    if selection == 'a':
        words = upload_dictionary()
    elif selection == 'b':
        file_name = input_handler.validator("Please enter a .txt file", ".txt", input_handler.validate_ending)
        words = upload_dictionary(file_name)
    

if __name__ == "__main__":
    main()