arr = [10, 5,10, 3, 4, 3, 5, 6]
arr1={}
k=2
for i in range(len(arr)):
    if arr[i] in arr1:
        if i-arr1[arr[i]] == k:
            print("True",arr[i])
    else:
        arr1[arr[i]]=i   

print(arr1)
print("False")        