x = [2, 3, 7, 8]
y = ["Fail", "Fail", "Pass", "Pass"]

new = 6
k = 3

#Calculate distance
distance = []

for i in range(len(x)):
    d = abs(x[i] - new) #abs absulate value means neg hole pos kore dy
    distance.append((d, y[i])) #distance r result ta rakha hocce, append means list e new kisu add kora

#Sort by distance
distance.sort()

#Take K nearest
nearest = distance[:k] #sort korar por 1st 3 ta result nibe

print("Nearest:", nearest) #konta konta value nisi dekhabe

#Count Pass and Fail
pass_count = 0
fail_count = 0

for d, label in nearest:
    if label == "Pass":
        pass_count += 1
    else:
        fail_count += 1

#Pass hobe naki fail check kora hocce
if pass_count > fail_count:
    print("Prediction: Pass")
else:
    print("Prediction: Fail")