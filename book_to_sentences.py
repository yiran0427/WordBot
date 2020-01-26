import os
import nltk.data # natural language toolkit; download 'punkt' package


def parse_to_sentences(path_in_dir_to_file):
    """
    Used to parse text file into sentences
    input: path_to_txt_file_in_dir
    output: list of strings (sentences)
    """
    tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
    with open(path_in_dir_to_file) as f:
        data = f.read()
    sentences = tokenizer.tokenize(data) # Parses as sentence
    formatted_sentences = list(map(lambda k: (k.replace('\n', "")), sentences)) # Removes unwanted '\n' in middle of sentence
    return formatted_sentences

# Test
"""
for i in os.listdir("./"):
    if i[-3:] == "txt":
        print(parse_to_sentences(i))
"""
