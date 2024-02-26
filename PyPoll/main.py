import os
import csv

# Creates a dictionaries to store data
total_votes = {}
candidate_count = {}

poll_csv = os.path.join('Resources', 'election_data.csv')

with open(poll_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',')

    # Skips the header row of the csv file
    header = next(csv_file)

    for row in csv_reader:

        # Adds each unique value of the ballot ID column to a dictionary
        # Allows us to later count the total votes and eliminate any duplicate votes
        ballot_id = row[0]
        if ballot_id in total_votes:
            total_votes[ballot_id] = total_votes[ballot_id]+1
        else:
            total_votes[ballot_id] = 1

        # Adds each candidate name to a dictionary and counts the occurance of each candidate name
        candidates = row[2]
        if candidates in candidate_count:
            candidate_count[candidates] = candidate_count[candidates]+1
        else:
            candidate_count[candidates] = 1

# Creates variables to contain each candidate's votes to simplify referencing these values
cand1_count = candidate_count.get('Charles Casper Stockham')
cand2_count = candidate_count.get('Diana DeGette')
cand3_count = candidate_count.get('Raymon Anthony Doane')

# Calculates the percentage of votes each candidate received and rounds the value to 3 decimals
cand1_percent = round((cand1_count) / (len(total_votes)) * 100, 3)
cand2_percent = round((cand2_count) / (len(total_votes)) * 100, 3)
cand3_percent = round((cand3_count) / (len(total_votes)) * 100, 3)

# Determines which candidate is the winner based on who has the most votes
# Returns 'Inconclusive Results' if there isn't a candidate with the most votes
if cand1_count > cand2_count and cand1_count > cand3_count:
    winner = list(candidate_count.items())[0][0]
elif cand2_count > cand1_count and cand2_count > cand3_count:
    winner = list(candidate_count.items())[1][0]
elif cand3_count > cand1_count and cand3_count > cand2_count:
    winner = list(candidate_count.items())[2][0]
else:
    winner = 'Inconclusive Results'

# Prints the results of our analysis
print(f'Election Results\n_______________________\nTotal Votes: {len(total_votes)}\n_______________________\n{list(candidate_count.items())[0][0]}: {cand1_percent}% ({cand1_count})\n{list(candidate_count.items())[1][0]}: {cand2_percent}% ({cand2_count})\n{list(candidate_count.items())[2][0]}: {cand3_percent}% ({cand3_count})\n_______________________\nWinner: {winner}\n_______________________')

# Provides header names for output file
categories = ['Candidate', 'Percentage of Votes', 'Candidate Votes', 'Total Votes', 'Winner']

# Provides the statistical data for the output file
values1 = [list(candidate_count.items())[0][0], cand1_percent, cand1_count, len(total_votes), winner]
values2 = [list(candidate_count.items())[1][0], cand2_percent, cand2_count]
values3 = [list(candidate_count.items())[2][0], cand3_percent, cand3_count]

# Identifies where the output file will be saved    
output = os.path.join("Analysis", "Results.csv")

# Writes to the csv output file
with open(output, 'w') as csvfile:
    
    csvwriter = csv.writer(csvfile)

    csvwriter.writerow(categories)
    csvwriter.writerow(values1)
    csvwriter.writerow(values2)
    csvwriter.writerow(values3)