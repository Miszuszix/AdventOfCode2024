def mul(a ,b):
    return a * b

global result
result = 0
global enabled
enabled = True

def findMul(line):
    global result
    global enabled
    x = line.find("mul")
    y = line.find("do()")
    z = line.find("don't()")
    print(f'x: {x}, y: {y}, z: {z}')
    if z != -1:
        if y != -1:
            if z < x and z < y:
                print("disabled")
                enabled = False
        else:
            if z < x:
                print("disabled")
                enabled = False
    if y != -1:
        if z != -1:
            if y < x and y < x:
                print("enabled")
                enabled = True
        else:
            if y < x:
                print("enabled")
                enabled = True
    if x != -1:
        line = line[x + 3:]
        if line[0] == '(':
            line = line[1:]
        else:
            return line
        x = line.find(",")
        if not line[:x].isdigit():
            return line
        a = int(line[:x])
        line = line[x + 1:]
        x = line.find(")")
        if x == 0 or x > 4:
            return line
        b = int(line[:x])
        print(a,b)
        if not enabled:
            return line
        result += mul(a,b)
        print(f'result: {result}')
    return line

with open("data") as file:
    for line in file:
        line = line.strip()
        print(line)
        while line.find("mul") != -1:
            line = findMul(line)

    print(result)