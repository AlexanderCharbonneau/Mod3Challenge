import csv
import os
import statistics

file = os.path.join('Resources', 'budget_data.csv')

dif_dict = {}

total_months = 0
total_dollar = 0

with open(file, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    headers = next(csv_reader)
    rows = list(csv_reader)
    total_months = len(rows)  
    total_dollar = sum(int(row[1]) for row in rows)
    for i in range(1, len(rows)):
        difference = int(rows[i][1]) - int(rows[i-1][1])
        dif_dict[rows[i][0]] = difference

average = statistics.mean(dif_dict.values())
max_dif = max(dif_dict.values())
min_dif = min(dif_dict.values())

max_month = ""
min_month = ""
for month, diff in dif_dict.items():
	if diff == max_dif:
		max_month = month
	if diff == min_dif:
		min_month = month

print("Financial Analysis")
print("--------------------")
print("Total Months: ", total_months)
print("Total: $", total_dollar)
print("Average Change: ", round(average, 2))
print("Greatest Increase in Profits: ", max_month, " ", "(", max_dif, ")")
print("Greatest Decrease in Profits: ", min_month, " ", "(", min_dif, ")")