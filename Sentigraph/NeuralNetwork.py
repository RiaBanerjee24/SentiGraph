import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

from sklearn.feature_extraction.text import CountVectorizer
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras.layers import Dense, Embedding, LSTM, SpatialDropout1D
from sklearn.model_selection import train_test_split
from keras.utils.np_utils import to_categorical
import re

data = pd.read_csv('Sentiment140.csv',encoding='latin-1')
data = data[['text','target']]

max_features = 2000
tokenizer = Tokenizer(num_words=max_features,split=' ')
tokenizer.fit_on_texts(data['text'].values)
X = tokenizer.texts_to_sequences(data['text'].values)
X = pad_sequences(X)

embed_dim = 128
lstm_out = 196

model = Sequential()  #Linear stack of layers
model.add(Embedding(max_features,embed_dim,input_length=X.shape[1]))   #Turns positive integers (indexes) into dense vectors of fixed size.
model.add(SpatialDropout1D(0.4)) #drops entire 1D feature maps
model.add(LSTM(lstm_out,dropout=0.2,recurrent_dropout=0.2))
model.add(Dense(2,activation='softmax'))
model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy'])

Y = pd.get_dummies(data['target']).values
X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.33,random_state=42)

batch_size = 32
model.fit(X_train,Y_train,epochs=7,batch_size=batch_size,verbose=2)

validation_size = 1500
X_validate = X_test[-validation_size:]
Y_validate = Y_test[-validation_size:]
X_test = X_test[:-validation_size]
Y_test = Y_test[:-validation_size]
score,acc = model.evaluate(X_test, Y_test, verbose = 2, batch_size = batch_size)
print("score: %.2f" % (score))
print("acc: %.2f" % (acc))

#score: 0.33
#acc: 0.86

