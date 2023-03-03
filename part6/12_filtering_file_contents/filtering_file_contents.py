def filter_solutions():
    solutions = []
    correct = []
    incorrect = []
    with open("solutions.csv") as s:
        for i in s:
            line = i.strip().split(";")
            solutions.append({ line[0]: line[1:] })
    for solution in solutions:
        for person, problem_result in solution.items():
            problem, result = problem_result[0], int(problem_result[1])
            if "+" in problem:
                x, y = map(int, problem.split("+"))
                correct.append({ person: problem_result }) if x + y == result else incorrect.append({ person: problem_result })
                continue
            x, y = map(int, problem.split("-"))
            correct.append({ person: problem_result }) if x - y == result else incorrect.append({ person: problem_result })
    with open("correct.csv", "w") as c:
        for solution in correct:
            for person, problem_result in solution.items():
                c.write(f"{person};{';'.join(problem_result)}\n")
    with open("incorrect.csv", "w") as i:
        for solution in incorrect:
            for person, problem_result in solution.items():
                i.write(f"{person};{';'.join(problem_result)}\n")


if __name__ == "__main__":
    filter_solutions()