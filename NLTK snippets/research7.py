from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

# print(lemmatizer.lemmatize("cats"))
# print(lemmatizer.lemmatize("cacti"))
# print(lemmatizer.lemmatize("geese"))
print(lemmatizer.lemmatize("tallest",pos="a"))