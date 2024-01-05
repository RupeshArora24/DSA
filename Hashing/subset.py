arr1 = [2,4,7,1,5,2,2]
arr2 = [5,2,2]
a=len(arr2)
b=0

for i in arr1:
    if i in arr2:
        b=b+1

if b == a :
    print("Yes it is the subset")
else:
    print("No")    