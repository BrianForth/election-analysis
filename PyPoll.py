# Needs:
# Total votes cast
# All candidates
# Each candidates vote total
# Each candidates vote share
# Winner based on FPTP
import csv
import os
# Assign a variable to read the file.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable for the file to save and the path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize total vote counter
total_votes = 0

#Establish candidate list
candidate_options = []
# Establish individual vote totals
candidate_votes = {}
#Establish winning candidate variables
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    #Read and analyze data here.
    file_reader = csv.reader(election_data)

    #Print headers.
    headers = next(file_reader)
    print(headers)
    for row in file_reader:
        candidate_name = row[2]
        # Add unique candidates to the list
        if candidate_name not in candidate_options:
            candidate_votes[candidate_name] = 0
            candidate_options.append(candidate_name)
        candidate_votes[candidate_name] += 1
        total_votes += 1

for candidate_name in candidate_votes:
    votes = candidate_votes[candidate_name]
    vote_percentage = float(votes) / float(total_votes) * 100
    if votes > winning_count and vote_percentage > winning_percentage:
        winning_count = votes
        winning_candidate = candidate_name
        winning_percentage = vote_percentage
    print(f"{candidate_name} received {vote_percentage:.1f}% ({votes:,} votes) of the vote.\n")
print(f"{winning_candidate} won the election with {winning_percentage:.1f}% ({winning_count:,} votes) of the vote.\n")


