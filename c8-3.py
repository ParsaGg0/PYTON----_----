list1 = [1,0,5,6,3,2,3,3,1,1,1,2,2,2,8]
list2 = []

for i in range(len(list1)):
    
    k = max(list1)
    list2.append(k)
    list1.remove(k)
    
print(list1)    
print(list2)