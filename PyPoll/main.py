# Import csv
import os
import csv

# Explain path to csv
election_data = os.path.join("..", "Resources", "election_data.csv")

# Set variables and lists    
total_votes = 0
vote_count = []
candidates = {}
candidates_percent = {}
winner = ""
winner_count = 0

# Open csv
with open(election_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    header = next(csvreader)
    firstrow = next(csvreader)
    for row in csvreader:
# Total number of votes cast and candidates who received votes
        total_votes = total_votes + 1

        if row[2] in candidates.keys():
            candidates[row[2]] += 1
        else:
            candidates[row[2]] = 1
# Percentage of votes each candidate won
for key, value in candidates.items():
    candidates_percent[key] = round((value/total_votes)*100,2)
# Total number of votes each candidate won and winner of the election
for key in candidates.keys():
    if candidates[key] > winner_count:
        winner = key
        winner_count = candidates[key]

# Print results
print("Election Results")
print("---------------------------------")
print("Total Votes: " + str(total_votes))
print("---------------------------------")
for key, value in candidates.items():
    print(key + ": " + str(candidates_percent[key]) + "% (" + str(value) + ")")
print("---------------------------------")
print("Winner: " + winner)
print("---------------------------------")

# Export results via text file
output = os.path.join(".", 'Election Results.txt')
with open(output,"w") as new:
    new.write("Election Results")
    new.write("\n")
    new.write("------------------------")
    new.write("\n")
    new.write("Total Votes: " + str(total_votes))
    new.write("\n")
    new.write("------------------------")
    new.write("\n")
    for key, value in candidates.items():
        new.write(key + ": " + str(candidates_percent[key]) + "% (" + str(value) + ")")
    new.write("\n")
    new.write("------------------------")
    new.write("\n")
    new.write("Winner: " + winner)
    new.write("\n")
    new.write("------------------------")
    new.write("\n")