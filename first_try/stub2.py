import csv

def bubble_sort(xs: list[int]) -> None:
    for i in range(len(xs)-1):
        if xs[i] > xs[i+1]:
            xs[i], xs[i+1] = xs[i+1], xs[i]

class Game:
    def __init__(self) -> None:
        self.score:list[int] = []
        self.name:dict[int:str] = {}

    def __str__(self) -> str:
        bubble_sort(self.score)
        return f"""  1. {self.name[self.score[0]]}: {self.score[0]}
  2. {self.name[self.score[1]]}: {self.score[1]}
  3. {self.name[self.score[2]]}: {self.score[2]}"""



           
games = [
    "Pacman",
    "Space Invaders",
    "Asteroids",
    "Frogger",
    "Pong",
    "Super Mario",
]

game_best:dict = {game: Game() for game in games}

with open("data.csv") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    
    for row in csv_reader:

        name = row["Student"]
        game = row["Game"]
        score = int(row["Score"])

        game_best[game].score.append(score)
        game_best[game].name.setdefault(score, name)

for game in game_best:
    print(f"{game}: \n{game_best[game]}")