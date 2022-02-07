# pylint: disable=invalid-name
"""
ex04
input: python Kmeans.py filepath='../ressources/solar_system_census.csv' ncentroid=4 max_iter=30
"""

from matplotlib import pyplot
from mpl_toolkits.mplot3d import Axes3D
from sklearn.cluster import KMeans

import argparse
import itertools
import pandas
import numpy
import sys


class KmeansClustering:
    def __init__(self, max_iter=20, ncentroid=5):
        self.ncentroid = ncentroid # number of centroids
        self.max_iter = max_iter # number of max iterations to update the centroids
        self.centroids = [] # values of the centroids

    def fit(self, X):
        """
        Run the K-means clustering algorithm.
        For the location of the initial centroids, random pick ncentroids from the dataset.
        """
        #km = KMeans(init='random', n_clusters=self.ncentroid, n_init=self.max_iter)
        pass

    def predict(self, X):
        """
        Predict from wich cluster each datapoint belongs to.
        """
        pass


def main(*args):
    parser = argparse.ArgumentParser(prog='kmeans', description='Implementation of a basic Kmeans algorithm.')

    parser.add_argument('--version', action='version', version='%(prog)s 0.1')
    #parser.add_argument('-f', '-filepath', '--filepath', nargs=1, type=argparse.FileType('r'), required=True)
    parser.add_argument('-f', '-filepath', '--filepath', type=str, required=True)
    parser.add_argument('-n', '-ncentroid', '--ncentroid', type=int)
    parser.add_argument('-m', '-max_iter', '--max_iter', type=int)

    args = parser.parse_args()

    # Get data and clean it from csv
    raw = pandas.read_csv(args.filepath)
    mask = raw.columns.str.match("Unnamed")
    points = raw.loc[:,~mask]

    # Get header list
    headers = list(points.columns)

    # kmeans fit
    km = KMeans(n_clusters=args.ncentroid, n_init=args.max_iter)
    km.fit(points[headers])
    # Predict
#    predicted = km.predict(points)
#    # Update data with cluster number
#    points['cluster'] = predicted
    #print(km.labels_)


    # Plot list
    fig = pyplot.figure()
    ax = fig.add_subplot(projection='3d')

    markers = iter(('o', 'v', 's', 'D', '+'))

    for centroid in range(args.ncentroid):
        mask = km.labels_ == centroid
        print(sum(mask), 'elements in centroid', centroid, 'with coordinates', km.cluster_centers_[centroid])
        ax.scatter(points[headers[0]][mask], points[headers[1]][mask], points[headers[2]][mask], marker=next(markers))

    ax.scatter(km.cluster_centers_[:,0], km.cluster_centers_[:,1], km.cluster_centers_[:,2], c='r', marker='X')

    ax.set_xlabel(headers[0])
    ax.set_ylabel(headers[1])
    ax.set_zlabel(headers[2])

    pyplot.show()



if __name__ == '__main__':
    main()
