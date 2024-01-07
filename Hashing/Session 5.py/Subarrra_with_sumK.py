Arr=[10 , 2, -2, -20, 10]#[10 , 2, -2, -20, 10]
N=len(Arr)
k=-10
prefix = [0]*(N+1)
        
for i in range(1,N+1):
    prefix[i]=prefix[i-1]+Arr[i-1]

print(prefix)            
mapp ={}    
count=0  
for i in range(N+1):

    if prefix[i] in mapp:
     
     mapp[prefix[i]]+=1
    
     if prefix[i]-k in mapp:
            
            print("I am in the loop",prefix[i],i)
            count+=mapp[prefix[i]]
    else:

        mapp[prefix[i]]=1
        if prefix[i]-k in mapp:
            
            print("I am in the loop",prefix[i],i)
            count+=mapp[prefix[i]]

print(count,mapp)        