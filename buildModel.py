import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer, TfidfVectorizer
from sklearn import feature_extraction, linear_model, model_selection, preprocessing
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.utils import shuffle
from sklearn.linear_model import PassiveAggressiveClassifier
import pickle
import string
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
stop = stopwords.words('english')

fake = pd.read_csv("data/Fake.csv")
true = pd.read_csv("data/True.csv")

fake['target'] = 'fake'
true['target'] = 'true'

data = pd.concat([fake, true]).reset_index(drop=True)
data = shuffle(data)
data = data.reset_index(drop=True)

data.drop(["date"], axis=1, inplace=True)
data.drop(["subject"], axis=1, inplace=True)


def punctuation_removal(text):
    all_list = [char for char in text if char not in string.punctuation]
    clean_str = ''.join(all_list)
    return clean_str


data['text'] = data['text'].apply(punctuation_removal)

data['text'] = data['text'].apply(lambda x: ' '.join([word for word in x.split() if word not in (stop)]))

# print(data)
# print(data.groupby(['target'])['text'].count())
# data.groupby(['target'])['text'].count().plot(kind="bar")
# plt.show()

X_train, X_test, Y_train, Y_test = train_test_split(data['text'], data.target, test_size=0.4, random_state=42)

pipe = Pipeline([('vect', TfidfVectorizer()),
                 ('tfidf', TfidfTransformer()),
                 ('model', PassiveAggressiveClassifier())])

model = pipe.fit(X_train, Y_train)
prediction = model.predict(X_test)
print("accuracy: {}%".format(round(accuracy_score(Y_test, prediction)*100, 2)))

model_file = "final_model.sav"
with open(model_file, 'wb') as file:
    pickle.dump(model, file)