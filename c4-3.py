T = 5
S = 1

gT = 400
gS = 350

if T==3:
    
    print("1 Gheymate nahayi : " ,  (T*gT + S*gS)*0.90 )
    
elif T==4 :
       
    print("2 Gheymate nahayi : " ,  (T*gT + S*gS)*0.88 )
    
    
elif T+S >= 5 :
    
    print("3 Gheymate nahayi : " ,  (T*gT + S*gS)*0.85 )
    
else:
    
    print("4 Gheymate nahayi : " ,  (T*gT + S*gS) )


