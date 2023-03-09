from datetime import datetime


def is_it_valid(pic: str):
    if not len(pic) == 11:
        return False
    control_chars = "0123456789ABCDEFHJKLMNPRSTUVWXY"
    udate, century, ident, char = pic[:6], pic[6:7], pic[7:10], pic[-1:]
    month, day = udate[2:4], udate[:2]
    if century not in "+-A":
        return False
    if century == "+":
        year = "18" + udate[-2:]
    if century == "-":
        year = "19" + udate[-2:]
    if century == "A":
        year = "20" + udate[-2:]
    try:
        valid_date = datetime(int(year), int(month), int(day))
        remainder = int(udate + ident) % 31  
    except ValueError:
        return False
    if not control_chars[remainder] == char:
        return False
    return True


if __name__ == "__main__":
    print(is_it_valid("230827-906F"))
    print(is_it_valid("080842-720N"))
    print(is_it_valid("290200A1239"))