import re
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer
from bs4 import BeautifulSoup

def html_docode(text):
    return [BeautifulSoup(article, "html").text for article in text]# HTML decoding. BeautifulSoup's text attribute will return a string stripped of any HTML tags and metadata.


def clean_text(text):
    REPLACE_BY_SPACE_RE = re.compile('[/(){}\[\]\|@,;\\n]')
    BAD_SYMBOLS_RE = re.compile('[^0-9a-z #+_]')
    STOPWORDS = set(stopwords.words('english'))
    cleaned_text = [article.lower() for article in text]# lowercase text
    cleaned_text = [REPLACE_BY_SPACE_RE.sub(' ', article)  for article in cleaned_text] # replace REPLACE_BY_SPACE_RE symbols by space in text. substitute the matched string in REPLACE_BY_SPACE_RE with space.
    cleaned_text = [BAD_SYMBOLS_RE.sub('', article) for article in cleaned_text] # remove symbols which are in BAD_SYMBOLS_RE from text. substitute the matched string in BAD_SYMBOLS_RE with nothing. 
    cleaned_text = [re.sub(r'[0-9]+','', article) for article in cleaned_text] #remove numbers
    return [' '.join(word for word in article.split() if (word not in STOPWORDS and len(word) >3)) for article in cleaned_text] 
    
def stemm_text(text):
    stemmer = PorterStemmer()
    return [' '.join([stemmer.stem(word) for word in review.split()]) for review in text]

def lemmatize_text(text):
    lemmatizer = WordNetLemmatizer()
    return [' '.join([lemmatizer.lemmatize(word) for word in review.split()]) for review in text]