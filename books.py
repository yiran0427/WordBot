import os
from format_words import alternative_gen_dict
from book_to_sentences import parse_to_sentences

class Book:
	"""
	Prepocess a text file to remove funny characters
	Parse text to sentences and store in array
	Parse sentences to words and ...
	Construct array of triplets (word, frequency, index_to_example_phrase)
	Include meta-data of book and additional statistics
	"""

	# misc 
	author = ""
	title = ""
	date = ""

	# stats
	total_word_count = 0
	unique_word_count = 0
	sentence_count = 0
	average_word_frequency = 0
	average_word_length = 0

	# arrays
	sentences = [] # ["Hello, world!", "My name is Fahim.", ...]

	# dictionaries
	words = {} # {{"Hello", 1, 0}, {"World", 1, 0}, {"My", 1, 1}, ...}


	# Methods
	def __init__(self, path_to_text_file_in_dir, author="", title="", date=""):
		"""
		Input: text file
		Output: processed Book object
		"""
		self.author = author
		self.title = title
		self.date = date
		self.sentences = parse_to_sentences(path_to_text_file_in_dir)
		self.words = alternative_gen_dict(self.sentences)
		self.total_word_count = sum(list(map(lambda k: (self.words[k])['freq'], self.words)))
		self.unique_word_count = len(self.words)
		self.sentence_count = len(self.sentences)
		self.average_word_frequency = self.total_word_count / self.unique_word_count
		self.average_word_length = sum(list(map(lambda k: ((self.words[k])['length'])*((self.words[k])['freq']), self.words))) / self.total_word_count

	def __str__(self):
		str_rep = "{} \n{} \n{} \nTotal Word Count: {} \nAvg Word Frequency: {} \nAverage word length: {}".format(self.author, self.title, self.date, \
			self.total_word_count, self.average_word_frequency, self.average_word_length)
		return str_rep


# Test
"""
counter = 1
for i in os.listdir("./"):
    if i[-3:] == "txt":
        text = Book(i, "Fahim Yusufzai", "How to win Hackathon " + str(counter), "11/06/97")
        counter += 1
        print(text)
"""

