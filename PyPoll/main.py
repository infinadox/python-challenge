import os
import csv

# Load the CSV file
file_path = os.path.join('Resources', 'election_data.csv')

# Initialize variables to store election analysis metrics
total_votes = 0
candidates = {}
winner = ''
winner_votes = 0

# Read the CSV file and calculate election metrics
with open(file_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    
    for row in csvreader:
        # Count total votes
        total_votes += 1
        
        # Add candidate to dictionary if not already present
        candidate_name = row[2]
        if candidate_name not in candidates:
            candidates[candidate_name] = 0
        
        # Increment candidate's vote count
        candidates[candidate_name] += 1

# Determine the winner based on popular vote
for candidate, votes in candidates.items():
    if votes > winner_votes:
        winner = candidate
        winner_votes = votes

# Calculate percentage of votes for each candidate
for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    candidates[candidate] = (percentage, votes)

# Print the election analysis results to the terminal
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate, (percentage, votes) in candidates.items():
    print(f"{candidate}: {percentage:.3f}% ({votes})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Export the results to a text file
output_file = os.path.join('analysis', 'election_results.txt')
with open(output_file, 'w') as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Total Votes: {total_votes}\n")
    txtfile.write("-------------------------\n")
    for candidate, (percentage, votes) in candidates.items():
        txtfile.write(f"{candidate}: {percentage:.3f}% ({votes})\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Winner: {winner}\n")
    txtfile.write("-------------------------\n")

print(f"\nElection analysis results have been exported to {output_file}")