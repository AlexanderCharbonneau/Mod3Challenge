import csv
import os
import statistics

file = os.path.join('Resources', 'election_data.csv')

c_count = 0
d_count = 0
r_count = 0
c = "Charles Casper Stockham"
d = "Diana DeGette"
r = "Raymon Anthony Doane"

with open(file, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    headers = next(csv_reader)
    rows = list(csv_reader)
    total_v = len(rows)

    for row in rows:
        candidate = row[2]
        if candidate == c:
             c_count +=1
        elif candidate == d:
             d_count +=1
        elif candidate == r:
             r_count +=1


winner = ""

if c_count > d_count and c_count > r_count:
    winner = c
elif d_count > c_count and d_count > r_count:
    winner = d
elif r_count > c_count and r_count > d_count:
    winner = r


print("Election Results")
print("--------------------")
print("Total Votes", " ",total_v)
print("--------------------")
print(c, ": {:.2f}% ({})".format((c_count/total_v)*100, c_count))
print(d, ": {:.2f}% ({})".format((d_count/total_v)*100, d_count))
print(r, ": {:.2f}% ({})".format((r_count/total_v)*100, r_count))
print("--------------------")
print("Winner:", " ",winner)