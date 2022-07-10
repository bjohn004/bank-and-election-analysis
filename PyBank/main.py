import os 
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

# define variable for calculating the months
months = []
# define variable for calculating the change in profit losses
changes = []
# define variable for summing up the values of profits/losses over the entire period
net_total = 0

# perfrom  chocolate cake recipe to bring in csv file
with open (csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    csv_header = next(csvreader)

    # define variable to be used when calculating the changes in profits/losses
    prev = 0

    # loop through rows of csv file to help determine number of months, net total of profits/losses, and the changes in profits by month
    for row in csvreader:
        
        # this will be used to simply calculate the length of the list to determine number of months
        months.append(row)

        # sums up the total profits/losses
        net_total += (int(row[1]))

        # set current profit/loss to the current row/column 2
        current = int(row[1])

        # use current and prev values to calculate change and add to changes list
        changes.append(current - prev)

        # now set the previous value so the next month will be compared to the previous month
        prev = int(row[1])

    # remove the first item in the changes list since we are starting at that value and no change has occurred
    x = changes.pop(0)

    # calculate the average change of profits/losses
    average = sum(changes) / len(changes)

    # find the greatest increase and decrease in the changes list
    greatest_increase = max(changes)
    greatest_decrease = min(changes)


# perfrom  chocolate cake recipe again to be able to perform another for loop
with open (csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    csv_header = next(csvreader)  

    # define variable to be used when calculating the changes in profits/losses
    prev = 0
    
    # loop through rows of csv file    
    for row in csvreader:
        #set current profit/loss to the current row/column 2
        current = int(row[1])
        # calculation will be used to compare to the greatest increase and decrease
        change = current - prev

        # if the change calculated above is equal to the greatest increase/decrease calulated after the orignal for loop, then match with the month/year row
        if change == greatest_increase:
            greatest_increase_month = row[0]    
        if change == greatest_decrease:
            greatest_decrease_month = row[0]

        # now set the previous value so the next month will be compared to the previous month
        prev = int(row[1])
print("")
print("FINANCIAL ANALYSIS")
print("__________________________________________________________________________")
print("")
print("The total number of months is " + str(len(months)) + " months.")
print("The net total of profits/losses over the entire period is $" + str(net_total) + ".")
print("The average change in profits/losses is $" + str(round(average, 2)) + ".")
print("The greatest increase in profits was $" + str(greatest_increase) + " in the month of " + greatest_increase_month + ".")
print("The greatest decrease in profits was $" + str(greatest_decrease) + " in the month of " + greatest_decrease_month + ".")

# create text file to display results
txtpath = os.path.join('Analysis', 'bank_results.txt')

with open(txtpath, 'w') as txtfile:

    # write text to bank_results.txt file
    txtfile.write("FINANCIAL ANALYSIS")
    txtfile.write('\n')
    txtfile.write("-------------------------------")
    txtfile.write('\n')
    txtfile.write("The total number of months is " + str(len(months)) + " months.")
    txtfile.write('\n')
    txtfile.write("The net total of profits/losses over the entire period is $" + str(net_total) + ".")
    txtfile.write('\n')
    txtfile.write("The average change in profits/losses is $" + str(round(average, 2)) + ".")
    txtfile.write('\n')
    txtfile.write("The greatest increase in profits was $" + str(greatest_increase) + " in the month of " + greatest_increase_month + ".")
    txtfile.write('\n')
    txtfile.write("The greatest decrease in profits was $" + str(greatest_decrease) + " in the month of " + greatest_decrease_month + ".")