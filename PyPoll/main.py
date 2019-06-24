import os
import csv

csvpath = os.path.join("election_data.csv")

total_votes = 0


candidates = []



with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvfile)

    for row in csvreader:
        #calculate total number of votes
        total_votes += 1

        #get a list of candidates
        if row[2] not in candidates:
            candidates.append(row[2])



    
    
    

print (total_votes)    
print (candidates)