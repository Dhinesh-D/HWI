n=int(input())
x=[]
l=list(map(int,input().split()))
for i in range(1,n):
    if l[i-1]>l[i]:
        x.append(abs(l[i-1]-l[i]))
        l[i-1],l[i]=l[i],l[i-1]
print(max(x))
