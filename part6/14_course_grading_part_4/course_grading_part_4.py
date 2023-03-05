data = {}

if True:
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
    exam_points = input("Exam points: ")
    course_info = input("Course information: ")
else:
    student_info = "students1.csv"
    exercise_data = "exercises1.csv"
    exam_points = "exam_points1.csv"
    course_info = "course1.txt"

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

with open(exam_points) as e:
    for i in e:
        line = i.split(";")
        if line[0] == "id":
            continue
        data[int(line[0])].append(sum(int(x.strip()) for x in line[1:]))

with open(course_info) as c:
    name, study_credits, info = None, None, None
    for i in c:
        line = i.strip()
        if "name:" in line:
            name = line.replace("name: ", "")
            continue
        study_credits = line.replace("study credits: ", "")

result_txt = f"{name}, {study_credits} credits\n"
result_txt += "=" * len(f"{name}, {study_credits} credits") + "\n"
result_txt += f"{'name':30}{'exec_nbr':10}{'exec_pts.':10}{'exm_pts.':10}{'tot_pts.':10}{'grade':10}\n"
result_csv = ""

for id in data:
    exercise_points = int((data[id][1] / 40) * 10) 
    total_points = data[id][2] + exercise_points
    grade = None

    if total_points < 15:
        grade = 0
    elif total_points < 18:
        grade = 1
    elif total_points < 21:
        grade = 2
    elif total_points < 24:
        grade = 3
    elif total_points < 28:
        grade = 4
    else:
        grade = 5
    
    result_csv += f"{id};{data[id][0]};{grade}\n"
    result_txt += f"{data[id][0]:30}{data[id][1]:<10}{exercise_points:<10}{data[id][2]:<10}{total_points:<10}{grade:<10}\n"

with open("results.csv", "w") as r:
    r.write(result_csv)

with open("results.txt", "w") as r:
    r.write(result_txt)