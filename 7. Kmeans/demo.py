import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.mixture import GaussianMixture
from sklearn.cluster import KMeans


data = pd.read_csv("fd.csv")
print("Input Data and Shape")
print(data.shape)
data.head()
print(data.head())

f1 = data["V1"].values
print("f1")
print(f1)
f2 = data["V2"].values

X = np.array(list(zip(f1, f2)))
print("x")
print(X)
print("Graph for whole dataset")
plt.scatter(f1, f2, c="black")
plt.show()

kmeans = KMeans(2, random_state=0)
labels = kmeans.fit(X).predict(X)
print("labels")
print(labels)
centroids = kmeans.cluster_centers_
print("centroids")
print(centroids)
plt.scatter(X[:, 0], X[:, 1], c=labels)
print("Graph using Kmeans Algorithm")
plt.scatter(centroids[:, 0], centroids[:, 1], marker="*", c="red")
plt.show()

gmm = GaussianMixture(n_components=2).fit(X)
labels = gmm.predict(X)
print("lLABELS GMM")
print(labels)
probs = gmm.predict_proba(X)
size = 10 * probs.max(1) ** 3
print("Graph using EM Algorithm")

plt.scatter(X[:, 0], X[:, 1], c=labels, cmap="viridis")
plt.show()