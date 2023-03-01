data = {}

if True:
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
else:
    student_info = "students1.csv"
    exercise_data = "exercises1.csv"

with open(student_info) as s:
    for i in s:
        line = i.split(";")
        if line[0] == "id":
            continue
        data[int(line[0])] = [f"{line[1]} {line[2].strip()}"]

with open(exercise_data) as e:
    for i in e:
        line = i.split(";")
        if line[0] == "id":
            continue
        data[int(line[0])].append(sum(int(x.strip()) for x in line[1:]))

for id in data:
    print(data[id][0], data[id][1]) 
