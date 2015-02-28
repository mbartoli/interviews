
# coding: utf-8

# In[9]:

import numpy
from sklearn import neighbors, datasets
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap


# In[10]:

n_neighbors=15


# In[11]:

iris = datasets.load_iris()


# In[17]:

X = iris.data[:, :2]


# In[22]:

y = iris.target
h = 0.02


# In[23]:

cmap_light = ListedColormap(['#FFAAAA', '#AAFFAA', '#AAAAFF'])
cmap_bold = ListedColormap(['#FF0000', '#00FF00', '#0000FF'])


# In[26]:

for weights in ['uniform', 'distance']:
    clf = neighbors.KNeighborsClassifier(n_neighbors, weights=weights)
    clf.fit(X,y)
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = numpy.meshgrid(numpy.arange(x_min, x_max, h),
                            numpy.arange(y_min, y_max, h))
    Z = clf.predict(numpy.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    plt.figure()
    plt.pcolormesh(xx,yy,Z,cmap=cmap_light)
    plt.scatter(X[:,0],X[:,1], c=y, cmap=cmap_bold)
    plt.xlim(xx.min(), xx.max())
    plt.ylim(yy.min(), yy.max())
    plt.title("3-Class classification (k = %i, weights = '%s)"
              % (n_neighbors, weights))


# In[27]:

plt.show()


# In[ ]:



