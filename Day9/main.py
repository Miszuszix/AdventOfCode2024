import time, os
start_time = time.time()
string = ""
counter = 0
even = True
with open("data_example", "r") as file:
    for line in file:
        line = line.strip()
        for char in line:
            for i in range(int(char)):
                if even:
                    string += str(counter)
                else:
                    string += "."
            if even:
                even = False
                counter += 1
            else:
                even = True
chars = list(string)
dot_index = 0
length = len(chars)
for index, char in enumerate(chars[::-1]):
    dot_index = chars[dot_index:].index(".") + dot_index
    print(index)
    if length - index <= dot_index:
        break
    if char != ".":
        chars[len(chars) - 1 - index], chars[dot_index] = chars[dot_index], chars[len(chars) - 1 - index]

result = 0
for index, number in enumerate(chars):
    if number == ".":
        break
    result += index * int(number)
print(result)
#89558806610