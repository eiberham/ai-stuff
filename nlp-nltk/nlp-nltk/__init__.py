import nltk
from nltk.stem import WordNetLemmatizer

# This line downloads the 'punkt_tab' tokenizer models from 
# the nltk data repository. The 'punkt' tokenizer is used 
# for tokenizing text into sentences or words.

# The 'punkt' tokenizer in the Natural Language Toolkit (nltk) 
# is a pre-trained model that is used for tokenizing text into 
# sentences or words. It is an unsupervised machine learning 
# method for sentence boundary detection that can be used to 
# split a text into a list of sentences or words.
nltk.download('punkt_tab')

# The 'stopwords' and 'wordnet' are two other datasets that
# are used in this example. The 'stopwords' dataset contains
# a list of common words that are often removed from text
# before processing. The 'wordnet' dataset contains a list
# of words that are used to lemmatize text. Lemmatization is
# the process of reducing words to their base or root form.
nltk.download('stopwords')
nltk.download('wordnet')

# Tokenization
# Tokenization is the process of breaking text into individual 
# tokens

text = "This is a simple text"
tokens = nltk.word_tokenize(text)
print(tokens)

# Preprocessing
# Preprocessing is the process of cleaning and normalizing data
# for training NLP models. This includes:
# 1. Stopword removal: Removing common words like "the", "and", 
# etc. that don't add much value to the model.
# 2. Stemming or Lemmatization: Reducing words to their base form 
# (e.g., "running" becomes "run").
# 3. Removing special characters and punctuation

# Remove stopwords and stem words using `nltk.stem`
stop_words = set(nltk.corpus.stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

filtered_tokens = [token for token in tokens if token.lower() not in stop_words]
stemmed_tokens = [lemmatizer.lemmatize(token) for token in filtered_tokens]

#Text Representation
#Text representation is the process of converting text to 
# numerical representations that can be processed by machines
print(stemmed_tokens)
