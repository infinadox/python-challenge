import os
import csv

# Load the CSV file
file_path = os.path.join('Resources', 'budget_data.csv')

# Initialize variables to store financial analysis metrics
total_months = 0
net_total = 0
previous_profit_loss = 0
monthly_changes = []
months = []

# Read the CSV file and calculate financial metrics
with open(file_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    
    for row in csvreader:
        # Count total months and calculate net total
        total_months += 1
        net_total += int(row[1])
        
        # Calculate monthly change in profit/loss
        if total_months > 1:
            monthly_change = int(row[1]) - previous_profit_loss
            monthly_changes.append(monthly_change)
            months.append(row[0])
        previous_profit_loss = int(row[1])

# Calculate average change, greatest increase, and greatest decrease
average_change = sum(monthly_changes) / len(monthly_changes)
greatest_increase = max(monthly_changes)
greatest_increase_month = months[monthly_changes.index(greatest_increase)]
greatest_decrease = min(monthly_changes)
greatest_decrease_month = months[monthly_changes.index(greatest_decrease)]

# Print the financial analysis results
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${round(average_change, 2)}")
print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})")

# Export the results to a text file
output_file = os.path.join('analysis', 'financial_analysis.txt')
with open(output_file, 'w') as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write("----------------------------\n")
    txtfile.write(f"Total Months: {total_months}\n")
    txtfile.write(f"Total: ${net_total}\n")
    txtfile.write(f"Average Change: ${round(average_change, 2)}\n")
    txtfile.write(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n")
    txtfile.write(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})\n")

print(f"\nFinancial analysis results have been exported to {output_file}")