



from sklearn.datasets.samples_generator import make_blobs
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from sklearn.cluster import KMeans



dataset = pd.read_csv("boardgeekgame_dataset.csv")

df = pd.DataFrame(dataset)

print(df.describe())


X = dataset.iloc[:,[1,3]].values #ave rating

Y = X
Y[:,1] = X[:,1]*0.0001 

#Y = dataset.iloc[:,[3]].values


#X,Y = make_blobs(n_samples=400, centers=4, 
#   cluster_std=0.80, random_state=0)



#plt.scatter(X,Y)
#plt.savefig('scatterplot.png')

def run_kmeans(n):
    kmeans = KMeans(n_clusters=n)
    kmeans.fit(Y)
    kmeans_results = kmeans.predict(Y)

    print(kmeans_results)

    plt.scatter(Y[:, 0],Y[:,1], c=kmeans_results)
    plt.savefig('scatterplot_color.png')

run_kmeans(4)

