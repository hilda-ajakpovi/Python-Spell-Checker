def validator(prompt:str, valid_values, validate_function):
    '''
    This function checks if a value is valid and keeps retrying it until it is valid
    
    :param prompt: Additional promt to display if value is invalid (str)
    :param valid_values: tupple of valid values or valid ending of a file
    validate_function: function to call to check if value is valid
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
    if not value.endswith(valid_ending):
        raise ValueError("\nInvalid File.")
    
def open_files(file_name, mode:str):
    while True:
        try:
            with open(file_name, mode) as file:
                if 'r' in mode:
                    return file.read()
        except:
            print("File does not exist. Please enter path to file again")
            file_name = validator("Please enter a .txt file", ".txt", validate_ending)
    