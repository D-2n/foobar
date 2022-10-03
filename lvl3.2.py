def solution(l):
    lis=[]
    n=len(l)
    counter=0
    for i in range(n):
        for j in range(i+1,n):
            if l[j]%l[i]==0 and j<n:
                for k in range(j+1,n):
                    if l[k]%l[j]==0:
                            counter+=1
    return counter
import random
                    
                
def test():
    for j in range(100):
        solution([random.randint(1,999999) for i in range(2000)])
        
        
def solution1(l):
    counter=0
    lis=[0]*len(l)
    for i in range(len(l)):
        for j in range(i):
            if l[i]%l[j]==0:
                lis[i]+=1
                counter+=lis[j]
    
    
                
                