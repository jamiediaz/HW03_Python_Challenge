import csv
import os


csvpath = os.path.join("budget_data.csv")

net_profit = 0
total_months = 0
rev_change_avg = 0

prev_month = 0
rev_change = 0
greatest_increase = ["", 0]
greatest_decrease = ["", 999999999]

revenue_change_list = []


with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvfile)

    
    for row in csvreader:
        #calculate total months and net profit
        total_months += 1
        net_profit += int(row[1])
        
        
        #subtract current row[1] with the row[1] from the previous month
        rev_change = int(row[1])  - prev_month
        
        #update prev_month with the data from the current row[1] after substraction
        prev_month = int(row[1])
        
        #calculate greatest increase now to decrease the number of loops
        if (rev_change > greatest_increase[1]):
            greatest_increase[1] = rev_change
            greatest_increase[0] = row[0]

        if (rev_change < greatest_decrease[1]):
            greatest_decrease[1] = rev_change
            greatest_decrease[0] = row[0]
            
        #add the results in rev_change to the list for calculation
        revenue_change_list.append(int(rev_change))
        
        
#calculate net/profit change average
revenue_change_list.pop(0) 
rev_change_avg = sum(revenue_change_list) / len(revenue_change_list)




 
print (f"There are {total_months} months.")
print (f"The netprofit/loss is {net_profit}.")
print (f"The net/profit change average is: {rev_change_avg}")
print (f"The greatest average increase is: {greatest_increase[1]} on {greatest_increase[0]}.")
print (f"The greatest average decrease is: {greatest_decrease[1]} on {greatest_decrease[0]}.")

