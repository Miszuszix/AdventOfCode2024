characters = {}
mapa = []
antinodes = []
with open("data_example") as file:
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
for element in characters:
    for i in range(len(characters[element]) - 1):
        antenna = characters[element][i]
        antenna2 = characters[element][i + 1]
        distance = [antenna[0] - antenna2[0], antenna[1] - antenna2[1]]
        try:
            antinode = [antenna[0] + distance[0], antenna[1] + distance[1]]
            if antinode not in antinodes:
                antinodes.append(antinode)
        except:
            pass
        try:
            antinode = [antenna2[0] - distance[0], antenna2[1] - distance[1]]
            if antinode not in antinodes:
                antinodes.append(antinode)
        except:
            pass
print(antinodes)