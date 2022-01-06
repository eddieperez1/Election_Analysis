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

#import csv and os libraries
import csv
import os

#Assign variable for file election_results
file_to_load = os.path.join("Resources","election_results.csv")

#Create filename variable to save election results analysis
file_to_save = os.path.join("analysis","election_analysis.txt")

#Open the election results and read the file_to_load.
with open(file_to_load) as election_data:

    #Read and analyze the data here
    #Read election_data
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)
    print(headers)

#Using open() function with "w" mode to write to file_to_save
with open(file_to_save,"w") as txt_file:

    #Write "Hello World" in txt file
    txt_file.write("Counties in the Election\n")
    txt_file.write("-------------------------\n")
    txt_file.write("Arapahoe\nDenver\nJefferson")
