arr = [1, 2, 1, 4, 3, 1,7,7]
n = len(arr)
d={}
for i in arr:
    if i in d:
        d[i]+=1
    else:
        d[i]=1

maxii = max(d.values())
print(n-maxii)            