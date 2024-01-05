N = int(input())
arr = list(map(int,input().strip().split()))
Q = int(input())
prefix=[0]*(N+1)
for i in range(1,N+1):
       prefix[i]=prefix[i-1]+arr[i-1]
def func(q1,q2):
 
   
   return(prefix[q2+1]-prefix[q1])   

while(Q):
 
    Quer=list(map(int,input().strip().split()))
   
    q1=Quer[0]
    q2=Quer[1]
    a=func(q1,q2)
    print(a)
    Q=Q-1