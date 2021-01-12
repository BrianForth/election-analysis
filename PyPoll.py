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

# Establish candidate list and county list
candidate_options = []
county_list = []
# Establish individual vote totals and county turnout
candidate_votes = {}
county_votes = {}
# Establish winning candidate variables
winning_candidate = ""
winning_count = 0
winning_percentage = 0
# Establish highest turnout county
turnout_county = ""
turnout_count = 0
turnout_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    #Read and analyze data here.
    file_reader = csv.reader(election_data)

    #Print headers.
    headers = next(file_reader)
    print(headers)
    for row in file_reader:
        candidate_name = row[2]
        county_name = row[1]
        # Add unique candidates and counties to their respective lists
        if candidate_name not in candidate_options:
            candidate_votes[candidate_name] = 0
            candidate_options.append(candidate_name)
        candidate_votes[candidate_name] += 1
        if county_name not in county_list:
            county_votes[county_name] = 0
            county_list.append(county_name)
        county_votes[county_name] += 1
        total_votes += 1
with open(file_to_save, "w") as txt_file:
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    #Save final count to text file.
    txt_file.write(election_results)

    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        if votes > winning_count and vote_percentage > winning_percentage:
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        # Print each candidate, vote count, and percentage to terminal
        print(candidate_results)
        # Save candidate results to the text file
        txt_file.write(candidate_results)

    # Print the winning candidate's results to the terminal.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)

    # Print county analysis to the terminal
    county_results = (
        f"\nElection Results by County\n"
        f"-------------------------\n")
    print(county_results, end="")
    #Save final count to text file.
    txt_file.write(county_results)

    # Reusing code for the candidates for the county
    for county_name in county_votes:
        votes = county_votes[county_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        if votes > turnout_count and vote_percentage > turnout_percentage:
            turnout_count = votes
            turnout_county = county_name
            turnout_percentage = vote_percentage
        county_results = (f"{county_name}: {vote_percentage:.1f}% ({votes:,})\n")
        # Print each county, vote count, and percentage to terminal
        print(county_results)
        # Save county results to the text file
        txt_file.write(county_results)
    
    # Print the highest turnout county's results to the terminal.
    turnout_county_summary = (
        f"-------------------------\n"
        f"County with the Highest Turnout: {turnout_county}\n"
        f"Total Votes from {turnout_county} County: {turnout_count:,}\n"
        f"Percent of Total Votes Cast: {turnout_percentage:.1f}%\n"
        f"-------------------------\n")
    print(turnout_county_summary)
    # Save the highest turnout county's results to the text file.
    txt_file.write(turnout_county_summary)
    