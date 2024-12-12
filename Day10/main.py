mapa = []
height = 0
width = 0
def findPath(current, coords):
    target = current + 1
    while True:
        if target == 9:
            print(f"Path found, coords: {coords}")
            return
        if coords[1] + 1 < width and mapa[coords[0]][coords[1] + 1] == target:
            target += 1
            coords[1] += 1
            continue
        if coords[0] + 1 < height and mapa[coords[0] + 1][coords[1]] == target:
            target += 1
            coords[0] += 1
            continue
        if coords[1] - 1 >= 0 and mapa[coords[0]][coords[1] - 1] == target:
            target += 1
            coords[1] -= 1
            continue
        if coords[0] - 1 >= 0 and mapa[coords[0] - 1][coords[1]] == target:
            target += 1
            coords[0] -= 1
            continue
        print(f"Path not found, coords: {coords}")
        return
with open("data_example", "r") as file:
    for line in file:
        row = []
        line = line.strip()
        for char in line:
            row.append(int(char))
        mapa.append(row)
height = len(mapa)
width = len(mapa[0])sh
for row in mapa:
    print(row)
for index, row in enumerate(mapa):
    for index2, element in enumerate(row):
        if element == 0:
            findPath(element, [index, index2])