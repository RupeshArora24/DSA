arr1 = [2,4,7,1,5,2,2]
arr2 = [5,2,2,9]
arr3 ={}
for i in arr1 :
   if i in arr3:
       arr3[i]+=1
   else:
       arr3[i]=1

for i in arr2:
    if i in arr3:
        arr3[i]-=1
    else:
        print("No such subset")
print("Yes subset present")        