import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

# Training and testing data from Kaggle's Sentiment140. Data is split in two parts
# using train_test_split

# Get data
train_df = pd.read_csv('Sentiment140.csv', encoding='latin-1')

# Vectorize data
vectorize = CountVectorizer()
X = vectorize.fit_transform(train_df.text)
Y = train_df.target

# Split data
X_train,x_test, y_train, Y_test = train_test_split(X,Y,test_size=0.3)

#Train and predict data
clf = MultinomialNB()
clf.fit(X=X_train,y=y_train)
predicted = clf.predict(x_test)
#print(predicted)
print(accuracy_score(Y_test,predicted))

# prints an accuracy of 0.8293432684941174
# 0.8299695142304012
