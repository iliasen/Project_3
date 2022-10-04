with open("Z3.txt", "r") as f:
    try:
        wor={}
        for line in f:
            line = line.strip("\n")
            print(line)
            num = 0
            for i in line.split():
                for a in range(len(i)):
                    if i[a] == "(":
                        k = i.rfind('(')
                        st_num = ""
                        for m in range(k):
                            st_num += i[m]
                        num += int(st_num)
            wor.update({line.split()[0] : num})
        print(wor)
    except IOError:
        print("Произошла ошибка ввода-вывода!")