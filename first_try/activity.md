# Old fashioned arcade games

When Mr Ambler was absent from school, his computer science class decided to play old fashioned arcade games instead of doing their work. After each game they played, they recorded the game's name and the score achieved, and saved their data in the file, `data.csv`. For example, the first few lines in the file are:

```csv
Student,Game,Score
Antao,Frogger,542
Franklin,Space Invaders,427
Charles,Pong,459
Eric,Space Invaders,471
.
.
.
```

The first row contains the column names.

The second row records that Antao got a score of 542 when he played the game called *Frogger*.

The third row records that Franklin got a score of 427 when he played *Space Invaders*; etc.

Here is a list of all the students and all the games:

```python
students = [
    "Charles",
    "Frank",
    "Antao",
    "Rain",
    "Cris",
    "Eric",
    "Franklin",
]

games = [
    "Pacman",
    "Space Invaders",
    "Asteroids",
    "Frogger",
    "Pong",
    "Super Mario",
]
```

For the following activities, it might help to:

* Use the `csv` library, as described in the attached tutorial.
* Use `dict`s or `class`es to store data as you read through the csv file.
* Discuss your solutions with each other.

Your scripts should not read through the csv file more than once.

## Activity 1

Write a Python script that (1) reads through the csv file and (2) reports the highest score, and the game, that each student got.

For example, the output might be something like:

```
Charles:
  Best score: 786
  Game: Space Invaders

Frank:
  Best score: 756
  Game: Pacman

etc.
``` 

## Activity 2

Write a Python script that (1) reads through the CSV file and (2) reports the top three scores and players for each game.

For example, the output might be something like:

```
Pacman:
  1. Frank: 756
  2. Rain: 564
  3. Rain: 537

Space Invaders:
  1. Charles: 786
  2. Eric: 612
  3. Franklin: 594

etc.
```
