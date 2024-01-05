n = int(input())
arr=[]
arr1=[0]*n
for i in range(n):
    a = int(input())
    arr.append(a)
    print("element - ",arr)
    arr1[a]+=1
    print("New array - ",arr1)

q = int(input())
while(q):
 quer = int(input())
 print("Frequeny - ",arr1[q])
 q=q-1   


 # this is only applicable for elements less than n-1 that is if n is 10 then we can find the frequency of only 0,1,2,3,4,5,6,7,8,9