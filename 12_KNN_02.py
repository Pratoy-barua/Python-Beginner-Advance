from sklearn.neighbors import KNeighborsClassifier
x= [
    [2,50],
    [3,60],
    [7,85],
    [8,90]
]

y= [
    "Fail", "Fail", "Pass", "Pass"
]

model = KNeighborsClassifier(n_neighbors= 3)
model.fit(x,y)
print(model.predict([[6,80]])) #how to use multiple values