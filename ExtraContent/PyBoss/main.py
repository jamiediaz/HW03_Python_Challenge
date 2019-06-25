import os
import csv

us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

csvpath = os.path.join("employee_data.csv")

outcsv = os.path.join("new_emp_data.csv","w")

#create the file the data will be outputted to. 
file = open("new_emp_data.csv","w") 

#create the headers in new_emp_data.csv
file.write("Emp ID,")
file.write("First Name,")
file.write("Last Name,")
file.write("DOB,")
file.write("SSN,")
file.write("State,\n")

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvfile)

    for row in csvreader:
                
        # For every row in the employee_data.csv, 
        # process and write it to new_emp_data.csv
        # Do all this in a loop so as data streams in from employee_data, it's pushed to new_emp_data. 
        name = row[1]
        Fname, Lname = name.split(" ",1)
        SSN = list(row[3])
        SSN[0:6] = "*","*","*","-","*","*"
        #SSN[6:7] = "*","*"
        SSN="".join(SSN)
        file.write(f"{row[0]},{Fname},{Lname},{row[2]},{SSN},{us_state_abbrev[row[4]]},\n")
        
file.close()