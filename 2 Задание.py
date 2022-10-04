with open("Z2.txt", "r") as f:
    max = 0.0
    for line in f:
        fl_check = float(line.split()[1])
        if max < fl_check:
            max = fl_check
        if fl_check > 4.0 and fl_check < 6.0:
            print("Ученик со средним балом от 4 до 6: ", line)
        elif fl_check > 6.0 and fl_check < 8.0:
            print("Ученик со средним балом от 6 до 8: ", line)
        elif fl_check > 8.0:
            print("Ученик со средним балом 8 и выше: ", line)
with open("Z2.txt", "r") as f:
    for lin in f:
        if max == float(lin.split()[1]):
            print("\nУченик с максимальным балом: ", lin.split()[0])
