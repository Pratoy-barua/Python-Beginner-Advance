from sklearn.cluster import KMeans #data gulo k group e vag kore

x= [
    [20,20],
    [22,25],
    [25,30],
    [40,80],
    [42,85],
    [45,90],
] #[age,spending]

model = KMeans(n_clusters=2, random_state=42) #n_clusters mane koita group hobe, random_state= centroid er position jeno random vabe choose kora na hoi
model.fit(x) #l-means algorithm kaj korche ay line e
print(model.labels_) #k kon group e gese sheta dekhabe
print(model.cluster_centers_) #cluster er final center dekhabe. gor ber kore