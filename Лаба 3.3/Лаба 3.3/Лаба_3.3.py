import math

def Authorization(exit):

    comand = str(input())
    comand = comand.split()
    x = len(comand)
    if comand[0] != "LOGIN":
        print("Код ошибки: 1")
        Authorization(exit)

    while len(comand) != 3:
        print("Код ошибки: 1")
        comand = str(input())
        comand = comand.split()

    f=open('pass.txt', 'r')
    for line in f:
        lst = line.split()
        if ((lst[0] == comand[1]) & (lst[1] == comand[2]) & (comand[0] == "LOGIN")):
            return True
            exit = True
            print("Код ошибки: 0")
    if exit == False:
        print("Код ошибки: 1")
        Authorization(exit)

error = 0
exit = False
exit = Authorization(exit)
exit = True
A = "NULL"
B = "NULL"
C = "NULL"
while exit:
    x = input()
    x = x.split()
    if x[0] == "STORE":
        if len(x) != 4:
            print("Код ошибки: 2")
            error = 2
        else:
            try:
                float(x[1])
                float(x[2])
                float(x[3])
                error = 0
            except ValueError:
                error = 3
        if error == 0:
            A = int(x[1])
            B = int(x[2])
            C = int(x[3])
        elif error == 3: 
            print("Код ошибки: 3")
        error = 0
    elif (x[0] == "SOLVE") & (len(x) == 1):
        if (A != "NULL") & (B != "NULL") & (C != "NULL") :
            discr = B ** 2 - 4 * A * C
            print("Дискриминант D = %.2f" % discr)
            if ((A == 0) & (B == 0) & (C ==0) or (A == 0)& (B == 0) & (C != 0)):
                print("Код ошибки: 2")
            else:
                if discr > 0:
                    x1 = float((-B + math.sqrt(float(discr))) / (2 * A))
                    x2 = float((-B - math.sqrt(float(discr))) / (2 * A))
                    print("x1 = %.2f \nx2 = %.2f" % (x1, x2))
                elif discr == 0:
                    x = -B / (2 * A)
                    print("x = %.2f" % x)
                else:
                    print("Корней нет\n" + "Код ошибки 0")
            A = "NULL"
            B = "NULL"
            C = "NULL"
        else:
            print("Код ошибки: 2")
    elif (x[0] == "SOLVE") & (len(x) == 4):
        try:
            float(x[1])
            float(x[2])
            float(x[3])
        except ValueError:
            error = 3
        if error == 0:
            A = float(x[1])
            B = float(x[2])
            C = float(x[3])
            discr = B ** 2 - 4 * A * C
            print("Дискриминант D = %.2f" % discr)
            if ((A == 0) & (B == 0) & (C ==0) or (A == 0)& (B == 0) & (C != 0)):
                print("Код ошибки: 2")
            else:
                if discr > 0:
                    x1 = float((-B + math.sqrt(float(discr))) / (2 * A))
                    x2 = float((-B - math.sqrt(float(discr))) / (2 * A))
                    print("x1 = %.2f \nx2 = %.2f" % (x1, x2))
                elif discr == 0:
                    x = -B / (2 * A)
                    print("x = %.2f" % x)
                else:
                    print("Корней нет\n" + "Код ошибки 0")
            A = "NULL"
            B = "NULL"
            C = "NULL"
        elif error == 3:
            print("Код ошибки: 3")
            error = 0
    else:
        print("Код ошибки: 3")
