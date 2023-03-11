numbers = []

while True:
    get_number = int(input("Type in a number: "))
    if get_number == 0:
        break
    numbers.append(get_number)

number, repeated = 0, 0
count = { n: numbers.count(n) for n in numbers }
for c in count:
    if count[c] > repeated:
        number, repeated = c, count[c]

print("Biggest:", max(numbers))
print("Smallest:", min(numbers))
print("Number of numbers:", len(numbers))
print("Sum:", sum(numbers))
print("Most repeated:", number)
