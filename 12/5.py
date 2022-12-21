string = input()
for i in range(int(string[1])):
    line = input()
    if "#" in line:
        pos = line.find("#")
        if pos > 0:
            print(line[:pos])
        else:
            print(line[pos:])
    elif "#" not in line:
        print(line)