from sklearn.neighbors import KNeighborsClassifier
x = [[2], [3], [7], [8]]
y = ["Fail", "Fail","Pass", "Pass"]

model = KNeighborsClassifier(n_neighbors=3) #k = 3 means 3 ta ashe pasher value check korbe
model.fit(x,y) #model k training data dewa
prediction = model.predict([[6]]) #6h pora student er result ki hobe ber korbe
print(prediction)