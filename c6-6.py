for n in range (1,1001):
    
    tedad = 0
    for m in range(1,n+1):
        
        if n%m == 0:
            
            tedad = tedad + 1
            
    
    if tedad == 3 :
        
        print(n)