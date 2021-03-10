# Add our dependencies.
import csv
import os
file_to_load = os.path.join("Resources", "election_results.csv")
# Add a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Open the election results and read the file.
with open(file_to_load) as election_data:
     # Read the file object with the reader function.
     file_reader = csv.reader(election_data)           
     # Print each row in the CSV file.
     for row in file_reader:
          print(row)