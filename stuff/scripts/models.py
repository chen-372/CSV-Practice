from jinja2 import Template

with open("templates/report-template.html") as f:
    _template = Template(f.read())

class Result:
    def __init__(self, subject: str, percentage: float, grade: int) -> None:
        self.subject = subject
        self.percentage = percentage
        self.grade = grade



class Student:
    def __init__(self, student_id: str) -> None:
        self.student_id = student_id
        self.results = list[Result]()


    def add_result(self, result: Result) -> None:
        self.results.append(result)

    def __str__(self) -> str:
        return _template.render(
            student_id=self.student_id,
            results=self.results,
        )