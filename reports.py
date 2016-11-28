import csv

def count_games(file_name):
  counter = 0
  file =  open(file_name, mode="r")
  for lines in file:
        counter += 1
  return counter
