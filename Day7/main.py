suma = 0
with open("data") as file:
    for line in file:
        line = line.split()
        result = line[0]
        number = int(result[:result.index(":")])
        line.pop(0)
        result, temp = number, number
        components = []
        sumOfComponents = 0
        for i in line:
            components.append(int(i))
        for i in components:
            sumOfComponents += i
            if temp % sumOfComponents == 0:
                temp /= sumOfComponents
                sumOfComponents = 0
                continue
        if temp == 1:
            suma += result
            continue
        components = components[::-1]
        for i in components:
            if temp % i == 0:
                temp /= i
                continue
            temp -= i
        if temp == 1:
            suma += result
print(suma)