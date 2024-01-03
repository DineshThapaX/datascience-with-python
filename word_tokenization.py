# Python - Word Tokenization
import nltk

word_data = "It originated from the idea that there are readers who prefer learning new skills from the comforts of their drawing rooms"
nltk_tokens = nltk.word_tokenize(word_data)
print (nltk_tokens)

# Tokenizing Sentences
import nltk
sentence_data = "Sun rises in the east. Sun sets in the west."
nltk_tokens = nltk.sent_tokenize(sentence_data)
print (nltk_tokens)

