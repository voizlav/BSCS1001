layers = int(input("Layers: "))
length = layers * 2 - 1
result = {x: "" for x in range(length)}

for i in range(layers):
    row = ""
    for j in range(i + 1):
        row += chr(65 + layers - 1 - j)
        if j == i:
            row += chr(65 + layers - 1 - j) * (layers - i - 1)
    result[i] = row + row[-2::-1]
    result[length - i - 1] = row + row[-2::-1]

for row in result:
    print(result[row])