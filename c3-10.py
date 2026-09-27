a = 10
b = 5
c = 'c'

shart_a = (type(a)==type(8) or type(a)==type(8.0))
shart_b = (type(b)==type(8) or type(b)==type(8.0))
shart_c = (type(c)==type(8) or type(c)==type(8.0))

if shart_a and shart_b and shart_c :
    
    if a<(b+c)  and  b<(a+c)  and  c<(a+b):
    
        print(" mosalas tashkil mishavad " )
    
    else :
    
        print(" moslas tashkil nemishavad ")
        
else:
    
    print(" yeki az maghadir addad int ya float nist! ")
    
    
