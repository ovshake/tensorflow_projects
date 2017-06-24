from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk
nltk.download()
example_sentence = "This example shows off the stop words"
stop_words = set(stopwords.words("english"))
words = word_tokenize(example_sentence)
for w in words:
	if w not in stop_words:
		print(w)