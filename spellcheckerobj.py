class SpellChecker(object):
	def __init__(self):
		self.words = []
		
	def load_file(self, file_name):
		return map(lambda x: x.strip().lower(), open(file_name).readlines())
	
	def load_words(self, file_name):
		self.words = self.load_file(file_name)

	def check_word(self, word):
		return word.lower().strip('.') in self.words
	

	def check_words(self, sentence, index=1):
		failed_words = []
		caret_position = 0
		for word in sentence.split(' '):
			if not self.check_word(word):
				failed_words.append('word:'+word+'  line:'+str(index) + '   pos:'+str(caret_position))
			caret_position = caret_position + len(word) + 1
		return failed_words
		
	def check_document(self, file_name):
		sentences = self.load_file(file_name)
		failed_words_in_sentences = []
		for index, sentence in enumerate(sentences):
			failed_words_in_sentences.extend(self.check_words(sentence, index))
		return failed_words_in_sentences
		

if __name__ == '__main__':
	SpellChecker = SpellChecker()
	SpellChecker.load_words("spell.words")
	print(SpellChecker.words)
	print(SpellChecker.check_word('zygotic'))
	SpellChecker.check_words('the brown fox jumped over the moon xxxx')
