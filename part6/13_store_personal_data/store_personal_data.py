def store_personal_data(person: tuple):
    name, age, height = person
    with open("people.csv", "a") as p:
        p.write(";".join([name,  str(age), str(height)]))


if __name__ == "__main__":
    store_personal_data(("Paul Paulson", 37, 175.5))