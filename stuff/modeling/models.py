class Student:
    def __init__(self, id) -> None:
        self.id = id

class Subject:
    def __init__(self, id) -> None:
        self.id = id

class Result:
    def __init__(self, id, grade, percentage, student_id, subject_id) -> None:
        self.id = id
        self.grade = grade
        self.percentage = percentage
        self.student_id = student_id
        self.subject_id = subject_id


import csv

students = dict[str, Student]()
subjects = dict[str, Subject]()
results = list[Result]()

with open("data.csv") as f:
    reader = csv.DictReader(f)

    for line in reader:

        if line["subject"] not in subjects:
            subjects[line["subject"]] = Subject(line["subject"])

        if line["student"] not in students:
            students[line["student"]] = Student(line["student"])

        results.append(Result(
            len(results), 
            line["grade"], 
            line["percentage"], 
            line["student"], 
            line["subject"]
            ))

print("Students:")
for k, student in students.items():
    print(f"{k}: {student}")

print("Subject:")
for k, subject in subjects.items():
    print(f"{k}: {subject}")

print("Result:")
for result in results:
    print(f"{result.id}: {result}")