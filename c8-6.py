N = 9998
print(N)

for counter in range(1000):
    
    n = N                        # kahsf ragham ha
    list1 = []
    for k in range(4):

        list1.append(n%10)
        n = n//10
        
 
    list2 = []                    #   list  bozorg be koochick
    for i in range(4):
        
        k = max(list1)
        list2.append(k)
        list1.remove(k)
        
        
    M = 0          
    m = 0

    c = 1000
    for j in list2:          #   max
        
        M = M + j*c
        c = c//10
        


    c = 1
    for j in list2:           # min
        
        m = m + j*c
        c = c*10
        


    #print(N,M,m,M-m)
    
    N = M-m                 #   update N
    
    print(N)

    if N==6174:
        
        break
