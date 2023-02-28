def add_student(data: dict, name: str):
    if name not in data:
        data[name] = []


def print_student(data: dict, name: str):
    if name not in data:
        print(f"{name}: no such person in the database")
        return
    if not data[name]:
        print(f"{name}: \n no completed courses")
        return
    print(f"{name}: \n {len(data[name])} completed courses:")
    total = 0
    for x in data[name]:
        total += x[1]
        print(f"  {x[0]} {x[1]}")
    print(f" average grade {total / len(data[name])}")


def add_course(data: dict, name: str, course: tuple):
    if course[1] == 0:
        return
    if name not in data:
        return
    for x in range(len(data[name])):
        if data[name][x][0] == course[0]:
            if data[name][x][1] < course[1]:
                data[name][x] = course
                return
            return
    data[name].append(course)


def summary(data: dict):
    most_courses = (None, -float("inf"))
    best_average = (None, -float("inf"))
    print(f"students {len(data)}")
    for student in data:
        total = 0
        for grade in data[student]:
            total += grade[1]
        if total / len(data[student]) > best_average[1]:
            best_average = (student, total / len(data[student]))
        if len(data[student]) > most_courses[1]:
            most_courses = (student, len(data[student]))
    print(f"most courses completed {most_courses[1]} {most_courses[0]}")
    print(f"best average grade {best_average[1]} {best_average[0]}")


if __name__ == "__main__":
    students = {}
    add_student(students, "Peter")
    add_student(students, "Eliza")
    add_course(students, "Peter", ("Data Structures and Algorithms", 1))
    add_course(students, "Peter", ("Introduction to Programming", 1))
    add_course(students, "Peter", ("Advanced Course in Programming", 1))
    add_course(students, "Eliza", ("Introduction to Programming", 5))
    add_course(students, "Eliza", ("Introduction to Computer Science", 4))
    summary(students)