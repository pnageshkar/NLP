import string
import re
import pandas as pd
from nltk.tokenize import word_tokenize

def process_text(text):
    # lower text
    text = text.lower()
    # tokenize_text
    text = [word for word in word_tokenize(text)]
    # join all
    text = " ".join(text)
    return(text)

# Read the csv file in to a pandas dataframe
df = pd.read_csv('C:\\Users\\HP M6\\NLP\\Build_DomSp_Models\\Data\\stackexchange_812k.csv.gz', 
                 compression='gzip', header=0, sep=',', quotechar='"')
df.tail()

# Adds a new column 'Processed_text'
df['Processed_text'] = df['text'].apply(lambda x: process_text(x))

df.iloc[ : 999,:].to_csv('stackexchange_812k_v1.csv', index=False) # Save first 1000 rows to csv
