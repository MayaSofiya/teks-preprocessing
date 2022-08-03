import re
import nltk
#nltk.download()
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

stp = stopwords.words('english')
stm = PorterStemmer()
lmtz = WordNetLemmatizer()


def lower(text):
    return text.lower()


def remove_punctuation(text):
    text = re.sub(r'[^\w\s]+', ' ', text) #cleaning 
    return text


def remove_stopwords(text):
    text = ' '.join([word for word in text.split() if word not in stp]) #stopword removal
    return text


def stem_text(text):
    text = ' '.join([stm.stem(word) for word in text.split()]) 
    return text


def lemmatize_text(text):
    text = ' '.join([lmtz.lemmatize(word) for word in text.split()]) 
    return text
