from collections import defaultdict

student_grades = {
    "John": [43, 87, 94],
    "Jacob": [99, 87, 67],
    "Jane": [3, 100, 100]
}

"""
Dictionaries and defaultDicts
"""
def get_grades_naive(name: str) -> []:
    if name in student_grades:
        return student_grades[name]
    return []


def get_grades_better(name: str) -> []:
    return student_grades.get(name, [])


def get_grades_with_assignment(name: str) -> []:
    if name not in student_grades:
        student_grades[name] = []
    return student_grades[name]


def set_grades_naive(name: str, score: int):
    if name in student_grades:
        grades = student_grades[name]
    else:
        student_grades[name] = []
        grades = student_grades[name]
    grades.append(score)


def set_grades_better(name: str, score: int):
    grades = get_grades_with_assignment(name)
    grades.append(score)


student_grades = defaultdict(list, student_grades)

def set_grade_best(name: str, score: int):
    student_grades[name].append(score)

