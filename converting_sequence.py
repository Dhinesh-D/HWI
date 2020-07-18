n=int(input())
l=list(input())
ll=[]
c=0
for i in range(n*2):
    if(l[i]=='('):
        ll.append('(')
    elif(ll==[]):
        for j in range(i+1,n*2):
            c+=1
            if(l[j]=='('):
                (l[i],l[j])=(l[j],l[i])
                break
        ll.append('(')
    else:
        ll.pop()
print(c)
