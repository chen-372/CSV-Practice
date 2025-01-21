import csv

students = [
    "Charles",
    "Frank",
    "Antao",
    "Rain",
    "Cris",
    "Eric",
    "Franklin",
]

with open("data.csv") as csv_file:
    csv_reader = csv.reader(csv_file)
    line_count = 0
    best_score = dict.fromkeys(students, [0, None])

    for row in csv_reader:
        if line_count != 0:
            name = row[0]
            game = row[1]
            score = int(row[2])

            if best_score[name][0] < score: 
                best_score[name] = [score, game]
        line_count += 1

for name in best_score:
    print(f"{name}:\n\tBest score: {best_score[name][0]}\n\tGame: {best_score[name][1]}")

