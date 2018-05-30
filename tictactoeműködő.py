import sys
#kezdetek kezdete
a1 = 7
a2 = 4
a3 = 1

b1 = 8
b2 = 5
b3 = 2

c1 = 9
c2 = 6
c3 = 3

turn = 0

f = 1


def nyeres ():
    if a1 == "x"and  a2 ==  "x"and a3 =="x":
        print ("x player won")
        sys.exit()
    elif b1 == "x"and  b2 == "x"and b3 =="x":
        print ("x player won")
        sys.exit()
    elif c1 == "x"and c2 == "x"and c3 == "x":
        print ("x player won")
        sys.exit()
    elif a1 == "x"and b1 == "x"and c1 == "x":
        print ("x player won")
        sys.exit()
    elif a2 == "x"and b2 == "x"and c2 == "x":
        print ("x player won")
        sys.exit()
    elif a3 == "x"and b3 == "x"and c3 == "x":
        print ("x player won")
        sys.exit()
    elif a1 == "x"and b2 == "x"and c3 == "x":
        print ("x player won")
        sys.exit()
    elif a3 == "x"and b2 == "x"and c1 == "x":
        print ("x player won")
        sys.exit()
    elif a1 == "0"and  a2 == "0"and a3 =="0":
        print ("0 player won")
        sys.exit()
    elif b1 == "0"and  b2 == "0"and b3 =="0":
        print ("0 player won")
        sys.exit()
    elif c1 == "0"and c2 == "0"and c3 == "0":
        print ("0 player won")
        sys.exit()
    elif a1 == "0"and b1 == "0"and c1 == "0":
        print ("0 player won")
        sys.exit()
    elif a2 == "0"and b2 == "0"and c2 == "0":
        print ("0 player won")
        sys.exit()
    elif a3 == "0"and b3 == "0"and c3 == "0":
        print ("0 player won")
        sys.exit()
    elif a1 == "0"and b2 == "0"and c3 == "0":
        print ("0 player won")
        sys.exit()
    elif a3 == "0"and b2 == "0"and c1 == "0":
        print ("0 player won")
        sys.exit()
    else:
        pass

def drawboard():
    print(a1,"|",b1,"|",c1,"|")
    print("-----------")
    print(a2,"|",b2,"|",c2, "|")
    print("-----------")
    print(a3,"|",b3,"|",c3, "|")


lista  = [7,8,9,4,5,6,1,2,3]
print("")
print("Welcome to tic tac toe!")
print("")
drawboard()
print("")
print("")

   
inp = input("where do u want to put your 0?: ")

for i in range(9):
    if inp == "7":
        if turn == 1:
            a1 = "x"
            drawboard()
            nyeres()
            inp = input("where do u want to put your 0?: ")
            turn = turn - 1
            
        elif turn == 0:
            a1 = "0"
            drawboard()
            nyeres()
            inp = input("where do u want to put your x?: ")
            turn = turn + 1
            
        continue
    elif inp == "4":
        if turn == 1:
            a2 = "x"
            drawboard()
            nyeres()
            inp = input("where do u want to put your 0?: ")
            turn = turn - 1
            
        elif turn == 0:
            a2 = "0"
            drawboard()
            nyeres()
            inp = input("where do u want to put your x?: ")
            turn = turn + 1
            
    elif inp == "1":
        if turn == 1:
            a3 = "x"
            drawboard()
            nyeres()
            inp = input("where do u want to put your 0?: ")
            turn = turn - 1
            
        elif turn == 0:
            a3 = "0"
            drawboard()
            nyeres()
            inp = input("where do u want to put your x?: ")
            turn = turn + 1
            
    elif inp == "8":
        if turn == 1:
            b1 = "x"
            drawboard()
            nyeres()
            inp = input("where do u want to put your 0?: ")
            turn = turn - 1
            
        elif turn == 0:
            b1 = "0"
            drawboard()
            nyeres()
            inp = input("where do u want to put your x?: ")
            turn = turn + 1
            
    elif inp == "5":
        if turn == 1:
            b2 = "x"
            drawboard()
            nyeres()
            inp = input("where do u want to put your 0?: ")
            turn = turn - 1
            
        elif turn == 0:
            b2 = "0"
            drawboard()
            nyeres()
            inp = input("where do u want to put your x?: ")
            turn = turn + 1
            
    elif inp == "2":
        if turn == 1:
            b3 = "x"
            drawboard()
            nyeres()
            inp = input("where do u want to put your 0?: ")
            turn = turn - 1
            
        elif turn == 0:
            b3 = "0"
            drawboard()
            nyeres()
            inp = input("where do u want to put your x?: ")
            turn = turn + 1
            
    elif inp == "9":
        if turn == 1:
            c1 = "x"
            drawboard()
            nyeres()
            inp = input("where do u want to put your 0?: ")
            turn = turn - 1
            
        elif turn == 0:
            c1 = "0"
            drawboard()
            nyeres()
            inp = input("where do u want to put your x?: ")
            turn = turn + 1
            
    elif inp == "6":
        if turn == 1:
            c2 = "x"
            drawboard()
            nyeres()
            inp = input("where do u want to put your 0?: ")
            turn = turn - 1
            
        elif turn == 0:
            c2 = "0"
            drawboard()
            nyeres()
            inp = input("where do u want to put your x?: ")
            turn = turn + 1
            
    elif inp == "3":
        if turn == 1:
            c3 = "x"
            drawboard()
            nyeres()
            inp = input("where do u want to put your 0?: ")
            turn = turn - 1
            
        elif turn == 0:
            c3 = "0"
            drawboard()
            nyeres()
            inp = input("where do u want to put your x?: ")
            turn = turn + 1

print("")
print("U both lose")
print("")          

