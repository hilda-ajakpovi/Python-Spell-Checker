def validator(prompt, valid_values, validate_function):
    '''
    This function checks if a value is valid and keeps retrying it until it is valid
    
    :param prompt: Additional promt to display if value is invalid (str)
    :param valid_values: tupple of valid values or valid ending of a file
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
        raise ValueError("Invalid Input.")
    
def validate_ending(value, valid_ending):
    if not value.endswith(valid_ending):
        raise ValueError("Invalid File.")
    
