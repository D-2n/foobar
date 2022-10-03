def solution(l):
    finalis=[]
    l2=[]
    for _ in l:
        if len(_.split('.'))==2:
            l2.append(_+'.-1')
        elif len(_.split('.'))==1:
            l2.append(_+'.-1.-1')
        else:
            l2.append(_)
    lis1=test(sortit(l2,0),0)
    l3=[]
    for i in lis1:
        l3.append(test(sortit(i,1),1))
    l4=[]
    for k in l3:
        for k1 in k:
            l4.append(test(sortit(k1,2),2))
    for l1 in l4:
        for l2 in l1:
            finalis+=l2
    finalis1=[]
    for elem in finalis:
        splitty=elem.split('.')
        if splitty[2]=='-1' and splitty[1]=='-1':
            finalis1.append(splitty[0])
        elif splitty[2]=='-1':
            finalis1.append(splitty[0]+'.'+splitty[1])
        else:
            finalis1.append(elem)
    return finalis1
    
        
        
def sortit(l,ind):
    for i in range (len(l)):
        j=i
        while j>0 and int(l[j-1].split('.')[ind])>int(l[j].split('.')[ind]):
            l[j-1],l[j]=l[j],l[j-1]
            j-=1
    return l
    
def test(l,ind):
    prev=0
    lis=[]
    m=l[0].split('.')[ind]
    for i in l:
        ti=i.split('.')[ind]
        if ti!=m:
            k=l.index(i)
            m=ti
            lis.append(l[prev:k])
            prev=k
    lis.append(l[prev:])
    return lis