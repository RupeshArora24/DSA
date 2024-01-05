arr = [1,3,3,4,1,4,4,4,4] 
n = len(arr)

querries = int(input())
while(querries):
    ans=0
    q = int(input())
    for i in range(n):
        if arr[i]==q:
            ans+=1
    print(ans)    
    querries=querries-1                

# here the time complexity of the code is O(n*querries)times as the for loop is running for n elements and for querries.
