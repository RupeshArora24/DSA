nums=[4,4,4,4,3,3,3,1,2,0,1]
count =0
maxx =0
vist = {}

for i in nums :
    vist[i]=True
print(vist)

for i in nums:
    if i-1 not in vist and vist[i]==True :
        print(i,"= i")
        vist[i] = False
        curr = i
        curr=curr+1
        print(vist,curr,count)
        count+=1
        while ((curr in vist) and (vist[curr]==True)) :
            print("in while loop","Curr = ",curr,"maxx = ",maxx,"count = ",count)
            if count>=maxx:
             count = count+1
            vist[curr]=False
            curr=curr+1
        maxx=count

print(maxx)            
