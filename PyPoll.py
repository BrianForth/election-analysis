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
# Open the election results and read the file.
with open(file_to_load) as election_data:
    #Read and analyze data here.
    file_reader = csv.reader(election_data)
    for row in file_reader:
        print(row) 
        