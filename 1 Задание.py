import os

with open("F1.txt", "w") as f:
    print("Если хотите прервать ввод просто нажмите enter")
    while True:
        str = input("Введите строку: ")
        str = str + '\n'
        f.write(str)
        if str == "\n":
            False
            break

try:
    with open("F1.txt") as f_obj, open("F2.txt", "w") as f2:
        for line in f_obj:
            if line.strip().endswith('А'):
                f2.write(line)
            for line in f_obj:
                print(line)
        # while True:
        #     print("Выберите\n1. Вывести данные 1-го файла\n2. Вывести данные 2-го файла\n3. Выход\nBаш выбор :")
        #     key = int(input())
        #     if key == 1:
        #         for line in f_obj:
        #             print(line)
        #     elif key == 2:
        #         for line in f2:
        #             print(line)
        #     else:
        #         print("Good bye")
        #         False
        #         break
except IOError:
    print("Произошла ошибка ввода-вывода!")
# os.remove("F1.txt")
# os.remove("F2.txt")
