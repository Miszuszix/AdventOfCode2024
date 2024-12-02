with open("data_example") as file:
    safe = 0
    for line in file:
        data = line.split()
        data = list(map(int, data))
        skip = False
        desc = True
        asc = True
        temp = data
        counter = 0
        for i in range(len(temp)-1):
            if temp[i] > temp[i+1]:
                continue
            else:
                if counter == 0:
                    counter += 1
                    continue
                else:
                    desc = False
                    break
        print(desc)
        exit()
print(safe)