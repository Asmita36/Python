## support vector machine
from sklearn import svm      
import numpy as np
import matplotlib.pyplot as plt

landslide = [[0],[100]]
action = ['Landslide Predicted', 'Landslide Detected']

clf = svm.SVC(gamma = 'scale')
clf.fit(landslide,action)


landslide = float(input('Enter Value'))
print(clf.predict([[landslide]]))
plt.plot(landslide,'ro')
plt.show()


