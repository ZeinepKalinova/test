a = int(input())
b = int(input())    //2
if a<b:
    for i in range(a, b+1):
        print(i)

else:
    for i in range(a,b-1, -1):
        print(i)
        