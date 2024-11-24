# جلسه ۲۰: بازی  tic tac toe (🔑)
# 
import os
import random
from re import X 

 
a, b, c = ['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']

 

def insert(a, b, c, turn, position): #

   if 1 <= position <= 3:

       a[position - 1] = turn#JAVAB=

   elif 4 <= position <= 6:

       b[position - 4] = turn#JAVAB=

   elif 7 <= position <= 9:

       c[position - 7] = turn# JAVAB= 

   return a, b, c

 

def check_win(a, b, c, turn):

   # rows

   if a[0] == turn and a[1] == turn and a[2] == turn:

       return True

   elif b[0] == turn and b[1] == turn and b[2] == turn:

       return True

   elif c[0] == turn and c[1] == turn and c[2] == turn:

       return True

   # columns

   elif a[0] == turn and b[0] == turn and c[0] == turn:

       return True

   elif a[1] == turn and b[1] == turn and c[1] == turn:

       return True

   elif a[2] == turn and b[2] == turn and c[2] == turn:

       return True

   # diagonal_GHOTR

   elif a[0] == turn and b[1] == turn and c[2] == turn:

       return True

   elif a[2] == turn and b[1] == turn and c[0] == turn:

       return True

   return False

 

def is_finished(a, b, c, result):# MOSHAKHAS MIKONAD KE BAZI TAMAM SHODE ? YA KHEIR!

   if result:

       return True

   elif a[0] != '-' and a[1] != '-' and a[2] != '-':#

       if b[0] != '-' and b[1] != '-' and b[2] != '-':#

           if c[0] != '-' and c[1] != '-' and c[2] != '-':#

               return True

   return False

 

def make_line(a):# Ozvhaye a ra beshmar va  namashesh toye 1 string ba space ( _ )

   line_a = a[0] + ' ' + a[1] + ' ' + a[2]

   return line_a

 

def print_board(a, b, c):

   line_a = make_line(a)

   line_b = make_line(b)

   line_c = make_line(c)

   board = line_a + '\n' + line_b + '\n' + line_c

   os.system('CLS')

   print(board)

  

 

ended = False# ASLI
x=(input("1V1?(🤖))OR PLAY WITH COMOUTER ??(🧑‍💻))"))# nahveye VORODI 
if x=='1v1':

    while not is_finished(a, b, c, ended):# ta vaghti ke tamom nashode 'natighe '..!

        print_board(a, b, c)

        

        command = input("enter your sign and number: ")

        params = command.split()

        turn = params[0]

        position = int(params[1])

        

        result = insert(a, b, c, turn, position)

        a = result[0]

        b = result[1]

        c = result[2]

        

        for t in ['X', 'O']:

            if check_win(a, b, c, turn):

                print_board(a, b, c)

                print(turn + ' is the winner!')

                ended = True

    

    if not ended:

        print_board(a, b, c)

        print('draw')
elif x=="0":
    print('play with computer')
    ended = False #
    nobat="user"# alan nobat user ast ! 
    while not is_finished(a, b, c, ended):# ta vaghti ke tamom nashode 'natighe '..!
        if nobat=='user':
            
        
            print_board(a, b, c) 

            

            command = input("enter your sign and number: ") # USER PART 

            params = command.split()

            turn = "x" # user

            position = int(params[1])

            

            result = insert(a, b, c, turn, position)

            a = result[0]

            b = result[1]

            c = result[2]
            nobat="computer"
        else:
            # start computer
            print_board(a, b, c) 

            

            turn= "o"# computer

        

           
        
            position = random.randint(1,9)

            

            result = insert(a, b, c, turn, position)

            a = result[0]

            b = result[1]

            c = result[2]
            nobat="user" # USER
            

        for t in ['X', 'O']:

            if check_win(a, b, c, turn):

                print_board(a, b, c)

                print(turn + ' is the winner!')

                ended = True

    

    if not ended:

        print_board(a, b, c)

        print('draw')