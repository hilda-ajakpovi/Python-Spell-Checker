from word_list import WordList

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


def spell_check_words(dictionary:set, words:str) -> WordList:
    '''
    Loops through all words in word string and checks if they are in the dictionary

    Input: dictionary - set of dictionary words, words - string to spell check
    Return: mispelled_words - object contining list of misspelled words
    '''
    words = split_words(words)
    mispelled_words = WordList()

    for index, word in enumerate(words):
        comparrison_word = word['word'].casefold() # convert word to lower and remove trailing and leading whitespace

        if comparrison_word not in dictionary:
            mispelled_words.append(word['word'], word['start'], word['end'], index)
    return mispelled_words