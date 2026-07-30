#while loop

count = 1
while count<=5:
    print(count)
    count+=1


num = 2
count = 1
while(count<=10):
    print(num,"*",count,"=",num*count)
    count+=1


num = [1,4, 9, 16, 25, 36, 49, 64, 81, 100]
count = 0
while count < len(num):
    print(num[count])
    count += 1

num = (1,4, 9, 16, 25, 36, 49, 64, 81, 100)
count = 0
x = 25
while count< len(num):
    if (num[count] ==x):
        print("Found")
        count += 1