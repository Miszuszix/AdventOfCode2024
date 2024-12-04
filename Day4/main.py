tab = []
global xmas
xmas = 0
def transponate(tab1):
    result = []
    for i in range(len(tab1)):
        temp = ""
        for j in range(len(tab1[i])):
            temp += tab1[j][i]
        result.append(temp)
    return result

def countHorizontal(tab1):
    global xmas
    for row in tab1:
        xmas += row.count("XMAS")
        xmas += row.count("SAMX")

def countDiagonal(tab1):
    global xmas
    for i in range(len(tab1) - 3):
        for j in range(len(tab1[i]) - 3):
            if tab1[i][j] == "X" and tab1[i + 1][j + 1] == "M" and tab1[i + 2][j + 2] == "A" and tab1[i + 3][j + 3] == "S":
                xmas += 1
            if tab1[i][j] == "S" and tab1[i + 1][j + 1] == "A" and tab1[i + 2][j + 2] == "M" and tab1[i + 3][j + 3] == "X":
                xmas += 1

def reverse(tab1):
    for i in range(len(tab1)):
        tab1[i] = tab1[i][::-1]
    return tab1

def countMAS(tab1):
    global xmas
    for i in range(len(tab1) - 2):
        for j in range(len(tab1[i]) - 2):
            if tab1[i][j] == "M" and tab1[i + 1][j + 1] == "A" and tab1[i + 2][j + 2] == "S" or tab1[i][j] == "S" and tab1[i + 1][j + 1] == "A" and tab1[i + 2][j + 2] == "M":
                if tab[i + 2][j] == "M" and tab[i + 1][j + 1] == "A" and tab[i][j + 2] == "S" or tab[i + 2][j] == "S" and tab[i + 1][j + 1] == "A" and tab[i][j + 2] == "M":
                    xmas += 1

with open("data") as file:
    for line in file:
        line = line.strip()
        tab.append(line)
countMAS(tab)
print(xmas)