from models import Student, Subject
import csv


data =  dict[str, Subject]()
# data={"bio":Subject, "BM": Subject....}

with open("data\data.csv") as f:
    reader = csv.DictReader(f)

    for row in reader: 
        if row["subject"] not in data:
            data[row["subject"]] = Subject(row["subject"])
        
        student = Student(
            row["student"],
            float(row["percentage"]),
            int(row["grade"]),
        )

        data[row["subject"]].add_student(student)
        #bio(Subject).add_student(student)


with open("template/head.html") as f:
    print(f.read())
    
sorted_keys = sorted(data.keys())

for subject in sorted_keys:
    print(data[subject])

with open("template/tail.html") as f:
    print(f.read())
