tab_odd = []
tab_even = []
counter = 1
with open("data") as file:
    for line in file:
        for i in line.split():
            i = int(i)
            if counter % 2 == 0:
                tab_odd.append(i)
            else:
                tab_even.append(i)
            counter += 1
# tab_odd.sort()
# tab_even.sort()
# result = 0
# temporary = 0
# for i in range(len(tab_odd)):
#     temporary = tab_odd[i] - tab_even[i]
#     if temporary < 0:
#         temporary *= -1
#         result += temporary
#     else:
#         result += temporary
# print(result)
result = 0
for i in tab_even:
    x = tab_odd.count(i)
    result += i * x
print(result)