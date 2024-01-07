arr = [15,-2,2,-8,1,7,10,23]
prefix=[0]*(len(arr)+1)

for i in range(1,len(arr)):
    prefix[i]=prefix[i-1]+arr[i-1]

# hasmap --> key = prefix sum , value = index   
prefix=prefix[1:]
mapi={}
res=0
maxx=0

for i in range(len(arr)):
    if prefix[i] in mapi :
        print("Ï am in  mappi")
        res = i-mapi[prefix[i]]
        print(i,mapi[prefix[i]],res)
    else:
        mapi[prefix[i]]=i
    maxx=max(res,maxx)
print(maxx)        