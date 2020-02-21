# Import csv
import os
import csv

# Explain path to csv
budget_data = os.path.join("..", "Resources", "budget_data.csv")

# Set variables    
month_count = []
profit = []
change_profit = []

# Open csv
with open(budget_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    header = next(csvreader)
    for row in csvreader:
# Total number of months included in the dataset
        month_count.append(row[0])
# Net total amount of profit/losses over an entire period
        profit.append(int(row[1]))
for i in range(len(profit)-1):
    change_profit.append(profit[i+1]-profit[i])
# Average of the changes in profits/losses over the entire period
increase = max(change_profit)
decrease = min(change_profit)
# Greatest increase in profits (date and amount) over the entire period
month_increase = change_profit.index(max(change_profit))+1
# Greatest decrease in profits (date and amount) over the entire period
month_decrease = change_profit.index(min(change_profit))+1

# Print results
print("Financial Analysis")
print("---------------------------------")
print(f"Total Months:{len(month_count)}")
print(f"Total: ${sum(profit)}")    
print(f"Average Change: ${round(sum(change_profit)/len(change_profit),2)}")
print(f"Greatest Increase in Profits: {month_count[month_increase]} (${(str(increase))})")
print(f"Greatest Decrease in Profits: {month_count[month_decrease]} (${(str(decrease))})")   

# Export results via text file
output = os.path.join(".", 'output.txt')
with open(output,"w") as new:
    new.write("Financial Analysis")
    new.write("\n")
    new.write("------------------------")
    new.write("\n")
    new.write(f"Total Months:{len(month_count)}")
    new.write("\n")
    new.write(f"Total: ${sum(profit)}")
    new.write("\n")
    new.write(f"Average Change: ${round(sum(change_profit)/len(change_profit),2)}")
    new.write("\n")
    new.write(f"Greatest Increase in Profits: {month_count[month_increase]} (${(str(increase))})")
    new.write("\n")
    new.write(f"Greatest Decrease in Profits: {month_count[month_decrease]} (${(str(decrease))})")