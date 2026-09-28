import math
x = [
    [2, 50],
    [3, 60],
    [7, 85],
    [8, 90]
]

y = ["Fail", "Fail", "Pass", "Pass"]

new = [6, 80]
k = 3

# Step 1: Calculate distance
distance = []

for i in range(len(x)):
    d = math.sqrt((x[i][0] - new[0]) ** 2 + (x[i][1] - new[1]) ** 2)

    distance.append((d, y[i]))

# Step 2: Sort by distance
distance.sort()

# Step 3: Take K nearest
nearest = distance[:k]

#print("Nearest:", nearest)

# Step 4: Count Pass and Fail
pass_count = 0
fail_count = 0

for d, label in nearest:
    if label == "Pass":
        pass_count += 1
    else:
        fail_count += 1

# Step 5: Prediction
if pass_count > fail_count:
    print("Prediction: Pass")
else:
    print("Prediction: Fail")