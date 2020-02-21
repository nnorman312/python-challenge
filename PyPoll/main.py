# Import csv
import os
import csv

# Explain path to csv
election_data = os.path.join("..", "Resources", "election_data.csv")

# Set variables    
votes_count = []
candidates = []
change_profit = []

# Open csv
with open(election_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    header = next(csvreader)
    for row in csvreader:
# Total number of votes cast
        votes_count.append(row[0])
# Candidates who received votes

# Percentage of votes each candidate won

# Total number of votes each candidate won

# Winner of the election


# Print results
print("Election Results")
print("---------------------------------")
print(f"Total Votes:{len(votes_count)}")
print("---------------------------------")


    