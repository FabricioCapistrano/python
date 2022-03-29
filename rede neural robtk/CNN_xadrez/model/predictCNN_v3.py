#load json and create model
from keras.models import model_from_json
import LoadDataset
from sklearn.preprocessing import LabelEncoder
from keras.utils import np_utils
import numpy as np
import cv2
from scipy import misc
import glob

#read file
json_file = open("model_v31.json", "r")
load_model_json = json_file.read()
json_file.close()

#load model
model = model_from_json(load_model_json)

#load weights into model
model.load_weights("model_v31.h5")

#compile model and evaluate
model.compile(loss="binary_crossentropy", optimizer="rmsprop", metrics=["accuracy"])



#load sample
file = ("/home/pi/Desktop/base imagem xadrez/teste/Rainha/20171110_143414.jpg")

img = misc.imread(file)
X = cv2.resize(img, (150, 150))
#X = img
X = X.astype("float32")
X /= 255.0
sc = model.predict_classes(np.array([X]))
cl = ["Bispo", "Cavalo", "Rei", "Rainha", "Torre", "Peão"]

print(cl[sc[0]])


