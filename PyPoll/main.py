# module to create file paths across operating systems
import os
# module for reading CSV files
import csv

csvpath = os.path.join("Resources", "election_data.csv")


total_count_of_votes = 0


# Open the CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvreader)


    #loop through each row in the csv file
    for row in csvreader:

        input_voter_id = row[0]
        input_county = row[1]
        input_candidate = row[2]

        #count the number of votes cast
        total_count_of_votes += 1

   


print (" ")
print ("Election Results")
print ("------------------------")

print ("Total Votes: " + str(total_count_of_votes))
print ("------------------------")