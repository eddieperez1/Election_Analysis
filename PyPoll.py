#The data we need to retrieve.
# 1. The total number of votes cast
# 2. Complete list of candidates who received votes
# 3. The percentage of votes each candidate won 
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote.

# Open election_result.csv
file_to_load = 'Resources\election_results.csv'
with open(file_to_load) as election_data:

    # Perform Analysis
    print(election_data)

#Module 3.4.2 exercise 
import csv
import os

#Assign variable for file election_results
file_to_load = os.path.join("Resources","election_results.csv")

#Open the election results and read the file.
with open(file_to_load) as election_data:

    #print the file object
    print(election_data)