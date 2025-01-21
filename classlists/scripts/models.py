from jinja2 import Template


with open("template/report-template.html") as f:
    _template = Template(f.read())


class Student:
    def __init__(self, student_id: str, percentage: float, grade: int) -> None:
        self.student_id = student_id
        self.percentage = percentage
        self.grade = grade


class Subject:
    def __init__(self, subject: str) -> None:
        self.subject = subject
        self.students: list = list[Student]()
        self.total: float = float(0)

    def add_student(self, student: Student) -> None:
        self.total += student.percentage
        self.students.append(student)

    def __str__(self) -> str:
        self.students.sort(key=lambda student: student.percentage, reverse=True)
        mean = self.total / len(self.students)
        sd = float(0)
        for student in self.students:
            sd += (student.percentage - mean) ** 2

        sd = (sd / len(self.students)) ** 0.5

        return _template.render(
            subject=self.subject,
            students=self.students,
            average=round(mean, 1),
            stander_deviation=round(sd, 1),
        )
