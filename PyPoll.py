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
