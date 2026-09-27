import random
a=[0,1]
scr_cmp=0
scr_user=0
while True:
    x=random.choice(a)
    y = int (input("enter your number"))
    if y==-1:
        break
    print('computer guess:',x)
    if x==y:
        scr_cmp = scr_cmp+1
    else:
        scr_user = scr_user+1
    print('user:',scr_user)
    print ('cmp:',scr_cmp)