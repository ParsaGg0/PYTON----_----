import random
import os


a, b, c = ['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']

 

def insert(a, b, c, turn, position, isEMPTY):

   if 1 <= position <= 3:

       if  a[position - 1] == "-" :

           a[position - 1] = turn
           isEMPTY = True
       else :
           isEMPTY =False

       

   elif 4 <= position <= 6:
    if  b[position - 4] == "-" :

       b[position - 4] = turn
       isEMPTY = True
    else :
           isEMPTY =False

   elif 7 <= position <= 9:
    if  c[position - 7] == "-" :

       c[position - 7] = turn
       isEMPTY = True
    else :
        isEMPTY =False

   return a, b, c , isEMPTY




 

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

   # diagonal

   elif a[0] == turn and b[1] == turn and c[2] == turn:

       return True

   elif a[2] == turn and b[1] == turn and c[0] == turn:

       return True

   return False

 

def is_finished(a, b, c, result):

   if result:

       return True

   elif a[0] != '-' and a[1] != '-' and a[2] != '-':

       if b[0] != '-' and b[1] != '-' and b[2] != '-':

           if c[0] != '-' and c[1] != '-' and c[2] != '-':

               return True

   return False

 

def make_line(a):

   line_a = a[0] + ' ' + a[1] + ' ' + a[2]

   return line_a

 

def print_board(a, b, c):

   line_a = make_line(a)

   line_b = make_line(b)

   line_c = make_line(c)

   board = line_a + '\n' + line_b + '\n' + line_c

   os.system('CLS')

   print(board)

  

 

ended = False

karbar = input("enter your mode :  1 - cumputer     2 - 1 vs 1")

if karbar=="2":

   ended = False

   while not is_finished(a, b, c, ended):

      print_board(a, b, c)

      isEMPTY=False
      while isEMPTY == False:

        command = input("enter your sign and number: ")

        params = command.split()

        turn = params[0]

        position = int(params[1])

     

        result = insert(a, b, c, turn, position,isEMPTY)
        isEMPTY = result [3]


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
      
else :
   
   nobat = "user"

   ended = False
   isEMPTY=False


   while not is_finished(a, b, c, ended):


      if nobat=="user":
        isEMPTY=False
        while isEMPTY == False:
         print_board(a, b, c)

         command = input("enter your sign and number: ")

         params = command.split()

         turn = "x"

         position = int(params[1])
         result = insert(a, b, c, turn, position,isEMPTY)
         isEMPTY = result [3]

        a = result[0]

        b = result[1]

        c = result[2]

        nobat = "comp"

      elif nobat == "comp" :
        isEMPTY=False
        while isEMPTY == False:
          comp = random.randint(1,9)

          turn = "o"

          position = comp

          nobat = "user"
         
          result = insert(a, b, c, turn, position,isEMPTY)
          isEMPTY = result[3]

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
