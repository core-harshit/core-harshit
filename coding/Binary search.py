def binarysearching(start,end,value,l):
    while start<end:
        mid=(start+end)//2
        if list[mid]==value:
            print("found at index: ",mid )
            break
        elif end-start==1:
            print("not found index")
            break
        else:
            if list[mid]<value:
                start=mid
            else:
                end=mid

list=[2,4,5,6,7,8,12,13,34,45,56,78,89,112,223,334,445,556]
start=0
end=len(list)
value=int(input("enter the value whose position u wanna find in list:: "))

binarysearching(start,end,value,list)
