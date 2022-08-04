
a=["sajan","aruna","sofiya","kartik","anuj","mamta"]
b=input("enter any name")
i=0
while i<len(a):
    c=a[i]
    if b==c[0:len(b)]:
        print(c)
    i=i+1