from collections import Counter
nums=[1,2,2,1]

k=1
count=0
"""for i in range(len(nums)):
    print(i,nums[i])
    if nums[i]-k in nums and i>(nums.index(nums[i]-k)) :
        print("If ==> ",i,(nums.index(nums[i]-k)))
        count=count+1 
    if nums[i]+k in nums and i>(nums.index(nums[i]+k)):
        print("else ==> ",i,(nums.index(nums[i]+k)))
        count=count+1


print(count)        """

store={}

for i in nums:
    if i in store:
       store[i]+=1
       print("in first if loop ",i)
       print(store)
       if i-k in store:
        print("In second if loop ",i-k,i+k)
        count=count+store[i] 
        print("Count = ",count)
       if i+k in store:
          print("In second if loop ",i-k,i+k,i,k,store[2])
          count=count+store[i] 
          print("Count = ",count)


    else:
        store[i]=1    

print(count)        