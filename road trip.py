import csv
with open('states.csv', newline='') as f: 
  state = input('State: ')
  for line in csv.DictReader(f):
    if line['state'] == state:
      print('Capital:', line['capital'])