#list is mutable and tuple is immutable, we cant change the values of tuple once it is created.

tuple1 = (1, 2, 3, 4, 5, 2, 3, 4, 5, 6, 7, 8, 9)
print(type(tuple1))
print(tuple1)
print(tuple1[1]) #indexing
print(tuple1.index(3)) #index method, 3 er index number return korbe
print("count of 2:", tuple1.count(2)) #count method, 2 kotobar ache seta return korbe

tup1= (1)
print(type(tup1)) #this is not a tuple, this is an integer

tup2=(1,) #this is a tuple, this is a single element tuple
print(type(tup2))

tup3=("hello",)
print(tup3)