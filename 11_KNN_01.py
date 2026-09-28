from sklearn.neighbors import KNeighborsClassifier
x = [[2], [3], [7], [8]]
y = ["Fail", "Fail","Pass", "Pass"]

model = KNeighborsClassifier(n_neighbors=3)
model.fit(x,y)
prediction = model.predict([[6]])
print(prediction)