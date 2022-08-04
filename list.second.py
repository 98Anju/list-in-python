a=[50,23,70,56,12,51,7]
i=0
sec=0
while i<len(a):
    if a[i]>sec:
        if a[i]!=max:
            sec=a[i]
            i=i+1
print(sec)









