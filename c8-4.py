list1 = [6,5,1,0]

M = 0
m = 0

c = 1000
for j in list1:
    
    M = M + j*c
    c = c//10
    #print('stop')
    
print(M)


c = 1
for j in list1:
    
    m = m + j*c
    c = c*10
    
print(m)