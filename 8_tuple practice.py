# list1 =[]
# mv1 = input("Enter the first movie name: ")
# mv2 = input("Enter the second movie name: ")
# mv3 = input("Enter the third movie name: ")

# list1.append(mv1)
# list1.append(mv2)
# list1.append(mv3)
# print(list1)

#n number of movies
list = []
n = int(input("Enter the number of movies:"))
for i in range(n):
    mv = input("Enter the movie name: ")
    list.append(mv)

print(list)

