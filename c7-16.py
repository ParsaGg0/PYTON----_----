n = 100000

list1 = [n]

for k in range(100000000):
    
    if n%2==0:
        n = n//2
        
    else:
        n = 3*n+1
        
    list1.append(n)
    
    if n==1:
        
        break
    
print(list1)
print('------------------------------')
print("tedade marahel:" , len(list1)-1)
    
    
    