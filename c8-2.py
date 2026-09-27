list1 = [1,0,5,6]
list2 = []

for i in range(4):
    
    k = max(list1)
    list2.append(k)
    list1.remove(k)
    
print(list1)    
print(list2)