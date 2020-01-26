import os 
import numpy as np 
import math
from books import Book
from collection_of_words import aggregate_words
from collection_of_sentences import aggregate_sentences

class Collection:
	"""
	Collection represents a library of Book class objects
	It should be used to check aggregate summary of statics over all Book instances
	"""

	# stats
	book_count = 0
	total_word_count = 0
	unique_word_count = 0
	sentence_count = 0
	average_word_frequency = 0
	average_word_length = 0
	deviation_frequency = 0
	deviation_length = 0

	# arrays
	books = []
	sentences = [] # ["Hello, world!", "My name is Fahim.", ...]

	# dictionaries
	words = {} # {{"Hello", 1, 0}, {"World", 1, 0}, {"My", 1, 1}, ...}

	def __init__(self, list_of_books):
		"""
		Input: Orderd list of Book instances
		"""
		self.books = list_of_books
		self.sentences = aggregate_sentences(list_of_books)
		self.words = aggregate_words(list_of_books)
		self.book_count = len(list_of_books)
		self.total_word_count = sum(list(map(lambda k: (self.words[k])['freq'], self.words)))
		self.unique_word_count = len(self.words)
		self.sentence_count = len(self.sentences)
		self.average_word_frequency = self.total_word_count / self.unique_word_count
		self.average_word_length = sum(list(map(lambda k: ((self.words[k])['length'])*((self.words[k])['freq']), self.words))) / self.total_word_count

		# Calculating deviations
		count = 0
		for word in self.words:
			length = ((self.words)[word])['length']
			frequency = ((self.words)[word])['freq']
			count += ((frequency - self.average_word_frequency)**2)
		self.deviation_frequency = math.sqrt(count/(self.total_word_count))

		count = 0
		for word in self.words:
			length = ((self.words)[word])['length']
			frequency = ((self.words)[word])['freq']
			count += (frequency * ((length - self.average_word_length)**2))
		self.deviation_length = math.sqrt(count/(self.total_word_count))

	def __str__(self):
		str_rep = "List of books:"
		for book in self.books:
			str_rep += (" " + book.title)
		str_rep += "\nTotal Word Count: {}\nAvg Word Frequency: {}\nAverage word length: {} \n{} \n{}".format(self.total_word_count, \
			self.average_word_frequency, self.average_word_length, self.deviation_frequency, self.deviation_length)
		return str_rep

# Test 
"""
counter = 1
list_of_books = []
for i in os.listdir("./"):
    if i[-3:] == "txt":
        text = Book(i, "Fahim Yusufzai", "How to win Hackathon " + str(counter), "11/06/97")
        list_of_books.append(text)
        counter += 1
collection = Collection(list_of_books)
print(collection)
print(collection.words["director"])
print(collection.sentences[0])
"""

