lst = list(map(int,input().split())) 
lst.sort()
new_lst = []
if len(lst)%2==0:
    for i in range(len(lst)//2):
        new_lst.append(lst[-i-1])
        new_lst.append(lst[i])
else:
    for i in range(len(lst)//2+1):
        new_lst.append(lst[-i-1])
        if i==len(lst)//2:
            continue
        new_lst.append(lst[i])
        
print(new_lst)
