x = 1
print(x)
print("I am pratoy")
print('Comma use korle','Same line e print hobe')
y= 23+34
print(y)
name = "Pratoy" #assignment operation, dan pasher value bam pashe store hoi
print("My name is", name)
age = 23
age2 = age
print(age2)
name = 'Pratoy'
age = 200
price = 24.56
print(type(name))
print(type(age))
print(type(price))

old = False
print(type(old))

a = 10
b = 20
print(a==b)

num = 10
num %=5
print(num) #modulus operation, 10%5 = 0

#logical operators
print(not False)
print(not True)
a = 50
b= 30
print(not(a>b))

val1 = True
val2 = False
print(val1 and val2) #value duita true holei true hobe, ekta false hole false hobe
print(val1 or val2) #value duita false holei false hobe, ekta true hole true hobe

#type coversion
a= 2
b = 4.25
sum = a+b #python automatically convert kore float e, jodi kono ekta value float hoi, tahole baki value o float e convert hobe
print(sum)

#type casting
a,b = 2, "4"
b = int(b) #string ke integer e convert kora holo
sum = a+b  
print(sum)

a = 3.4
a = str(a) #float ke string e convert kora holo
print(type(a))