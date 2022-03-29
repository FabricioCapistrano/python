#load json and create model
from keras.models import model_from_json
from preprocessing_img import LoadDataset
from sklearn.preprocessing import LabelEncoder
from keras.utils import np_utils
import matplotlib.pyplot as plt
import numpy as np
from plot_class import ConfusionMatrix
from sklearn.metrics import confusion_matrix

#read file
json_file = open("model_v31.json", "r")
load_model_json = json_file.read()
json_file.close()

#load model
model = model_from_json(load_model_json)

#load weights into model
model.load_weights("model_v31.h5")

#compile model and evaluate
model.compile(loss="categorical_crossentropy", optimizer="rmsprop", metrics=["accuracy"])

#load dataset
X, y = LoadDataset.loadTestDataSet()

#normalize dataset from 0-255 to 0.0-1.0
X = X.astype("float32")
X /= 255.0

yp = model.predict_classes(X, verbose=0)

yp = yp.reshape(len(yp), 1)

print(yp.shape)
print(y.shape)
print("Acertos:", sum(y==yp)/len(y))
print("Erros: ", sum(y!=yp)/len(y))

np.set_printoptions(precision=2)
class_names = ["C0","C1", "C2", "C3", "C4", "C5"]
confusionMatrix = confusion_matrix(y, yp)
plt.figure()
ConfusionMatrix.plot_confusion_matrix(confusionMatrix, classes=class_names, title='Confusion matrix')
plt.show()

