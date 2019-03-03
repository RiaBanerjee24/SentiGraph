import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score


# Get data
train_df = pd.read_csv('Sentiment140.csv', encoding='latin-1')

# Vectorize data
vectorize = CountVectorizer()
X = vectorize.fit_transform(train_df['text'])
Y = train_df['target']

# Split data
X_train,x_test, y_train, Y_test = train_test_split(X,Y,test_size=0.3)

#Train and predict data
clf = svm.LinearSVC(C=0.1)
clf.fit(X=X_train,y=y_train)
predicted = clf.predict(x_test)
#print(predicted)

print(accuracy_score(Y_test,predicted))

#Works slower than MultinomialNB
#0.8469099382337327
#0.8462900503221827
