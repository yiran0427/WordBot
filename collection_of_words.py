from books import Book

def aggregate_words(list_of_books):
	"""
	Create a database of words aggregated over a list of books
	Make sure to account for duplicate words
	"""
	temp = {}
	current_sum_of_sentences = 0
	for book in list_of_books:
		for word in book.words:
			frequency = ((book.words)[word])['freq']
			length = ((book.words)[word])['length']
			list_of_indicies_wrt_book = ((book.words)[word])['indicies']
			list_of_indicies_wrt_collection = [x + current_sum_of_sentences for x in list_of_indicies_wrt_book]
			if word in temp:
				(temp[word])['freq'] += frequency
				for index in list_of_indicies_wrt_collection:
					if index not in (temp[word])['indicies']:
						(temp[word])['indicies'].append(index)
			else:
				(temp[word]) = {'freq':frequency, 'length':length, 'indicies':list_of_indicies_wrt_collection}
		current_sum_of_sentences += book.sentence_count
	return temp
