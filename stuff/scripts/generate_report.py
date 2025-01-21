from models import Student, Result
import csv

data = dict[str, Student]()

with open("data\data.csv") as f:
    reader = csv.DictReader(f)

    for row in reader:
        if row["student"] not in data:
            data[row["student"]] = Student(row["student"])

        result = Result(row["subject"],float(row["percentage"]),int(row["grade"]),)

        data[row["student"]].add_result(result)
        
with open("templates/head.html") as f:
    print(f.read())
for student in data.values():
    print(student)
with open("templates/tail.html") as f:
    print(f.read())

#for student_id, student in data.items():
#    print(student_id)
#    for result in student.results:
#        print(result)


