def winner(symbol):
    global table
    for i in range(3):
        if table[i][0] == table[i][1] == table[i][2] == symbol:
            return True
    for j in range(3):
        if table[0][j] == table[1][j] == table[2][j] == symbol:
            return True
    if table[0][0] == table[1][1] == table[2][2] == symbol \
        or table[0][2] == table[1][1] == table[2][0] == symbol:
            return True
    return False


table = [[" " for i in range(3)]for j in range(3)]
current_symbol = "X"

while True:
    print("-" * 9)
    for i in range(len(table)):
        for j in range(len(table[i])):
            if j == 0:
                print("| " + table[i][j], end=" ")
            else:
                print(table[i][j], end=" ")
        print("|")
    print("-" * 9)
    
    if winner("X") or winner("O"):
        if "X":
            print("X wins")
        else:
            print("O wins")
        break
    elif not any(x for row in table for x in row if x == " "):
        print("Draw")
        break
    else:
        while True:
            user_move = input().split()
            try:
                user_move = [eval(i) for i in user_move]
            except ValueError:
                print("You should enter numbers")
                continue
            if len(user_move) < 2:
                print("You should enter two numbers!")
                continue
            elif (1 > (user_move[0] or user_move[1])) or ((user_move[0] or user_move[1]) > 3):
                print("Coordinates should be from 1 to 3!")
                continue
            elif table[user_move[0] - 1][user_move[1] - 1] != " ":
                print("This cell is occupied! Choose another one!")
                continue
            else:
                table[user_move[0] - 1][user_move[1] - 1] = current_symbol
                current_symbol = "O" if current_symbol == "X" else "X"
                break
                