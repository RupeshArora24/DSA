nums=[9,1,4,7,3,-1,0,5,8,-1,6]
arr = sorted(nums)
arr= set(arr)
arr= list(arr)
arr=sorted(arr)
N=len(arr)
print(arr)
out=0
maxi=0
for i in range(1,N):
    if arr[i]-1==arr[i-1]:
      print("Maxi = ",maxi,"Out = ",out)  
      print("In the if == ","Maxi = ",maxi,"Out = ",out)
      print(arr[i-1],arr[i],out)      
      out+=1
      if maxi<=out :
        maxi=out
    else:
        print("Hey")
        out=0
        print("out = ",out)

    if N==0:
     print(0)
    else:
     print(maxi+1)