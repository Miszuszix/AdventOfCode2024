def check(tab):
    positive = [1,2,3]
    negative = [-1, -2, -3]
    differences = []
    pos = True
    neg = True
    for i in range(len(tab) - 1):
        difference = tab[i + 1] - tab[i]
        differences.append(difference)
    for i in differences:
        if i not in positive:
            pos = False
    for i in differences:
        if i not in negative:
            neg = False
    if pos or neg:
        return True
    return False

safe = 0
with open("data") as file:
    for line in file:
        row = [int(i) for i in line.split()]
        if check(row):
            safe += 1
            continue
        for i in range(len(row)):
            temp = row[:i] + row[i + 1:]
            if check(temp):
                safe += 1
                break
    print(safe)