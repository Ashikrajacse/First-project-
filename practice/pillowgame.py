n=int(input('Enter number of player:'))
m=int(input('Enter number of second:'))
a=[]
for i in range(1,n+1):
     b=a.append(i)
     if i==n:
         for i in range(1,n):
               b=a.append(n-i)
print(a[m%len(a)])