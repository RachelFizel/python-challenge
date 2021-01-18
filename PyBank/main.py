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

    count = 0
    total = 0
    greatest_increase_in_profit = 0

    for row in csvreader:

        input_date = row[0]
        input_profit_loss = int(row[1])

        count = count + 1

        total = total + input_profit_loss

        if (input_profit_loss > greatest_increase_in_profit):
            greatest_increase_in_profit = input_profit_loss
            greatest_increase_in_profit_month = input_date



    print ("  ")
    print ("Financial Analysis")
    print ("--------------------------")

    print("Total Months: " + str(count))

    print("Total: $" + str(total))

    print("Greatest Increase in Profits: " + str(greatest_increase_in_profit_month) + " (" + str(greatest_increase_in_profit) + ")")
    


        
