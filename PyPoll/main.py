import os
import csv
#from collections import Counter
#from operator import itemgetter

csvpath = os.path.join("election_data.csv")

total_votes = 0


candidates = []
votes = {}



with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvfile)

    for row in csvreader:
        #calculate total number of votes
        total_votes += 1

        #get a list of candidates
        if row[2] not in votes:
            #if the candidate is not in the dictionary, add the name.  This also counts as 1 vote.  
            # Add the names into the candidates list too. 
            votes[row[2]] = 1
            candidates.append(row[2])
            

        else:
            #if candidates are already listed, add 1 to ever duplicate. 
            votes[row[2]] += 1
        
    



    
    
    

print (total_votes)    
print (candidates)
print (votes)

