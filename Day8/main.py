characters = {}
mapa = []
with open("data") as file:
    for line in file:
        line = line.strip()
        mapa.append(list(line))
for row in mapa:
    for element in row:
        if element != '.':
            if element not in characters:
                coords = [mapa.index(row), row.index(element)]
                characters[element] = [coords]
                continue
            coords = [mapa.index(row), row.index(element)]
            characters[element].append(coords)
antinodes = []
for element in characters:
    for i in range(len(characters[element]) - 1):
        for j in range(i + 1, (len(characters[element]))):
            multiplier = 1
            antenna = characters[element][i]
            antenna2 = characters[element][j]
            distance = [antenna[0] - antenna2[0], antenna[1] - antenna2[1]]
            while True:
                    rank = antenna[0] + (distance[0] * multiplier)
                    column = antenna[1] + (distance[1] * multiplier)
                    if -1 < rank < len(mapa) and -1 < column < len(mapa[0]):
                        antinode = [rank, column]
                        if antinode not in antinodes:
                            antinodes.append(antinode)
                        multiplier += 1
                    else:
                        break
            multiplier = 1
            while True:
                    rank = antenna2[0] - (distance[0] * multiplier)
                    column = antenna2[1] - (distance[1] * multiplier)
                    if -1 < rank < len(mapa) and -1 < column < len(mapa[0]):
                        antinode = [rank, column]
                        if antinode not in antinodes:
                            antinodes.append(antinode)
                        multiplier += 1
                    else:
                        break
for element in characters:
    for i in range(len(characters[element])):
        if characters[element][i] not in antinodes:
            antinodes.append(characters[element][i])
#print(antinodes)
print(len(antinodes))