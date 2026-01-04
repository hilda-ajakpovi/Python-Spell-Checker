from word_list import WordList

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