arr=[0, -1, 2, -3, 1]
su = 2
su1=0
dic = {}

# Step1 --> first enetering all the numbers in the dictionary
# Step 2 --> su=2 --> a+b=2--> a=2-b
for i in arr:
    if su-i in dic :
        print("True", su-i,i)
    else :
        dic[i] = 1

print("No sum is not possible")             