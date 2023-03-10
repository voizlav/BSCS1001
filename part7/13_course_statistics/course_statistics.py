import urllib.request
from json import loads, dumps


def retrieve_all():
    get_data = loads(urllib.request.urlopen("https://studies.cs.helsinki.fi/stats-mock/api/courses").read())
    result = []
    for data in get_data:
        if data["enabled"]:
            result.append((data["fullName"], data["name"], data["year"], sum(data["exercises"])))
    return result


def retrieve_course(course_name: str):
    URL = f"https://studies.cs.helsinki.fi/stats-mock/api/courses/{course_name}/stats"
    get_data = loads(urllib.request.urlopen(URL).read())
    result = {
        "weeks": len(get_data),
        "students": 0,
        "hours": 0,
        "hours_average": 0,
        "exercises": 0,
        "exercises_average": 0
    }
    for data in get_data:
        if get_data[data]["students"] > result["students"]:
            result["students"] = get_data[data]["students"]
        result["hours"] += get_data[data]["hour_total"]
        result["exercises"] += get_data[data]["exercise_total"]
    result["hours_average"] = result["hours"] // result["students"]
    result["exercises_average"] = result["exercises"] // result["students"]
    return result


if __name__ == "__main__":
    print(retrieve_all())
    print(retrieve_course("docker2019"))