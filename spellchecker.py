def load_words(file_name):
	words = open(file_name).readlines()
	words = map(lambda x: x.strip(), words)
	return words

def check_word(words, word):
	return word in words
	

def check_words(words, sentence):
	for word in sentence.split(' '):
		if not check_word(words, word):
			print(word, word in words, "does not exist")
			return False
		else:
			print(word, "does exist")
	return True
		



words = load_words('spell.words')
word = 'zygotic'
print (check_word(words, word)) 
print check_words(words, "the fox did jump")