'''
Input Handler
Hilda Ajakpovi

This file contains functions for validating user input (input is continously asked from user until it is valid) and for opening files
(often from user input)
'''


def validator(prompt:str, valid_values, validate_function:function):
    '''
    This function checks if a value is valid and keeps retrying it until it is valid
    
    Input: prompt - Additional prompt to display if value is invalid, valid_valus - valid valus or ending of a file, validate_function
    - function to call to check if value is valid
    Return: value - value that is garunteed to be valid
    '''
    while True:
        try:
            value = input("Enter Input: ").casefold().strip()
            validate_function(value, valid_values)
            return value
        except Exception as e:
            print(e)
            print(prompt)

def validate_value(value, valid_values):
    if value not in valid_values:
        raise ValueError("\nInvalid Input.")
    
def validate_ending(value, valid_ending):
    if not value.endswith(valid_ending) and value != 'q':
        raise ValueError("\nInvalid File.")
    
def open_files(file_name, mode:str, text:str=None):
    while True:
        try:
            with open(file_name, mode) as file:
                if 'r' in mode:
                    return file.read(), file_name
                elif 'w' in mode:
                    return file.write(text)
        except:
            print("File does not exist. Please enter path to file again")
            file_name = validator("Please enter a .txt file", ".txt", validate_ending)
    