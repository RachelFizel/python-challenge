# module to create file paths across operating systems
import os
# module for reading CSV files
import csv

import operator


#use the first line to step through the code in visual studio
#csvpath = os.path.join("C:\\Users\\rache\\Desktop\\python-challenge\\PyPoll\\Resources", "election_data.csv")
csvpath = os.path.join("Resources", "election_data.csv")

total_count_of_votes = 0


# Open the CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvreader)

    #make a dictionary of the candidates
    candidates = {}

    #loop through each row in the csv file
    for row in csvreader:

        input_voter_id = row[0]
        input_county = row[1]
        input_candidate = row[2]

        #count the number of votes cast
        total_count_of_votes += 1

        #pull the vote count from the diction for the candidate that is in the input 
        vote_count = candidates.get(input_candidate)
        
        if vote_count is None:
            #if the input candidate is not in the list yet add it and set his vote count to 1
            candidates[input_candidate] = 1
            
        else:
            #the candidate is in the list so increase his vote count
            vote_count += 1
            #put that value back in the dictionary
            candidates[input_candidate] = vote_count
            


#print results to the terminal
print (" ")
print ("Election Results")
print ("-----------------------------")

print ("Total Votes: " + str(total_count_of_votes))
print ("-----------------------------")

#loop through each record in the dictionary and output the results
for key in candidates:
    vote_percentage = candidates[key] / total_count_of_votes
    vote_percentage = vote_percentage * 100
    
    print ("{}: {:.3f}% ({})".format(key,vote_percentage, candidates[key]))

winner = max(candidates.items(), key=operator.itemgetter(1))[0]

print ("-----------------------------")
print ("Winner: " + winner)
print ("-----------------------------")



#output analysis to a text file
f = open("Election Results.txt", "w")

f.write(" ")
f.write ("Election Results\n")
f.write ("-----------------------------\n")

f.write ("Total Votes: " + str(total_count_of_votes) + "\n")
f.write ("-----------------------------\n")

#loop through each record in the dictionary and output the results
for key in candidates:
    vote_percentage = candidates[key] / total_count_of_votes
    vote_percentage = vote_percentage * 100
    
    f.write ("{}: {:.3f}% ({})\n".format(key,vote_percentage, candidates[key]))
    
winner = max(candidates.items(), key=operator.itemgetter(1))[0]

f.write ("-----------------------------\n")
f.write ("Winner: " + winner + "\n")
f.write ("-----------------------------\n")
    
f.close()    

