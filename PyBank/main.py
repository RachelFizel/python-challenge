# module to create file paths across operating systems
import os
# module for reading CSV files
import csv

csvpath = os.path.join("Resources", "budget_data.csv")

# Open the CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvreader)

    count = 0
    total = 0
    greatest_increase_in_profit = 0
    greatest_decrease_in_profit = 0
    change_in_profit_loss = 0
    last_profit_loss = 0

    #loop through each row in the csv file and calculate difference and total
    for row in csvreader:

        input_date = row[0]
        input_profit_loss = int(row[1])
        difference_profit_loss = int(row[1]) - last_profit_loss
        
        count = count + 1

        total = total + input_profit_loss

        if (difference_profit_loss > greatest_increase_in_profit):
            greatest_increase_in_profit = difference_profit_loss
            greatest_increase_in_profit_month = input_date

        if (difference_profit_loss < greatest_decrease_in_profit):
            greatest_decrease_in_profit = difference_profit_loss
            greatest_decrease_in_profit_month = input_date

        last_profit_loss = input_profit_loss

        if count != 1:
            change_in_profit_loss = change_in_profit_loss + difference_profit_loss
    

    #output analysis to the terminal
    print ("  ")
    print ("Financial Analysis")
    print ("--------------------------")

    print("Total Months: " + str(count))

    print("Total: $" + str(total))

    average_change = change_in_profit_loss / (count - 1)
    average_change = round(average_change, 2)

    print("Average Change: $" + str(average_change))

    print("Greatest Increase in Profits: " + str(greatest_increase_in_profit_month) + " ($" + str(greatest_increase_in_profit) + ")")
    print("Greatest Decrease in Profits: " + str(greatest_decrease_in_profit_month) + " ($" + str(greatest_decrease_in_profit) + ")")

    #output analysis to a text file
    f = open("Financial Analysis.txt", "w")

    f.write ("Financial Analysis\n")
    f.write ("--------------------------\n")

    f.write("Total Months: " + str(count) + "\n")

    f.write("Total: $" + str(total) + "\n")

    f.write("Average Change: $" + str(average_change) + "\n")

    f.write("Greatest Increase in Profits: " + str(greatest_increase_in_profit_month) + " ($" + str(greatest_increase_in_profit) + ")\n")
    f.write("Greatest Decrease in Profits: " + str(greatest_decrease_in_profit_month) + " ($" + str(greatest_decrease_in_profit) + ")\n")

    
    f.close()
        
