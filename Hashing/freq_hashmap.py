arr1 = [1, 3, 3, 4, 1, 4, 4, 4, 4] 
arr2 = {}

for i in arr1:
    if i in arr2 :
        arr2[i]+=1
    else:
        arr2[i]=1 
print(arr2)           