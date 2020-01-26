from books import Book

def aggregate_sentences(list_of_books):
	aggregate_sentences = []
	for book in list_of_books:
		for sentence in book.sentences:
			aggregate_sentences.append(sentence)
	return aggregate_sentences