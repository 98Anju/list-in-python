name=["n","i","t","i","n"]
s=[]
i=-1
while i>=-len(name):
    b=name[i]
    s.append(b)
    i=i+1
    if name==s:
        print("palindrom")
    else:
        print("not palindrom")
        