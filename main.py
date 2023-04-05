def check_win(field):
    if field[0] == field[1] == field[2]:
        return True
    elif field[3] == field[4] == field[5]:
        return True
    elif field[6] == field[7] == field[8]:
        return True
    elif field[0] == field[3] == field[6]:
        return True
    elif field[1] == field[4] == field[7]:
        return True
    elif field[2] == field[5] == field[8]:
        return True
    elif field[0] == field[4] == field[8]:
        return True
    elif field[2] == field[4] == field[6]:
        return True

def check_pat(field):
    if (field[0] == " O " or field[0] == " X ") \
            and (field[0] == " O " or field[0] == " X ")\
            and (field[1] == " O " or field[1] == " X ")\
            and (field[2] == " O " or field[2] == " X ")\
            and (field[3] == " O " or field[3] == " X ")\
            and (field[4] == " O " or field[4] == " X ")\
            and (field[5] == " O " or field[5] == " X ")\
            and (field[6] == " O " or field[6] == " X ")\
            and (field[7] == " O " or field[7] == " X ")\
            and (field[8] == " O " or field[8] == " X "):
        return True

def print_box(field):
    print()
    print(field[0] + "|" + field[1] + "|" + field[2])
    print("___" + "|" + "___" + "|" + "___")
    print(field[3] + "|" + field[4] + "|" + field[5])
    print("___" + "|" + " ___ " + "|" + "___")
    print(field[6] + "|" + field[7] + "|" + field[8])

def game():
    filed = [" 1 ", " 2 ", " 3 ", " 4 ", " 5 ", " 6 ", " 7 ", " 8 ", " 9 ", ]

    print_box(filed)
    print("Крестики ходят первыми")
    current_user = " X "
    while True:
        try:
            num = int(input("Выберете номер клетки: "))
            if num < 1 or num > 9:
                print("Введите числовое значение от 1 до 9")
                continue
        except:
            print("Введите числовое значение от 1 до 9")
            continue

        if filed[num -1] == " X " or filed[num-1] == " O ":
            print("Выберете не занятое число!")
            continue

        filed[num - 1] = current_user

        print_box(filed)
        if check_pat(filed):
            print()
            print("Ничья!")
            return

        if check_win(filed):
            print()
            print("Выиграли " + current_user)
            return

        if current_user == " X ":
            current_user = " O "
        else:
            current_user = " X "

while True:
    print("Новая игра:")
    game()
    print()
    print()
    print()
    print()