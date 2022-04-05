a = [ [ None for i in range(3) ] for j in range(3) ]
for i in range(len(a)):
    for j in range(len(a)):
        a[i][j] = ' '
def fincOne():
    print(a[0][0])
    print("---------")
    print("| "+a[0][0]+" "+a[0][1]+" "+a[0][2]+" |")
    print("| "+a[1][0]+" "+a[1][1]+" "+a[1][2]+" |")
    print("| "+a[2][0]+" "+a[2][1]+" "+a[2][2]+" |")
    print("---------")


    victory = [[a[0][0],a[0][1],a[0][2]],
               [a[1][0],a[1][1],a[1][2]],
               [a[2][0],a[2][1],a[2][2]],
               [a[0][0],a[1][1],a[2][2]],
               [a[0][2],a[1][1],a[2][0]],
               [a[0][0],a[1][0],a[2][0]],
               [a[0][1],a[1][1],a[2][1]],
               [a[0][2],a[1][2],a[2][2]]]
    X_win = False
    O_win = False

    for i in victory:

            if ''.join(i) == 'XXX':
                X_win = True
            if ''.join(i) == 'OOO':
                O_win = True

    if (X_win and O_win) or (abs(a.count('O') - a.count('X')) >= 2):
        print('Impossible')
        return 1
    elif X_win:
        print('X wins')
        return 1
    elif O_win:
        print('O wins')
        return 1
    elif find() == -1 and a.count('O') == a.count('X'):
        print('Draw')
        return 1
    elif (a.count('O') == a.count('X')) and ((a.count('O') + a.count('X')) < 9):
        print('Game not finished')
        return 0
def find():
    for i in range(len(a)):
        for j in range(len(a)):
            if a[i][j] == " ":
                return 1
    return -1

def user_input(f):
    x, y = input('Enter the coordinates:').split(' ')
    try:
        x = int(x) - 1
        y = int(y) - 1
        if (x or y) not in range(0, 3):
            print('Coordinates should be from 1 to 3!')
            return
        elif a[x][y] != ' ':
            print('This cell is occupied! Choose another one!')
            return
        else:
            a[x][y] = f

    except:
        print('You should enter numbers!')
        return

f = 'X'

while(1):
    user_input(f)
    if (fincOne() == 1):
        break
    if f == 'X':
        f = 'O'
    else:
        f = 'X'
