#list

thislist = ["apple", "banana", "cherry"]
print(thislist)

#list length
print(len(thislist))

list1 = ["kola", 34, 4.56, True]
print(list1)
print(type(list1))
print(list1[1]) 
print(list1[2:3])

#Range of Indexes
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5]) #index 2 to 4

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4]) #index 0 to 3

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:]) #index 2 to the end

mylist = ['apple', 'banana', 'cherry']
print(mylist[-1]) #prints the last item in the list

#change item list
list_1 = [10, 20, 30, 40, 50]
list_1[3] = 200 #index 3 is changed to 200
print(list_1)

mylist = ['apple', 'banana', 'cherry']
mylist[0] = 'kiwi'
print(mylist)
print(mylist[1])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

#insert item list
list_1 = [10, 20, 30, 40, 50]
list_1.insert(1, 200) ##insert korle ager data remove hoi na (index, element)
print(list_1)

#To add an item to the end of the list
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#extand list
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

#remove item list
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

#remove specific index
print("remove specific index")
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

#sort list
thislist = [20, 40, 100, 23, 55, 550]
thislist.sort()
print(thislist)

list4= ['a', 'x', 'c', 'b', 'e']
list4.sort()
print(list4)

#reverse list
thislist = ["apple", "banana", "cherry"]    
thislist.reverse()
print(thislist)
