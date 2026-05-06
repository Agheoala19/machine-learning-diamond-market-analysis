from sklearn.cluster import KMeans

def run_clustering(X, k=3):
    # Definirea problemei: Segmentarea automata a portofoliului de produse.
    # Metode: Algoritmul K-Means cu k centroidi.
    model = KMeans(n_clusters=k, n_init=10, random_state=42)
    clusters = model.fit_predict(X)
    return clusters
