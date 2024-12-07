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

with open("data") as file:
    for line in file:
        line = line.strip()
        room.append(list(line))
for i, row in enumerate(room):
    if '^' in row:
        guard = [i, row.index('^')]
        path.append(guard.copy())
        break

while True:
    print(guard)
    try:
        prediction = 1
        match direction:
            case "up":
                current = [guard[0], guard[1] + prediction]
                try:
                    while current != '#':
                        try:
                            index = path.index([guard[0], guard[1] + prediction])
                        except ValueError:
                            prediction += 1
                            current = [guard[0], guard[1] + prediction]
                            if current[1] == len(room[0]):
                                break
                            continue
                        if [guard[0], guard[1] + prediction] in path and previous != "left":
                            if directions[index] == "right":
                                counter += 1
                                break
                        prediction += 1
                        current = [guard[0], guard[1] + prediction]
                        if current[1] == len(room[0]):
                            break
                except IndexError:
                    pass
                moveUp()
            case "down":
                current = [guard[0], guard[1] - prediction]
                try:
                    while current != '#':
                        try:
                            index = path.index([guard[0], guard[1] - prediction])
                        except ValueError:
                            prediction += 1
                            current = [guard[0], guard[1] - prediction]
                            if current[1] == 0:
                                break
                            continue
                        if [guard[0], guard[1] - prediction] in path and previous != "right":
                            if directions[index] == "left":
                                counter += 1
                                break
                        prediction += 1
                        current = [guard[0], guard[1] - prediction]
                        if current[1] == 0:
                            break
                except IndexError:
                    pass
                moveDown()
            case "left":
                current = [guard[0] - prediction, guard[1]]
                try:
                    while current != '#':
                        try:
                            index = path.index([guard[0] - prediction, guard[1]])
                        except ValueError:
                            prediction += 1
                            current = [guard[0] - prediction, guard[1]]
                            if current[0] == 0:
                                break
                            continue
                        if [guard[0] - prediction, guard[1]] in path and previous != "down":
                            if directions[index] == "up":
                                counter += 1
                                break
                        prediction += 1
                        current = [guard[0] - prediction, guard[1]]
                        if current[0] == 0:
                            break
                except IndexError:
                    pass

                moveLeft()
            case "right":
                current = [guard[0] + prediction, guard[1]]
                try:
                    while current != '#':
                        try:
                            index = path.index([guard[0] + prediction, guard[1]])
                        except ValueError:
                            prediction += 1
                            current = [guard[0] + prediction, guard[1]]
                            if current[0] == len(room):
                                break
                            continue
                        if [guard[0] + prediction, guard[1]] in path and previous != "up":
                            if directions[index] == "down":
                                counter += 1
                                break
                        prediction += 1
                        current = [guard[0] + prediction, guard[1]]
                        if current[0] == len(room):
                            break
                except IndexError:
                    pass
                moveRight()
        path.append(guard.copy())
        directions.append(direction)
    except IndexError:
        break
print(counter)