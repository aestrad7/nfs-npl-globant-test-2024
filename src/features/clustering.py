import umap
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.manifold import TSNE
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import silhouette_score, calinski_harabasz_score, davies_bouldin_score

class Cluster:
    """Class for applying dimensionality reduction and visualizing clusters."""
    
    def __init__(self) -> None:
        pass

    def apply_dimensionality_reduction(self, method, data, n_components=2, **kwargs):
        """
        Applies dimensionality reduction using the specified method.
        
        Args:
        method (str): A string specifying 'PCA', 't-SNE', or 'UMAP'.
        data (DataFrame or NumPy array): The data to be reduced.
        n_components (int): Number of components for the reduction.
        **kwargs: Additional arguments specific to the method.
        
        Returns:
        array: Data transformed to a lower-dimensional space.
        """
        if method == 'PCA':
            model = PCA(n_components=n_components, **kwargs)
        elif method == 't-SNE':
            model = TSNE(n_components=n_components, **kwargs)
        elif method == 'UMAP':
            model = umap.UMAP(n_components=n_components, **kwargs)
        else:
            raise ValueError(f"Unsupported method: {method}")
        
        return model.fit_transform(data)
    
    def visualize_clusters_3d(self, data, cluster_labels, cluster_column_name, best_k=10):
        """
        Visualizes clusters in a 3D plot using PCA, t-SNE, and UMAP.

        Args:
        data (DataFrame or array): The data to be visualized.
        cluster_labels (array): The labels for the clusters.
        cluster_column_name (str): The name of the cluster column.
        best_k (int): The number of clusters considered optimal.
        """
        pca_result = self.apply_dimensionality_reduction('PCA', data, n_components=3)
        tsne_result = self.apply_dimensionality_reduction('t-SNE', data, n_components=3, init='random', perplexity=30)
        umap_result = self.apply_dimensionality_reduction('UMAP', data, n_components=3, n_neighbors=15, min_dist=0.1)
        
        fig = plt.figure(figsize=(18, 6))
        titles = ['PCA Clustering', 't-SNE Clustering', 'UMAP Clustering']
        results = [pca_result, tsne_result, umap_result]

        for i, (result, title) in enumerate(zip(results, titles), start=1):
            ax = fig.add_subplot(1, 3, i, projection='3d')
            sc = ax.scatter(result[:, 0], result[:, 1], result[:, 2], c=cluster_labels, cmap='viridis', s=50, alpha=0.6)
            ax.set_title(title)

        fig.colorbar(sc, ax=ax, orientation='horizontal', label=cluster_column_name, shrink=0.5)
        plt.show()

    def find_optimal_k(self, X, start_k=2, end_k=10, random_state=0):
        """
        Finds the optimal number of clusters (k) using various metrics.

        Args:
        X (array): The data for clustering.
        start_k (int): The starting number of clusters.
        end_k (int): The ending number of clusters.
        random_state (int): Random state for reproducibility.

        Returns:
        None: This function only plots the results.
        """
        silhouette_avg_scores = []
        calinski_harabasz_scores = []
        davies_bouldin_scores = []
        
        X_dense = X.toarray()  # Convert to dense matrix once outside the loop
        
        for k in range(start_k, end_k + 1):
            kmeans = KMeans(n_clusters=k, random_state=random_state)
            kmeans.fit(X_dense)
            
            labels = kmeans.labels_
            
            silhouette_avg_scores.append(silhouette_score(X_dense, labels))
            calinski_harabasz_scores.append(calinski_harabasz_score(X_dense, labels))
            davies_bouldin_scores.append(davies_bouldin_score(X_dense, labels))
        
        plt.figure(figsize=(20, 5))
        
        plt.subplot(1, 3, 1)
        plt.plot(range(start_k, end_k + 1), silhouette_avg_scores, marker='o')
        plt.xlabel('Number of Clusters (k)')
        plt.ylabel('Silhouette Score')
        plt.title('Silhouette Score vs Number of Clusters')
        
        plt.subplot(1, 3, 2)
        plt.plot(range(start_k, end_k + 1), calinski_harabasz_scores, marker='o')
        plt.xlabel('Number of Clusters (k)')
        plt.ylabel('Calinski-Harabasz Score')
        plt.title('Calinski-Harabasz Score vs Number of Clusters')
        
        plt.subplot(1, 3, 3)
        plt.plot(range(start_k, end_k + 1), davies_bouldin_scores, marker='o')
        plt.xlabel('Number of Clusters (k)')
        plt.ylabel('Davies-Bouldin Score')
        plt.title('Davies-Bouldin Score vs Number of Clusters')
        
        plt.show()
