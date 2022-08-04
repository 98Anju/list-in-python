a=[1,0,1]
sum=0
i=-1
b=len(a)-1
while i>=len(a):
    sum=sum+a[i]*2**b
    i=-1
    b+=1
print(sum)



   
