room = []
direction = "up"
directions = ["up"]
path = []
counter = 0
previous = ""
def moveUp():
    global guard
    global direction
    global previous
    if room[guard[0] - 1][guard[1]] == '#':
        direction = "right"
        return
    guard[0] -= 1
    previous = "up"

def moveDown():
    global guard
    global direction
    global previous
    if room[guard[0] + 1][guard[1]] == '#':
        direction = "left"
        return
    guard[0] += 1
    previous = "down"

def moveLeft():
    global guard
    global direction
    global previous
    if room[guard[0]][guard[1] - 1] == '#':
        direction = "up"
        return
    guard[1] -= 1
    previous = "left"

def moveRight():
    global guard
    global direction
    global previous
    if room[guard[0]][guard[1] + 1] == '#':
        direction = "down"
        return
    guard[1] += 1
    previous = "right"

with open("data_example") as file:
    for line in file:
        line = line.strip()
        room.append(list(line))
for i, row in enumerate(room):
    if '^' in row:
        guard = [i, row.index('^')]
        path.append(guard.copy())
        break

while True:
    try:
        match direction:
            case "up":
                if [guard[0], guard[1] + 1] in path and previous != "left":
                    index = path.index([guard[0], guard[1] + 1])
                    if directions[index] == "right":
                        counter += 1
                moveUp()
            case "down":
                if [guard[0], guard[1] - 1] in path and previous != "right":
                    index = path.index([guard[0], guard[1] - 1])
                    if directions[index] == "left":
                        counter += 1
                moveDown()
            case "left":
                if [guard[0] - 1, guard[1]] in path and previous != "down":
                    index = path.index([guard[0] - 1, guard[1]])
                    if directions[index] == "up":
                        counter += 1
                moveLeft()
            case "right":
                if [guard[0] + 1, guard[1]] in path and previous != "up":
                    index = path.index([guard[0] + 1, guard[1]])
                    if directions[index] == "down":
                        counter += 1
                moveRight()
        path.append(guard.copy())
        directions.append(direction)
    except IndexError:
        break
print(counter)