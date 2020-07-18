for i in range(int(input())):
    n=int(input())
    ll=[]
    l=list(map(int,input().split()))
    f=False
    while f==0:
        for j in range(n-1):
            if l[i]>l[i+1]:
                ll.append(l[i]-l[i+1])
                l[i],l[i+1]=l[i+1],l[i]
        if l==sorted(l):
            f=True
    print(max(ll))
