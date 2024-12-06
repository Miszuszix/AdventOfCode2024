before = []
after = []
suma = 0
canContinue = True
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
        while True:
            for i in range(len(tab) - 1):
                current = tab[i]
                temp = tab[i + 1:]
                target = []
                for j in range(len(before)):
                    if before[j] == current and after[j] in temp:
                        target.append(after[j])
                if len(target) == len(temp):
                    continue
                for j in temp:
                    if j not in target:
                        okay = False
                        inTab = tab.index(j)
                        notInTab = tab.index(current)
                        tab[notInTab], tab[inTab] = j, current
                break
            else:
                break
        if not okay:
            result = tab[int((len(tab) - 1) / 2)]
            suma += result
print(f'Suma: {suma}')