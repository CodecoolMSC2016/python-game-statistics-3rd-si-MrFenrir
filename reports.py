def count_games(file_name):
  with open(file_name, mode="r") as file:
    counter = 0
    for lines in file:
            counter += 1
    return counter

def decide(file_name, year):
  with open(file_name, mode="r") as file:
    for lines in file:
        parts=lines.split("\t")
        game_year=int(parts[2])
        if game_year==year:
            return True
    return False