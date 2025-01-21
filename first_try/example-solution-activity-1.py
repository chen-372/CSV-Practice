import csv

# Define a new type to model a student:
class Student:
    # A student will consist of a game name (str)
    # and a top score (int).
    def __init__(self) -> None:
        self.game = ""
        self.top_score = -1

    # This is called when we apply the str function
    # to an instance of Student (for example, if we
    # try to print the instance).
    def __str__(self) -> str:
        return f"{self.game}; Score: {self.top_score}"


# Here are all the student names.
students = [
    "Charles",
    "Frank",
    "Antao",
    "Rain",
    "Cris",
    "Eric",
    "Franklin",
]

# Use the student names as keys, and create instances
# of the Student class defined above for each student:
student_dict = {student: Student() for student in students}

# Open the data file:
with open("data.csv") as f:
    # Use the csv library to handle the splitting,
    # removal of \n, quotation marks if any, etc.,
    # so that we can focus on the logic rather than
    # the details of string splitting and
    # manipulation.
    reader = csv.DictReader(f)

    # Go through each row in the data...
    for row in reader:
        # Read what data is stored in the row...
        name, game, score = row["Student"], row["Game"], int(row["Score"])

        # Identify which student instance we
        # should look at...
        student = student_dict[name]

        # If the student's current top score
        # is less than the score in the row...
        if student.top_score < score:
            # Update the student data...
            student.top_score = score
            student.game = game

# Output the updated data for each student.
for key in students:
    print(f"{key}: {student_dict[key]}")
