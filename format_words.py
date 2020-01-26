from book_to_sentences import parse_to_sentences

def format_word(s):
    """
    Input: string s (word)
    outputs: string w with proper alphabetical format without any syntax or punctuation
    Note: s is immutable, format_word only mutates a copy
    """
    if s.isalpha() == True:
        return s
    else:
        for i in range(len(s)):
            if s[i].isalpha() == False:
                if i == len(s) - 1:
                    return format_word(s[:i])
                elif i == len(s) - 2:
                    if s[-1] == 'd':
                        return format_word(s[:i])
                    elif s[-1] == 't':
                        if s == "can't":
                            return "cannot"
                        elif s[i - 1] == 'n':
                            return format_word(s[:i - 1])
                    elif s[-1] == 's':
                        return format_word(s[:i])
                    elif s[i:] == 've':
                        return format_word(s[:i])
            elif s[0] == '"' or s[0] == '(' or s[0] == '.' or s[0] == ' ':
                return format_word(s[1:])


def parse_to_words(path_in_dir_to_file):
    """
    Parse an entire txt file directly to list of words
    """
    with open(path_in_dir_to_file) as f:
        data = f.readlines()
    X  = list(filter(lambda k: len(k) > 3, data))   # removes white lines in b/w paragraphs
    X2 = list(map(lambda k: k.strip(), X))          # removes indents and '\n' after each line
    X3 = list(map(lambda k: k.split(), X2))         # example: [['the', 'cat', 'ate'], ['everyone']]
    X4 = list(map(lambda k: k.lower(), X3))
    X5 = list(map(lambda k: format_word(k), X5))    # removes plural forms, syntax, and numbers, etc.
    X6 = list(filter(lambda k: type(k) != type(None), X5)) # notalp('...') => None, this removes None type
    X7 = list(filter(lambda k: len(s) >= 2, X6))    # removes small words like 'i' and 'a'
    return X7

def generate_dict(list_of_words): # alternative_gen_dict offers better dictionary
    """
    generate a dictionary from list of words
    """
    dictionary = {} # container for words -- dictionary = { key=word : value={ 'freq' : n, 'length' : l, ...}, ...}
    for word in list_of_words:
        if word in dictionary:
            (dictionary[word])['freq'] += 1
        else:
            dictionary[word] = {'freq':1, 'length':len(word)}
    return dictionary

def alternative_gen_dict(list_of_sentences):
    """
    generate a dictionary with example phrases from list of sentences
    """
    dictionary = {}
    for index, sentence in enumerate(list_of_sentences): # example: "the cat ate everypne"
        Y  = list(sentence.split()) # example: ['the', 'cat', 'ate', 'everyone']
        Y1 = list(map(lambda k: format_word(k), Y))
        Y2 = list(filter(lambda k: type(k) != type(None), Y1))
        Y3 = list(map(lambda k: k.lower(), Y2))
        Y4 = list(filter(lambda k: len(k) >= 3, Y3))
        for formatted_word in Y4:
            if formatted_word in dictionary:
                (dictionary[formatted_word])['freq'] += 1
                list_of_index = ((dictionary[formatted_word])['indicies'])
                if index not in list_of_index:
                    ((dictionary[formatted_word])['indicies']).append(index)
            else:
                dictionary[formatted_word] = {'freq':1, 'length':len(formatted_word), 'indicies':[index]}
    return dictionary


# Test
"""
s = " (HELP " # s is immutable
print(format_word("(Help"))
print(format_word("(help"))
print(format_word("help)"))
print(format_word("(help)"))
print(format_word(".Fahim"))
print(format_word("Fahim."))
print(format_word("Fahim..."))
print(format_word(s))
print(s)
"""

# Test alt_gen_dict
"""
sent = ['/ THE BOY WHO LIVED Mr. and Mrs. Dursley, of number four, Privet Drive, were PINK proud to say that they were perfectly normal, thank you very much.', 'Page | 348 Harry Potter and PINK the Philosophers Stone - J.K. Rowling', 'pink']
alternative_gen_dict(sent)
print(sent)
"""