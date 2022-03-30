
import numpy as np
import matplotlib.pyplot as plt
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import Flatten
from keras.layers.convolutional import Convolution2D
from keras.layers.convolutional import MaxPooling2D
from keras.models import Sequential
from sklearn.preprocessing import LabelEncoder
from keras.utils import np_utils
from preprocessing_img import LoadDataset
from sklearn.model_selection import train_test_split

#fix random seed for reproducibility
seed = 7
np.random.seed(seed)

#load dataset
(X, y) = LoadDataset.loadDataset()

#normalize dataset from 0-255 to 0.0-1.0
X = X.astype("float32")
X /= 255.0
print(X.shape)
#encode class values as integers
encoder = LabelEncoder()
encoder.fit(y)
encoded_y = encoder.transform(y)


#convert integers to dummy variables (i.e one hot encoded)
y = np_utils.to_categorical(encoded_y)

#split varibles into train (67%) and test (33%) variables
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=seed)

#create the model
model = Sequential()
model.add(Convolution2D(32, (3, 3), input_shape=(150, 150, 3), activation="relu"))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Convolution2D(32, (3, 3), activation="relu"))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Convolution2D(64, (3, 3), activation="relu"))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Flatten())
model.add(Dense(64, activation="relu"))
model.add(Dropout(0.5))
model.add(Dense(6, activation="sigmoid"))
model.compile(loss='categorical_crossentropy', optimizer='rmsprop', metrics=['accuracy'])


history = model.fit(X_train, y_train, epochs=40, batch_size=32, validation_data=(X_test, y_test), verbose=2)

# summarize history for accuracy
plt.plot(history.history['acc'])
plt.plot(history.history['val_acc'])
plt.title('Learning curve')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='lower right')
plt.show()


#serialize model to JSON
model_json = model.to_json()
with open("model_v31.json", "w") as json_file:
    json_file.write(model_json)

#serialize weights to HDF5
model.save_weights("model_v31.h5")
print("Saved model to disk")