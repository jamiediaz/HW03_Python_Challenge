import os
import csv
 

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
            #else the candidates are already listed, add 1 for every duplicate. 
            votes[row[2]] += 1


       
    
    
#Print out a total of the votes casted
print (f"The total votes casted are: {total_votes}.")    
#Print out a list of the candidates
print (f"The following candidates are running:\n{candidates}")
#Print out the number of the votes they got
print (f"\n-------------Vote Tally----------------\n{votes}")

# It would not allow me to divide by total_votes.  It didn't like mixing int and dictionary values.  So I summed all the votes instead and used that to divide with. 
sum_votes = sum(votes.values())
for i in votes:
    votes[i] = float(round((votes[i]/sum_votes)*100))

#Print out what each candidate got in percent
print (f"\n------Results in percent-----------------\n{votes}")

#Declare a winner by taking the max value and somehow tying in the key associated with that max value. 
max_val = max(votes.values())
max_key = [k for k, v in votes.items() if v == max_val]

print (f"\n------------------------------------------\nThe winner is: {max_key} with {max_val}% of the vote")


file = open("results.txt","w")
file.write(f"---------Total Votes-------------\n{total_votes}\n\n")
file.write(f"---------The results are---------\n{votes}\n\n")
file.write(f"---------The Winner--------------\n{max_key} with {max_val}%")
file.close()