import csv
import os

csvpath = os.path.join("budget_data.csv")

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvfile)
    
    total_months = sum(1 for row in csvreader)
    print (f" There are {total_months} months.")
    
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvfile)

    net_profit = 0
    for row2 in csvreader:
        
        net_profit += int(row2[1])
        
    print (net_profit)



