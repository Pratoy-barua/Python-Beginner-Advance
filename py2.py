#input
name =input("Enter your name: ")
print("Hello, " + name + "! Welcome to the program.")

#val = int(input("Enter a number: ")) #python input k string hisabe nibe, tai amra int() use kore string ke integer e convert korechi
#print(type(val) , val)

val1 = input("Enter a number: ")
val2 = input("Enter another number: ")
print("Sum of number is: ", val1 + val2) #its called concataration, eta sting so pasha pashi number boshe jabe, sum hobe na
print("Sum of number is: ", int(val1) + int(val2)) #string ke integer e convert kore sum kora holo

#length of string
str1 = "Hello"
print("Length of str1 is: ",len(str1)) #string er length ber kora holo

#string identification
str= "hello world"
print(str[4]) #string er 4th index er character ber kora holo

#string slicing
str1 = "Hello World"
print(str1[0:5]) #string er 0 to 4th index er character ber kora holo
print(str1[6:]) #string er 6th index theke last index porjonto character ber kora holo

#negetive indexing
str1 = "Hello World"
print(str1[-1]) #string er last index er character ber kora holo
print(str1[-5:-1]) #string er -5 to -2 index er character ber kora holo

str= "iam a coder"
print(str.endswith("er")) #string er last character du ta check kora holo