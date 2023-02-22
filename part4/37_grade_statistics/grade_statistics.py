def main():
    data = get_data()

    for student in data:
        student["exercise_points"] = exercises_to_points(student["exercises"])
        student["total_points"] = total_points(student["exercise_points"], student["exam_points"])
        student["grade"] = calculate_grade(student["total_points"])
        student["failed"] = fail(student["grade"])
        if auto_fail(student["exam_points"]):
            student["failed"] = True
    
    print("Statistics:")
    print(f"Points average: {average_points(data):.1f}")
    print(f"Pass percentage: {pass_percentage(data):.1f}")
    print("Grade distribution:")
    print_grades(grade_distribution(data))


def get_data() -> list:
    data = []
    while True:
        data_input = input("Exam points and exercises completed: ")
        if not data_input:
            break
        data.append(normalize_data(data_input))
    return data


def normalize_data(string: str) -> dict:
    points, exercises = string.split(" ")
    return {"exam_points": int(points), "exercises": int(exercises)}


def exercises_to_points(exercises: int) -> int:
    return exercises // 10


def total_points(exercise: int, exam: int) -> int:
    return exercise + exam


def average_points(data: list) -> float:
    return sum(student["total_points"] for student in data) / len(data)


def auto_fail(exam_points: int) -> bool:
    return exam_points < 10


def fail(grade: int) -> bool:
    return grade == 0


def pass_percentage(data: list) -> float:
    return (sum(not student["failed"] for student in data) / len(data)) * 100


def calculate_grade(points: int) -> int:
    if points < 15:
        return 0
    elif points < 18:
        return 1
    elif points < 21:
        return 2
    elif points < 24:
        return 3
    elif points < 28:
        return 4
    return 5


def grade_distribution(data: list) -> list:
    grades = ["" for _ in range(6)]
    for student in data:
        if student["failed"]:
            grades[0] += "*"
            continue
        grades[student["grade"]] += "*"    
    return grades


def print_grades(grades: list):
    x = 5
    for grade in grades[::-1]:
        print(f"{str(x): >3}: {grade}")
        x -= 1


main()