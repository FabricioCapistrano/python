import cv2
from scipy import misc
import numpy as np
import glob

def getImgByClass(path, category):
    files = glob.glob(path)
    X = []
    y = []
    for f in files:
        img = misc.imread(f)
        resized = cv2.resize(img, (150, 150))
        X.append(resized)
        y.append([category])
    return X, y

def loadDataset():
    "/Users/renatohidaka/Google Drive/IFPA/LABOTICA/base imagem xadrez/treino"
    (X1, y1) = getImgByClass("/Users/renatohidaka/Google Drive/IFPA/LABOTICA/base imagem xadrez/treino/Bispo/*.jpg", 0)
    (X2, y2) = getImgByClass("/Users/renatohidaka/Google Drive/IFPA/LABOTICA/base imagem xadrez/treino/Cavalo/*jpg", 1)
    (X3, y3) = getImgByClass("/Users/renatohidaka/Google Drive/IFPA/LABOTICA/base imagem xadrez/treino/Rei/*.jpg", 2)
    (X4, y4) = getImgByClass("/Users/renatohidaka/Google Drive/IFPA/LABOTICA/base imagem xadrez/treino/Rainha/*.jpg", 3)
    (X5, y5) = getImgByClass("/Users/renatohidaka/Google Drive/IFPA/LABOTICA/base imagem xadrez/treino/Torre/*.jpg", 4)
    (X6, y6) = getImgByClass("/Users/renatohidaka/Google Drive/IFPA/LABOTICA/base imagem xadrez/treino/Peão/*.jpg", 5)

    X = np.concatenate([X1,X2,X3,X4,X5,X6], axis=0)
    y = np.concatenate([y1,y2,y3,y4,y5,y6], axis=0)


    return X,y

def loadTestDataSet():
    (X1, y1) = getImgByClass("/Users/renatohidaka/Documents/IFPA/LABOTICA/base imagem xadrez/teste/Bispo/*.jpg", 0)
    (X2, y2) = getImgByClass("/Users/renatohidaka/Documents/IFPA/LABOTICA/base imagem xadrez/teste/Cavalo/*jpg", 1)
    (X3, y3) = getImgByClass("/Users/renatohidaka/Documents/IFPA/LABOTICA/base imagem xadrez/teste/Rei/*.jpg", 2)
    (X4, y4) = getImgByClass("/Users/renatohidaka/Documents/IFPA/LABOTICA/base imagem xadrez/teste/Rainha/*.jpg", 3)
    (X5, y5) = getImgByClass("/Users/renatohidaka/Documents/IFPA/LABOTICA/base imagem xadrez/teste/Torre/*.jpg", 4)
    (X6, y6) = getImgByClass("/Users/renatohidaka/Documents/IFPA/LABOTICA/base imagem xadrez/teste/Peão/*.jpg", 5)


    X = np.concatenate([X1,X2,X3,X4,X5], axis=0)
    y = np.concatenate([y1,y2,y3,y4,y5], axis=0)
    print(X.shape)
    return X, y
