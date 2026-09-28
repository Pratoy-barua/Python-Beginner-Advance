import math

data = [
    [1, 1],
    [2, 2],
    [8, 8],
    [9, 9]
]

centroid1 = [1, 1]
centroid2 = [8, 8]

for step in range(len(data)):

    cluster1 = []
    cluster2 = []

    # Assign points
    for point in data:

        d1 = math.sqrt(
            (point[0] - centroid1[0])**2 +
            (point[1] - centroid1[1])**2
        )

        d2 = math.sqrt(
            (point[0] - centroid2[0])**2 +
            (point[1] - centroid2[1])**2
        )

        if d1 < d2:
            cluster1.append(point)
        else:
            cluster2.append(point)

    # New centroid
    centroid1 = [
        sum(point[0] for point in cluster1) / len(cluster1),
        sum(point[1] for point in cluster1) / len(cluster1)
    ]

    centroid2 = [
        sum(point[0] for point in cluster2) / len(cluster2),
        sum(point[1] for point in cluster2) / len(cluster2)
    ]

print("Cluster 1:", cluster1)
print("Cluster 2:", cluster2)

print("Centroid 1:", centroid1)
print("Centroid 2:", centroid2)