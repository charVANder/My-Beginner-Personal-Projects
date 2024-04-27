'''
Evangeline Kim
April 10th, 2024
K-means Clustering Program
'''
# Necessary Imports
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs # I love this name, also this just makes the visualization prettier (not actually required)

def make_centroids(k, data_points):
    '''Function make_centroids generates random starting centroids within the max/min boundaries of the data points.
    np.random.uniform generates random numbers b/w the min and max values for each feature in the dataset.
    The output is an array of shape (k, num_features), where k is the number of centroids and num_features is the number
    of features in the dataset (dimensions in the array). Each row in the centroids array represents a centroid, and
    each column represents a feature. These centroids are randomly generated within the range of the dataset's feature values.
    Parameters: The number of centroids to generate (k), and an array of all the data_points (data_points)
    Returns: An array of all the randomly generated centroids (centroids)
    '''
    return np.random.uniform(np.amin(data_points, axis=0), np.amax(data_points, axis=0), size=(k, data_points.shape[1]))

def get_distance(data_point, centroids):
    '''Function get_distance calculates the Euclidean distance between a data point and all centroids.
    Parameters: The data point in questions (data_point), and the array of centroids to calculate distances from (centroids).
    Returns: An array of all the euclidean distances b/w the data point and all the centroids.
    '''
    return np.sqrt(np.sum((centroids - data_point)**2, axis=1))

def assign_clusters(data_points, centroids):
    '''Function assign_clusters assigns each data point to the nearest centroid based on the Euclidean distance.
    Parameters: The array of data_points (data_points), and the array of centroids (centroids).
    Returns: An array with an index assignment of the nearest centroid for each data point.
    '''
    cluster_labels = []
    for data_point in data_points: # Iterate through each data point
        distances = get_distance(data_point, centroids) # Getting Euclidean distance
        cluster_num = np.argmin(distances)  # Assigning to the closest cluster
        cluster_labels.append(cluster_num)
    return np.array(cluster_labels)

def update_centroids(data_points, cluster_labels, centroids):
    '''Function update_centroids updates the centroids based on the mean of data points assigned to each cluster.
    Parameters: The array of data points (data_point), the array of cluster labels for each data point (cluster_labels),
    and the array of centroids (centroids).
    Returns: The array of all the updated centroids.
    '''
    cluster_indices = [] # Grouping by cluster
    # Iterating over each centroid, finding the indices of data points belonging to each cluster
    for i in range(len(centroids)):
        indices = np.argwhere(cluster_labels == i).flatten()
        cluster_indices.append(indices)

    cluster_centers = [] #Assigning new clusters
    # Iterating over each cluster, calculating the mean, assigning new centroid
    for i, indices in enumerate(cluster_indices):
        if len(indices) != 0: # Check if data points assigned to current cluster
            centroid = np.mean(data_points[indices], axis=0) # Calculating mean
        else: # If there are no data points assigned to the cluster, keep the centroid unchanged
            centroid = centroids[i]        
        cluster_centers.append(centroid)
    return np.array(cluster_centers)

def kmeans(data_points, k=3, iterations=300):
    '''Function kmeans implements the actual K-means clustering algorithm using previous functions.
    Parameters: The array of data points (data_points), the number of clusters w/ default 3 (k), and the
    max number of iterations w/ default 300 (iterations)
    Returns: A tuple containing an array of cluster labels for each data point, and an array containing the centroids.
    '''
    centroids = make_centroids(k, data_points) # Creating the centroids
    # Iterating to assign data points to the clusters and updating them.
    for i in range(iterations):
        cluster_labels = assign_clusters(data_points, centroids)
        new_centroids = update_centroids(data_points, cluster_labels, centroids)

        # Checking if means did not change much b/w iterations. If stable, you can stop early, otherwise, continue.
        if np.max(centroids - new_centroids) < 0.0001:
            break
        else:
            centroids = new_centroids
    return cluster_labels, centroids


def main():
    '''Generate data, run K-means clustering, and plot into a scatter plot.
    '''
    # Generating the fake data. 100 data points, 2 dimensions, 3 clusters.
    # make_blobs() generates isotropic Gaussian blobs for clustering. It makes the visualizations better.
    data = make_blobs(n_samples=100, n_features=2, centers=3)
    data_points = data[0] # Ignore the cluster labels

    # Running K-means clustering
    labels, centroids = kmeans(data_points)

    #Generating the scatter plot visualization
    plt.scatter(data_points[:, 0], data_points[:, 1], c=labels)
    plt.scatter(centroids[:, 0], centroids[:, 1], c=range(len(centroids)), marker='*', s=200, edgecolors='red')
    plt.title('K-means Clustering Scatter Plot')
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')
    plt.legend(['Data Points', 'Centroids'], title='Legend')
    plt.show()

if __name__ == "__main__":
    main()