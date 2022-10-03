def counter(lis,j):
    count=0
    for i in range(j,len(lis)):
        if i==1:
            count+=1
    print( count)
def solution(i):
    stringy=''
    lis=[q for q in range(2,13002)]
    for k in range(1000):
        p=lis[k]
        if p!=0:
            stringy+=str(p)
            lis2=lis[:lis.index(p)+1]
        for j in range(lis.index(p)+1,len(lis)):
            if lis[j]%p!=0:
                lis2.append(lis[j])
        lis=lis2.copy()
    for q in lis:
        stringy+=str(q)
    print(len(stringy))
    return stringy[i:i+5]

def solution1(i):
    stringy='23'
    const=1
    while len(stringy)<i+5:
        stringy+=str(6*const-1)
        stringy+=str(6*const+1)
        const+=1
    print(stringy)
    return 

def test():
    k=[]
    for i in range(100):
        if i%2==0:
            k.append(0)
        elif i%3==0:
            k.append(0)
        else:
            k.append(i)
    print(k)
    for j in k:
        if j==0:
            k.remove(j)
    return k
    
        
        
    
