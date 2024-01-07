nums=[1,2,2,1]
k=1
store={}
count=0
for i in range(len(nums)):
    print(nums[i],i)
    for j in range(len(nums)):
        print("Nums[j], ",nums[j],j,"difference = ",abs(nums[i]-nums[j]),"j = ",j,"i = ",i)
        if j>i and abs(nums[i]-nums[j])==k :
            count=count+1
print(count)
