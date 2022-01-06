#The data we need to retrieve.
# 1. The total number of votes cast
# 2. Complete list of candidates who received votes
# 3. The percentage of votes each candidate won 
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote.

#import csv and os libraries
import csv
import os

#Assign variable for file election_results
file_to_load = os.path.join("Resources","election_results.csv")

#Create filename variable to save election results analysis
file_to_save = os.path.join("analysis","election_analysis.txt")

# 1. Initialize a total_votes counter
total_votes = 0

#Initialize candidate name list
candidate_options = []
#Open the election results and read the file_to_load.
with open(file_to_load) as election_data:

    #Read and analyze the data here
    #Read election_data
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)
    
    #Find total votes
    for row in file_reader:
        # Add to the total vote count
        total_votes += 1

        #Find candidate name
        candidate_name = row[2]

        #If candidate name is not in candidate options...
        if candidate_name not in candidate_options:
            #Then Add candidate name to candidate options
            candidate_options.append(candidate_name)

# 3. Print the total votes
print(f'Total Votes: {total_votes:,}')
# Print candidate options
print(f'Candidates: {candidate_options}')
    

#Using open() function with "w" mode to write to file_to_save
with open(file_to_save,"w") as txt_file:

    #Write "Hello World" in txt file
    txt_file.write("Counties in the Election\n")
    txt_file.write("-------------------------\n")
    txt_file.write("Arapahoe\nDenver\nJefferson")
