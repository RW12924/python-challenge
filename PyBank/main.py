import os
import csv

budget_csv = os.path.join("Resources", "budget_data.csv")

with open(budget_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    # Skips the header row of the csv file
    header = next(csv_file)

    # Sets starting values and creates a list for data to be stored
    net_total = 0
    month_count = 0
    max_inc = 0
    max_dec = 0
    change = 0
    change_list = []
    

    for row in csv_reader:
        # Each row of the data represents one month. This iterates through the rows to count how many months/rows are in the data.
        month_count = month_count + 1

        # Adds each profit/loss to the total.
        net_total = (net_total + int(row[1]))

        # Calculates the change in profit/loss from one row to the next and adds that change to a list.
        change = (int(row[1]) - int(change))
        change_list.append(change)

        # Compares the change in profit/loss of the current row to our maximum increase to find the greatest increase in profits/losses.
        # Records the month that the change occurred.
        if change > max_inc:
            max_inc = change
            max_inc_row = row[0]
        
        # Compares the change in profit/loss of the current row to our maximum decrease to find the greatest decrease in profits/losses.
        # Records the month that the change occurred.
        if change < max_dec:
            max_dec = change
            max_dec_row = row[0]

        # Resets "change" to the current profit/loss row's value to prepare for the next iteration.
        change = row[1]

    # Removes the first value of the change list because we don't have data to calculate the change from the month before 10-Jan.
    change_list.pop(0)

    # Calculates the average change
    avg_change = round(sum(change_list)/len(change_list), 2)

    # Prints the results of the script
    print(f'Total Months: {month_count}')
    print(f'Total: ${net_total}')
    print(f'Average Change: ${avg_change}')
    print(f'Greatest Increase in Profits: {max_inc_row} (${max_inc})')
    print(f'Greatest Decrease in Profits: {max_dec_row} (${max_dec})')

# Provides header names for output file
categories = ['Total Months', 'Total', 'Average Change', 'Greatest Inc Month', 'Greatest Increase in Profits', 'Greatest Dec Month', 'Greatest Decrease in Profits']

# Provides the statistical data for the output file
values = [month_count, net_total, avg_change, max_inc_row, max_inc, max_dec_row, max_dec]

# Identifies where the output file will be saved    
output = os.path.join("Analysis", "Results.csv")

# Writes to the csv output file
with open(output, 'w') as csvfile:
    
    csvwriter = csv.writer(csvfile)

    csvwriter.writerow(categories)
    csvwriter.writerow(values)