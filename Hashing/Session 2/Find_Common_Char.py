arr=["cool","lock","cook"]
ans=[]
alpha={}
for i in range(ord('a'),ord('z')+1) :
    alpha[chr(i)]=float('inf')

for i in arr:
  al = {}

  for j in i:
    if j in al:

        al[j]+=1
    else:
       
        al[j]=1

  for i in alpha :
     if i in al:
        alpha[i]=min(alpha[i],al[i])
     else:
        alpha[i]=0

for i in alpha:
    while alpha[i]>0:
        ans.append(i)
        alpha[i]=alpha[i]-1

print(ans)                    

