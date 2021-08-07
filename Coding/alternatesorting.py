def alternatingSort(a):
    b=[]
    c=0
    if len(a)%2==0:
        for c in range(len(a)//2):
            b.append(a[c])
            b.append(a[-c-1])

        if len(b)!=len(set(b)):
            return False
        else:
            if b==sorted(b):
                return True
            else:
                return False
    else:
        for c in range(len(a)):
            b.append(a[c])
            b.append(a[-c-1])
            del b[len(a)::]
        if len(b)!=len(set(b)):
            return False
        else:
            if b==sorted(b):
                return True
            else:
                return False
a=[-92, -23, 0, 45, 89, 96, 99, 95, 89, 41, -17, -48]
p=alternatingSort(a)
print(p)
