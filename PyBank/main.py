import csv
import os

csvpath = os.path.join("budget_data.csv")

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvfile)
    
    total_months = sum(1 for row in csvreader)
    print (f"There are {total_months} months.")
    
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvfile)

    net_profit = 0
    for row in csvreader:
        
        net_profit += int(row[1])
        net_average = net_profit / total_months
        
    print (f"The netprofit/loss is {net_profit}.")
    print (net_average)


with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvfile)

    
    row_val = []
    for row in csvreader:
        row_val.append(int(row[1]))
        
print (row_val)    
change_val = []
for i in row_val:
    delta = 0
    delta = int(row_val[i+1]) - int(row_val[i])
    change_val.append(delta)

print (change_val)
        


