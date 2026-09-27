n = 3647
list1 = []
for k in range(4):

    list1.append(n%10)
    n = n//10
    

list2 = []

for i in range(4):
    
    k = max(list1)
    list2.append(k)
    list1.remove(k)
    


M = 0
m = 0

c = 1000
for j in list2:
    
    M = M + j*c
    c = c//10
    


c = 1
for j in list2:
    
    m = m + j*c
    c = c*10
    


print(M,m,M-m)

