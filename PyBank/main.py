# module to create file paths across operating systems
import os
# module for reading CSV files
import csv

csvpath = os.path.join("Resources", "budget_data.csv")

# Open the CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvreader)

    #print(f"CSV Header: {csv_header}")

    total = 0

    for row in csvreader:

        input_date = row[0]
        input_profit_loss = int(row[1])

        total = total + input_profit_loss



    print ("Financial Analysis")
    print ("--------------------------")

    print("Total: $" + str(total))
    


        
