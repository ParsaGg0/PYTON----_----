m = 123456789

for k in range(1000):
    
    print(m)
    print(m%10 , 'yekan \n')
    m = m//10
    
    if m==0:
        
        break