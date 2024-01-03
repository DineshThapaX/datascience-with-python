# Porter Stemming Algorithm for stemming
import nltk
from nltk.stem.porter import PorterStemmer
porter_stemmer = PorterStemmer()

word_data = "It originated from the idea that there are readers who prefer learning new skills from the comforts of their drawing rooms"
# First Word tokenization
nltk_tokens = nltk.word_tokenize(word_data)
#Next find the roots of the word
for w in nltk_tokens:
       print ("Actual: %s  Stem: %s"  % (w,porter_stemmer.stem(w)))

print("\n")

# Lemmatization
nltk.download('wordnet')
import nltk
from nltk.stem import WordNetLemmatizer
wordnet_lemmatizer = WordNetLemmatizer()

word_data = "It originated from the idea that there are readers who prefer learning new skills from the comforts of their drawing rooms"
nltk_tokens = nltk.word_tokenize(word_data)
for w in nltk_tokens:
       print ("Actual: %s  Lemma: %s"  % (w,wordnet_lemmatizer.lemmatize(w)))