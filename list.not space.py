a=["a name is arpita"]
i=0
s=" "
count=0
while i<=len(a):
    j=0
    while j<=len(a[i]):
        if a[i]!=" ":
            s=s+a[i]
        count=count+1
        i=i+1
print(s)


