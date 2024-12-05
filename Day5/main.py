before = []
after = []
result = 0
with open("data") as file:
    for line in file:
        if line == "\n":
            break
        line = line.strip()
        before.append(int(line[:line.find("|")]))
        after.append(int(line[line.find("|") + 1:]))
    for line in file:
        okay = True
        line = line.strip()
        tab = list(map(int, line.split(",")))
        for i in range(len(tab) - 1):
            if not okay:
                break
            current = tab[i]
            temp = tab[i + 1:]
            target = []
            for j in range(len(before)):
                if before[j] == current and after[j] in temp:
                    target.append(after[j])
            if len(target) != len(temp):
                okay = False
        if okay:
            result += tab[int((len(tab) - 1) / 2)]
print(f'Result: {result}')