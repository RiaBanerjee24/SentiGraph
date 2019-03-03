from sklearn.naive_bayes import BernoulliNB
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.utils import shuffle


# Get data
train_df = pd.read_csv('Sentiment140.csv', encoding='latin-1')
train_df = shuffle(train_df)
# Vectorize data
vectorize = CountVectorizer()
X = vectorize.fit_transform(train_df.text)
Y = train_df.target

# Split data
X_train, x_test, y_train, Y_test = train_test_split(X, Y, train_size=0.8)

#Predict
clf = BernoulliNB()
clf.fit(X_train,y_train)
predicted = clf.predict(x_test)
accuracy = accuracy_score(Y_test,predicted)

print(accuracy)
#gives an accuracy of 0.8240668332411452
# 0.823785500391005
